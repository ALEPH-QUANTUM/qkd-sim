from qkd.protocols import bb84_protocol


def qkd_decision(
    n=1000,
    attack=None,
    noise_rate=0.0,
    thresholds=None,
    seed=None,
):
    """
    Autonomy-grade decision interface.
    Deterministic if seed is provided.
    """

    full = bb84_protocol(
        n=n,
        attack=attack,
        noise_rate=noise_rate,
        thresholds=thresholds,
        seed=seed,
    )

    thresholds_used = thresholds if thresholds is not None else {
        "benign_noise_max": 0.03,
        "attack_min": 0.06,
    }

    return {
        "secure": full["secure"],
        "threat_level": full["threat_level"],
        "error_rate": full["error_rate"],
        "thresholds_used": thresholds_used,
        "seed": seed,
    }
