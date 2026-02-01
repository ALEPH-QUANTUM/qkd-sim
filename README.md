# qkd-sim

qkd-sim is a lightweight, research-stage simulator for  
Quantum Key Distribution (QKD) protocols.

It is developed under ℵ - QUANTUM, a quantum software initiative focused on
simulation, validation, and reliability of quantum systems.

This project is software-only and does **not** simulate quantum hardware,
qubits, or physical quantum devices.

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

Researchstage.

Interfaces, structure, and supported protocols may evolve.
The project prioritizes clarity and correctness over
performance or completeness.
