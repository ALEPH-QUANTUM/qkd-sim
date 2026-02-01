from qkd.protocols import bb84_protocol

def test_key_not_empty():
    key = bb84_protocol(500)
    assert len(key) > 0

