from qkd.protocols import bb84_protocol
from qkd import qkd_decision


def print_report(title, report):
    print(title)
    print(f"Raw bits sent:        {report['raw_bits']}")
    print(f"Matched bases:        {report['matched_bases']}")
    print(f"Final key length:     {report['final_key_length']}")
    print(f"Error rate (QBER):    {report['error_rate']:.4f}")
    print(f"Secure channel:       {report['secure']}")
    print(f"Threat level:         {report['threat_level']}")
    print(f"Threat reason:        {report['threat_reason']}")
    print("")


def print_decision(title, decision):
    print(title)
    print(f"Secure:              {decision['secure']}")
    print(f"Threat level:        {decision['threat_level']}")
    print(f"Error rate (QBER):    {decision['error_rate']:.4f}")
    print(f"Thresholds used:      {decision['thresholds_used']}")
    print("")


def main():
    # Full report (research output)
    report = bb84_protocol(1000)
    print_report("=== BB84 Full Report (No attack, No noise) ===", report)

    # Autonomy-grade decision (minimal output)
    decision = qkd_decision(1000)
    print_decision("=== Autonomy Decision (No attack, No noise) ===", decision)

    # Noise scenario
    report_noise = bb84_protocol(1000, noise_rate=0.01)
    print_report("=== BB84 Full Report (Noise 0.01) ===", report_noise)

    decision_noise = qkd_decision(1000, noise_rate=0.01)
    print_decision("=== Autonomy Decision (Noise 0.01) ===", decision_noise)

    # Attack scenario
    report_attack = bb84_protocol(1000, attack="intercept_resend")
    print_report("=== BB84 Full Report (Intercept-Resend) ===", report_attack)

    decision_attack = qkd_decision(1000, attack="intercept_resend")
    print_decision("=== Autonomy Decision (Intercept-Resend) ===", decision_attack)


if __name__ == "__main__":
    main()
