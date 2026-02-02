# QKD Metrics and Decision Criteria

This document defines the metrics produced by `qkd-sim`
and the rationale behind their interpretation.

The goal is not physical accuracy, but **clear, explicit,
and reproducible decision logic**.

---

## Raw Bits

**Definition:**  
Total number of quantum states transmitted.

**Purpose:**  
Baseline for all derived quantities.

---

## Matched Bases

**Definition:**  
Number of positions where sender and receiver used the same basis.

**Purpose:**  
Determines the maximum possible sifted key length.

---

## Final Key Length

**Definition:**  
Key length after basis sifting (and before advanced post-processing).

**Purpose:**  
Indicates usable secret material under idealized assumptions.

---

## Error Rate (QBER)

**Definition:**  
Fraction of mismatched bits within the sifted key.

QBER = errors / matched_bases


**Interpretation:**
- Low QBER -> channel likely uncompromised
- High QBER -> noise or active eavesdropping

This simulator treats QBER as a **decision signal**, not a physical measurement.

---

## Secure Flag

**Definition:**  
Boolean indicator derived from a fixed threshold rule.

secure = (QBER ≤ threshold)


**Purpose:**  
Provide a simple, explicit decision outcome suitable for
automation and higher-level logic.

The threshold is intentionally configurable and conservative.

---

## Design Philosophy

- Metrics are explicit and human-readable
- Thresholds are visible and adjustable
- Decisions are deterministic
- No hidden heuristics

This makes the simulator suitable for:
- education
- protocol comparison
- system-level reasoning
- autonomy research inputs

## Threat Classification

`qkd-sim` maps observed error rate into a coarse threat label:

- `benign_noise` — consistent with low channel noise
- `suspected_attack` — consistent with strong adversarial disturbance
- `unknown` — ambiguous zone requiring caution

This classification is deterministic and threshold-based by design.

## Configurable Thresholds

Threat classification thresholds in `qkd-sim` are explicit and configurable.

Default values:

- benign_noise_max = 0.03  
- attack_min = 0.06  

These thresholds define how observed error rates are interpreted.

Users may override thresholds to:
- explore sensitivity
- reproduce experiments
- model different channel assumptions
- integrate with higher-level decision logic

No thresholds are hidden or hard-coded into the decision process.

