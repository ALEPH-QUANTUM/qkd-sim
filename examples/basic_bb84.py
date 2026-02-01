from qkd.protocols import bb84_protocol

key = bb84_protocol(1000)
print("Key length:", len(key))
print("First 20 bits:", key[:20])

