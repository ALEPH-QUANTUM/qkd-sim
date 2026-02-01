def bb84_protocol(n=100):
    alice_bits = random_bits(n)
    alice_bases = random_bases(n)
    bob_bases = random_bases(n)

    bob_results = [
        measure(alice_bits[i], alice_bases[i], bob_bases[i])
        for i in range(n)
    ]

    sifted_key = [
        bob_results[i]
        for i in range(n)
        if alice_bases[i] == bob_bases[i]
    ]

    alice_sifted_key = [
        alice_bits[i]
        for i in range(n)
        if alice_bases[i] == bob_bases[i]
    ]

    errors = sum(
        1 for a, b in zip(alice_sifted_key, sifted_key) if a != b
    )

    key_length = len(sifted_key)
    error_rate = errors / key_length if key_length > 0 else 0
    secure = error_rate < 0.11

    return {
        "sent_bits": n,
        "sifted_key_length": key_length,
        "error_rate": error_rate,
        "secure": secure,
        "key": sifted_key
    }
