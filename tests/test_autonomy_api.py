from qkd import qkd_decision


def test_qkd_decision_minimal_keys():
    d = qkd_decision(n=500)

    assert isinstance(d, dict)
    assert set(d.keys()) == {"secure", "threat_level", "error_rate", "thresholds_used"}


def test_qkd_decision_attack_flags():
    d = qkd_decision(n=3000, attack="intercept_resend")

    assert d["secure"] is False
    assert d["threat_level"] == "suspected_attack"


def test_qkd_decision_noise_typically_ok():
    d = qkd_decision(n=3000, noise_rate=0.01)

    assert d["threat_level"] == "benign_noise"
