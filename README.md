# qkd-sim

Quantum Key Distribution protocol simulator for research and education.

This project implements software simulations of quantum key distribution
protocols with configurable noise, eavesdropping attacks, and post-processing.

Currently supported:
- BB84 (in progress)

Planned:
- E91
- Channel noise models
- Intercept-resend attack
- Error correction
- Privacy amplification

## Architecture

qkd/
  protocols/    -> QKD protocols
  channel.py    -> quantum channel models
  attacks.py    -> eavesdropper models
  reconciliation.py -> error correction
  privacy.py   -> privacy amplification

## Goal

Provide a clean, readable reference implementation of core QKD concepts.

_qkd-sim is a lightweight simulator for quantum key distribution missions, designed to generate mission-state scenarios and serve as autonomy input. It does NOT simulate quantum hardware - it models abstract channels and mission behavior relevant to ℵ - QUANTUM autonomy logic. 
ℵ - QUANTUM develops focused quantum software and simulation tools. Some of this research may later inform space systems via ℵ - SYSTEMS._
