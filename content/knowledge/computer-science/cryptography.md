---
title: "Cryptography"
slug: "cryptography"
type: "knowledge"
status: "seed"
date: 2025-12-18
domains: ["Computer Science", "Mathematics"]
tags: ["encryption", "decryption", "public-key", "private-key", "hashing", "security"]
difficulty: "advanced"
reading_time: "7 mins"
summary: "The practice and study of techniques for secure communication in the presence of third parties."
---

## Overview
**Cryptography** is the art of writing codes. It allows two people to communicate in secret, even if everyone else is listening.

## Core Idea
The core idea is **Asymmetry**. It should be easy to lock the box, but impossible to unlock it without the key.

## Formal Definition
The study of mathematical techniques related to aspects of information security such as confidentiality, data integrity, entity authentication, and data origin authentication.

## Intuition
-   **The Padlock:**
    -   *Symmetric Encryption:* We both have the same key. I lock it, send it to you, you unlock it. Problem: How do I get the key to you securely?
    -   *Public Key Encryption (Asymmetric):* I have a public lock (that anyone can use to lock a message to me) and a private key (that only I have). You put your message in a box, lock it with my public lock, and send it. Only I can open it.

## Examples
-   **HTTPS:** The lock icon in your browser. It uses TLS/SSL to encrypt your credit card number.
-   **Bitcoin:** Uses cryptography to prove ownership of money.
-   **Enigma Machine:** The Nazi code machine broken by Alan Turing.

## Common Misconceptions
-   **Misconception:** It's unhackable.
    -   **Correction:** It's computationally *infeasible*. It would take a billion years to guess the key. But quantum computers might change that.
-   **Misconception:** Security through obscurity works.
    -   **Correction:** Hiding *how* the system works is bad. The system should be secure even if the enemy knows exactly how it works (Kerckhoffs's Principle). Only the *key* must be secret.

## Related Concepts
-   **[Information Theory](file:///home/kdos/Anvil/kdos-main/content/knowledge/systems/information-theory.md):** Entropy is key to good keys.
-   **[Number Theory](file:///home/kdos/Anvil/kdos-main/content/knowledge/mathematics/number-theory.md):** The math behind RSA (prime numbers).

## Applications
-   **Privacy:** Signal, WhatsApp.
-   **Authentication:** Passwords (hashed, not stored as text).

## Criticism and Limitations
-   **The Human Factor:** The math is perfect, but the user wrote their password on a sticky note.

## Further Reading
-   *The Code Book* by Simon Singh
-   *Applied Cryptography* by Bruce Schneier
