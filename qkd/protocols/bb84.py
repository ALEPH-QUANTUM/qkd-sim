import random

def random_bits(n):
    return [random.randint(0, 1) for _ in range(n)]

def random_bases(n):
    return [random.choice(["Z", "X"]) for _ in range(n)]

def measure(bit, basis_sender, basis_receiver):
    if basis_sender == basis_receiver:
        return bit
    return random.randint(0, 1)

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

    return sifted_key
