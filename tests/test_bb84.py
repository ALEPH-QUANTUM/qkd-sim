from qkd.protocols import bb84_protocol
from qkd import qkd_decision


def test_deterministic_bb84_with_seed():
    r1 = bb84_protocol(2000, noise_rate=0.01, seed=42)
    r2 = bb84_protocol(2000, noise_rate=0.01, seed=42)

    assert r1["error_rate"] == r2["error_rate"]
    assert r1["threat_level"] == r2["threat_level"]


def test_autonomy_decision_deterministic():
    d1 = qkd_decision(3000, attack="intercept_resend", seed=123)
    d2 = qkd_decision(3000, attack="intercept_resend", seed=123)

    assert d1 == d2
