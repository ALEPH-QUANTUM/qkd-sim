# qkd-sim — Research Note (v0.1)

## Purpose

`qkd-sim` is a software-only simulator for studying **protocol-level behavior**
of Quantum Key Distribution (QKD) under noise and adversarial disturbance.

The project focuses on **decision-relevant signals** rather than physical
device modeling.

---

## Research Question

The simulator is designed to explore questions such as:

- How does observed error rate evolve with channel noise?
- At what point does protocol behavior transition from usable to unsafe?
- Can simple, explicit metrics support higher-level decision logic?

---

## Scope and Non-Goals

### In Scope
- QKD protocol logic (currently BB84)
- Abstract channel noise
- Simple eavesdropping models
- Deterministic, reproducible experiments
- Explicit security decision criteria

### Out of Scope
- Quantum hardware simulation
- Device-level physics
- Production cryptographic guarantees
- Full reconciliation and privacy amplification

---

## Design Principles

- Explicit assumptions
- Deterministic behavior (seeded randomness)
- Transparent thresholds
- Minimal, autonomy-grade outputs

---

## Intended Use

This tool is intended for:
- education
- protocol comparison
- exploratory research
- system-level reasoning

It is **not** intended to claim physical security guarantees.

---

## Status

Version: v0.1  
The API is frozen at this stage.
Future changes will be additive.
