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

