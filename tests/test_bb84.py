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
