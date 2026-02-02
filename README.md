# qkd-sim

**qkd-sim** is a research-stage simulator for **Quantum Key Distribution (QKD)** protocols.
It is designed for **protocol behavior analysis** (noise, attacks, post-processing) and for
producing **reliability metrics** that can feed higher-level decision logic.

Developed under **ℵ – QUANTUM** (software-first quantum simulation and reliability tooling).

This project is software-only and does **not** simulate quantum hardware,
qubits, or physical quantum devices.


## What this project is (and is not)

### It is
- a clean reference implementation of QKD protocol logic
- a simulator of abstract channels, noise, and eavesdropping models
- a producer of observable metrics (e.g., error rate) for analysis and validation

### It is not
- a quantum computer simulator
- a qubit/optics hardware model
- a flight system
---

## Purpose

Quantum Key Distribution protocols are conceptually simple but
operationally fragile.

`qkd-sim` provides a **clean, readable reference implementation** of core QKD
concepts suitable for:

- research exploration
- education
- protocol comparison
- higher-level system modeling

The simulator models abstract quantum channels and protocol behavior
rather than device-level physics.

---

## Scope

`qkd-sim` focuses on:

- QKD protocol logic
- abstract channel noise effects
- eavesdropping strategies
- classical post-processing stages

It explicitly excludes:

- quantum hardware simulation
- qubit-level physical modeling
- device-specific effects

---

## Supported Protocols

**In progress**
- BB84

**Planned**
- E91
- configurable channel noise models
- intercept–resend attack
- error correction
- privacy amplification

---

## Architecture Overview

qkd/
--> protocols/ # QKD protocol implementations
--> channel.py # Abstract quantum channel models
--> attacks.py # Eavesdropper models
--> reconciliation.py # Error correction
--> privacy.py # Privacy amplification


The architecture is intentionally modular to support experimentation,
analysis, and future extensions.

---

## Observed metrics (current)

The simulator outputs a simple report rather than only returning a key:

- `raw_bits` - total bits sent
- `matched_bases` - how many bases matched (sifted set size)
- `final_key_length` - resulting key size after sifting
- `error_rate` - observed bit error rate (QBER)
- `secure` - boolean decision based on a threshold rule

These values are intended for **analysis and decision logic**, not performance claims.

---

## Relationship to Autonomy & Systems Research

Simulation outputs from `qkd-sim` can be used to generate
**protocol-level behavior and reliability indicators**.

These outputs may serve as inputs to higher-level decision logic
(e.g. mission or system autonomy research).

This connection is conceptual, not operational or flight-related.

---

## Relationship Between ℵ - QUANTUM and ℵ - SYSTEMS

- **ℵ - QUANTUM** explores quantum computing and communication foundations
  through focused software and simulation tools.
- **ℵ - SYSTEMS** applies selected results to space mission
  and autonomy contexts.

The two initiatives are related but distinct in scope.

---

## Status

Research-stage.

Interfaces, structure, and supported protocols may evolve.
The project prioritizes clarity and correctness over
performance or completeness.

---

## Quick:


python examples/basic_bb84.py 

## Autonomy-grade API

If you only need decision signals (for higher-level logic), use:

```python
from qkd import qkd_decision

decision = qkd_decision(n=1000, noise_rate=0.01)
print(decision)

This returns only:

secure

threat_level

error_rate

thresholds_used
