DEFAULT_THRESHOLDS = {
    "benign_noise_max": 0.03,
    "attack_min": 0.06,
}

def bb84_protocol(n=1000, attack=None, noise_rate=0.0):

if noise_rate > 0.0:
    from qkd.channel import noisy_channel
    transmitted_bits = noisy_channel(transmitted_bits, noise_rate)


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

# Threat classification (simple, explicit, tunable)
# I can adjust these later, but keep them visible.
BENIGN_NOISE_MAX = 0.03
ATTACK_MIN = 0.06

if result["error_rate"] <= BENIGN_NOISE_MAX:
    threat_level = "benign_noise"
    threat_reason = "Error rate consistent with low channel noise"
elif result["error_rate"] >= ATTACK_MIN:
    threat_level = "suspected_attack"
    threat_reason = "Error rate exceeds attack suspicion threshold"
else:
    threat_level = "unknown"
    threat_reason = "Error rate in ambiguous zone"

result["threat_level"] = threat_level
result["threat_reason"] = threat_reason


    return {
        "sent_bits": n,
        "sifted_key_length": key_length,
        "error_rate": error_rate,
        "secure": secure,
        "key": sifted_key
    }
