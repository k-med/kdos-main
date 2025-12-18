---
title: "Quantum Information Theory"
slug: "quantum-information-theory"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Information Theory"
  - "Physics"
  - "Quantum Mechanics"
tags:
  - "qubit"
  - "entanglement"
  - "superposition"
  - "teleportation"
  - "quantum-computing"
  - "no-cloning"
difficulty: "advanced"
reading_time: 7
summary: >
  Quantum information theory is the study of how information is processed and transmitted using quantum mechanical systems. It generalizes classical information theory to the quantum realm.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Classical bits are 0 or 1. Quantum bits (qubits) can be 0, 1, or *both at the same time*. This changes the rules of information.

## Core Idea
**Superposition:** A qubit exists in a state $\alpha|0\rangle + \beta|1\rangle$. It contains more "potential" information than a bit, but when you measure it, it collapses to 0 or 1.

## Formal Definition (if applicable)
**Entanglement:** "Spooky action at a distance." Two qubits can be linked so that measuring one instantly determines the state of the other, even if they are light-years apart.

## Intuition
- **No-Cloning Theorem:** You cannot copy a qubit. (If you could, you could violate the uncertainty principle). This makes quantum money theoretically impossible to counterfeit.
- **Quantum Teleportation:** Moving the *state* of a qubit to another location (destroying the original).

## Examples
- **Quantum Key Distribution (BB84):** Using physics to detect eavesdroppers. If Eve tries to measure the key, she disturbs the state (Heisenberg Uncertainty), and Alice and Bob know they are being watched.
- **Shor's Algorithm:** A quantum computer can factor large numbers exponentially faster than a classical computer, breaking RSA encryption.

## Common Misconceptions
- "Quantum computers try every answer at once." (Not quite. They use interference to cancel out wrong answers and amplify the right one).
- "Faster than light communication." (Entanglement cannot transmit information faster than light. You still need a classical channel to decode the result).

## Related Concepts
- **Von Neumann Entropy:** The quantum version of Shannon entropy.
- **Decoherence:** The environment messing up the quantum state (why quantum computers are hard to build).

## Applications
- **Cryptography:** Post-quantum crypto.
- **Simulation:** Simulating molecules for drug discovery.

## Criticism / Limitations
Quantum computers are extremely fragile and error-prone (Noise).

## Further Reading
- Nielsen & Chuang, *Quantum Computation and Quantum Information*
- Wilde, *Quantum Information Theory*
