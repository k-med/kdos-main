---
title: "Cryptography"
slug: "cryptography"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Information Theory"
  - "Computer Science"
  - "Mathematics"
tags:
  - "encryption"
  - "decryption"
  - "public-key"
  - "private-key"
  - "rsa"
  - "hashing"
  - "security"
difficulty: "intermediate"
reading_time: 6
summary: >
  Cryptography is the practice and study of techniques for secure communication in the presence of third parties called adversaries.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Alice wants to send a message to Bob without Eve reading it. For thousands of years, they used secret codes. Today, we use math.

## Core Idea
**Symmetric vs. Asymmetric:**
- **Symmetric (AES):** Same key locks and unlocks. Fast, but how do you share the key?
- **Asymmetric (RSA):** Public Key locks, Private Key unlocks. Anyone can send you a secret message, but only you can read it.

## Formal Definition (if applicable)
**Kerckhoffs's Principle:** A cryptosystem should be secure even if everything about the system, except the key, is public knowledge. (Security through obscurity is bad).

## Intuition
- **Hashing:** A one-way function. You can turn a password into a hash ("123456" -> "e10adc..."), but you can't turn the hash back into the password. Used for storing passwords.
- **Digital Signature:** Proving you wrote the message. (Encrypting with your Private Key).

## Examples
- **Enigma Machine:** The Nazi code machine broken by Alan Turing.
- **HTTPS:** The lock icon in your browser. Uses TLS (Transport Layer Security) to encrypt traffic.
- **Bitcoin:** Uses cryptography to prove ownership of money.

## Common Misconceptions
- "Encryption is unbreakable." (It's only computationally infeasible. A quantum computer could break RSA).
- "I have nothing to hide." (Privacy is a fundamental right. Encryption protects your bank account, not just your secrets).

## Related Concepts
- **Steganography:** Hiding the message inside an image.
- **Quantum Cryptography:** Using physics to detect eavesdroppers (QKD).
- **Zero-Knowledge Proof:** Proving you know a secret without revealing the secret.

## Applications
- **E-commerce:** Credit card transactions.
- **VPN:** Hiding your IP address.
- **Messaging:** WhatsApp/Signal (End-to-End Encryption).

## Criticism / Limitations
"Rubber-hose cryptanalysis." It's easier to beat someone until they tell you the password than to break the encryption.

## Further Reading
- Singh, *The Code Book*
- Schneier, *Applied Cryptography*
