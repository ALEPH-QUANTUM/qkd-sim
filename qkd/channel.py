import random


def noisy_channel(bits, noise_rate=0.02):
    """
    Flip bits with probability = noise_rate.
    Models benign channel noise.
    """
    noisy_bits = []

    for bit in bits:
        if random.random() < noise_rate:
            noisy_bits.append(1 - bit)
        else:
            noisy_bits.append(bit)

    return noisy_bits

