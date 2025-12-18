---
title: "Quantum Computing"
slug: "quantum-computing"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Computer Science"
  - "Physics"
tags:
  - "qubits"
  - "superposition"
  - "entanglement"
  - "algorithms"
  - "shor"
  - "grover"
difficulty: "advanced"
reading_time: 6
summary: >
  Quantum computing is a type of computation that harnesses the collective properties of quantum states, such as superposition, interference, and entanglement, to perform calculations. The devices that perform these computations are known as quantum computers.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Classic computers are just really fast light switches. They are either On (1) or Off (0). Quantum computers are different. They use the laws of quantum mechanics to be On and Off *at the same time*. This allows them to solve certain problems (like breaking codes) billions of times faster than the most powerful supercomputer.

## Core Idea
The core idea is **The Qubit**.
-   **Bit:** A coin that is either Heads or Tails.
-   **Qubit:** A spinning coin. It is a mix of Heads and Tails until you stop it (measure it).

## Formal Definition
A model of computation based on the principles of quantum theory.
Key concepts:
1.  **Superposition:** Being in multiple states at once.
2.  **Entanglement:** Two qubits are linked. If you measure one, the other instantly changes, even if it is on the other side of the universe.

## Intuition
Imagine you are looking for a needle in a haystack.
-   **Classic Computer:** Picks up one piece of hay at a time. "Is this it? No. Is this it? No."
-   **Quantum Computer:** Looks at *every* piece of hay simultaneously. "Found it."

## Examples
-   **Shor's Algorithm:** A math trick that can factor huge numbers instantly. This is scary because all internet security (RSA encryption) is based on the fact that factoring huge numbers is hard. A quantum computer could hack every bank in the world.
-   **Drug Discovery:** Simulating a molecule is hard because electrons are quantum. A classic computer can't do it well. A quantum computer can simulate nature perfectly because it *is* nature.

## Common Misconceptions
-   **They are faster at everything:** No. For watching Netflix or writing Word docs, your laptop is better. Quantum computers are only faster for specific math problems (Optimization, Factoring).
-   **They will be on your desk:** They need to be kept at absolute zero (-273°C) to work. You will access them via the cloud, not have one in your house.

## Related Concepts
-   **Quantum Supremacy:** The moment a quantum computer solves a problem that a classic computer cannot (Google claimed this in 2019 with the Sycamore processor).
-   **Decoherence:** The enemy. If a qubit touches a single air molecule, it stops spinning and becomes a normal bit. Keeping them isolated is the hardest engineering challenge.

## Applications
-   **Logistics:** Finding the absolute best route for 1,000 delivery trucks (The Traveling Salesman Problem).
-   **Batteries:** Designing new materials for electric cars.

## Criticism / Limitations
-   **Error Rate:** Qubits are fragile. They make mistakes. We need "Error Correction" (using 1,000 physical qubits to make 1 logical qubit) to make them useful.

## Further Reading
-   Nielsen, Michael and Chuang, Isaac. *Quantum Computation and Quantum Information*. (The standard textbook).
-   Deutsch, David. *The Fabric of Reality*.
