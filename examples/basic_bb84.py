from qkd.protocols import bb84_protocol


def print_result(title, result):
    print(title)
    print(f"Raw bits sent:        {result['raw_bits']}")
    print(f"Matched bases:        {result['matched_bases']}")
    print(f"Final key length:     {result['final_key_length']}")
    print(f"Error rate (QBER):    {result['error_rate']:.4f}")
    print(f"Secure channel:       {result['secure']}")
    print("")


def main():
    print("=== ℵ - QUANTUM | qkd-sim | BB84 Demo ===\n")

    # Baseline run (no attack)
    baseline = bb84_protocol(1000)
    print_result("---- Baseline (no attack) ----", baseline)

    # Attack run (intercept–resend)
    attacked = bb84_protocol(1000, attack="intercept_resend")
    print_result("---- With intercept–resend attack ----", attacked)

    # Quick interpretation
    if baseline["secure"] and not attacked["secure"]:
        print("Interpretation: Attack increases QBER and triggers rejection (expected).")
    else:
        print("Interpretation: Check thresholds/implementation if results look unexpected.")


if __name__ == "__main__":
    main()

print("\n--- Running with benign channel noise ---")
noise_result = bb84_protocol(1000, noise_rate=0.01)

print(f"Error rate (QBER): {noise_result['error_rate']:.4f}")
print(f"Secure channel:    {noise_result['secure']}")
print(f"Threat level:        {result['threat_level']}")
print(f"Threat reason:       {result['threat_reason']}")
