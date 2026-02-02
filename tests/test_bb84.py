from qkd.protocols import bb84_protocol


def test_bb84_returns_report():
    result = bb84_protocol(500)

    # basic structure
    assert isinstance(result, dict)

    # required fields
    assert "raw_bits" in result
    assert "matched_bases" in result
    assert "final_key_length" in result
    assert "error_rate" in result
    assert "secure" in result

    # sanity checks
    assert result["raw_bits"] > 0
    assert result["matched_bases"] >= 0
    assert result["final_key_length"] >= 0
    assert 0.0 <= result["error_rate"] <= 1.0


def test_intercept_resend_detected():
    """
    Intercept–resend should introduce a noticeable error rate
    and cause the security decision to fail (secure == False).
    """
    result = bb84_protocol(1000, attack="intercept_resend")

    assert isinstance(result, dict)
    assert "error_rate" in result
    assert "secure" in result

    # conservative threshold: intercept–resend should push errors up
    assert result["error_rate"] > 0.05
    assert result["secure"] is False

def test_noise_does_not_always_break_security():
    result = bb84_protocol(2000, noise_rate=0.01)

    assert result["error_rate"] < 0.05
    assert result["secure"] is True


def test_attack_breaks_security_more_than_noise():
    noisy = bb84_protocol(2000, noise_rate=0.01)
    attacked = bb84_protocol(2000, attack="intercept_resend")

    assert attacked["error_rate"] > noisy["error_rate"]
    assert attacked["secure"] is False
