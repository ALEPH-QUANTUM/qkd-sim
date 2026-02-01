from qkd.protocols import bb84_protocol


def main():
    result = bb84_protocol(1000)

    print("=== BB84 Simulation Result ===")
    print(f"Raw bits sent:        {result['raw_bits']}")
    print(f"Matched bases:        {result['matched_bases']}")
    print(f"Final key length:     {result['final_key_length']}")
    print(f"Error rate (QBER):    {result['error_rate']:.4f}")
    print(f"Secure channel:       {result['secure']}")

    if result["secure"]:
        print("\nResult: Key accepted.")
    else:
        print("\nResult: Key rejected due to high error rate.")


if __name__ == "__main__":
    main()
