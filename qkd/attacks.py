import random


def intercept_resend(bits, bases):
    """
    Simple intercept–resend attack.

    Eve measures each qubit in a random basis and resends it.
    This introduces detectable errors.
    """
    eve_bits = []
    eve_bases = []

    for bit in bits:
        eve_basis = random.choice([0, 1])
        eve_bases.append(eve_basis)

        # Eve measures (random if basis mismatch)
        if eve_basis == 0:
            eve_bits.append(bit)
        else:
            eve_bits.append(random.choice([0, 1]))

    return eve_bits, eve_bases
