import random

from qkd.attacks import intercept_resend
from qkd.channel import noisy_channel

DEFAULT_THRESHOLDS = {
    "benign_noise_max": 0.03,
    "attack_min": 0.06,
}


def bb84_protocol(n=1000, attack=None, noise_rate=0.0, thresholds=None):
    if thresholds is None:
        thresholds = DEFAULT_THRESHOLDS

    benign_noise_max = thresholds["benign_noise_max"]
    attack_min = thresholds["attack_min"]

    # Alice prepares bits and bases
    bits = [random.choice([0, 1]) for _ in range(n)]
    bases = [random.choice([0, 1]) for _ in range(n)]

    # Transmission (optional attack)
    if attack == "intercept_resend":
        transmitted_bits, transmitted_bases = intercept_resend(bits, bases)
    else:
        transmitted_bits, transmitted_bases = bits, bases

    # Channel noise
    if noise_rate > 0.0:
        transmitted_bits = noisy_channel(transmitted_bits, noise_rate)

    # Bob chooses bases
    bob_bases = [random.choice([0, 1]) for _ in range(n)]

    # Sifting
    sifted_alice = []
    sifted_bob = []

    for i in range(n):
        if bases[i] == bob_bases[i]:
            sifted_alice.append(bits[i])
            sifted_bob.append(transmitted_bits[i])

    matched_bases = len(sifted_alice)

    # Error calculation
    errors = sum(
        1 for a, b in zip(sifted_alice, sifted_bob) if a != b
    )

    error_rate = errors / matched_bases if matched_bases > 0 else 0.0

    # Security decision
    secure = error_rate <= benign_noise_max

    # Threat classification
    if error_rate <= benign_noise_max:
        threat_level = "benign_noise"
        threat_reason = "Error rate consistent with low channel noise"
    elif error_rate >= attack_min:
        threat_level = "suspected_attack"
        threat_reason = "Error rate exceeds attack suspicion threshold"
    else:
        threat_level = "unknown"
        threat_reason = "Error rate in ambiguous zone"

    return {
        "raw_bits": n,
        "matched_bases": matched_bases,
        "final_key_length": matched_bases,
        "error_rate": error_rate,
        "secure": secure,
        "threat_level": threat_level,
        "threat_reason": threat_reason,
    }
