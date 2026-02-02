# Modeling Assumptions

This document lists explicit assumptions made by `qkd-sim`.

The simulator prioritizes clarity and reproducibility over physical realism.

---

## Quantum State Modeling

- Quantum states are modeled abstractly.
- No qubit-level physics is simulated.
- Measurement outcomes are probabilistic by design.

---

## Channel Model

- Noise is modeled as independent bit flips.
- No temporal correlation is assumed.
- Loss is not explicitly modeled.

---

## Attacker Model

- Intercept–resend is idealized.
- Eve has no memory or adaptive strategy.
- Attacks are not stealth-optimized.

---

## Security Decisions

- Security is determined via threshold rules.
- Thresholds are configurable and visible.
- No statistical confidence bounds are computed.

---

## Non-Goals

This simulator does not aim to:
- reproduce laboratory results
- replace hardware-level simulators
- claim physical security guarantees
