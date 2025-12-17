---
title: "Cybersecurity"
slug: "cybersecurity"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Computer Science"
tags:
  - "encryption"
  - "authentication"
  - "network-security"
  - "vulnerabilities"
  - "malware"
  - "cryptography"
difficulty: "intermediate"
reading_time: 6
summary: >
  Cybersecurity is the practice of protecting systems, networks, and programs from digital attacks. These cyberattacks are usually aimed at accessing, changing, or destroying sensitive information.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
It is an arms race. Defenders try to patch holes; attackers try to find new ones. As we connect more devices to the internet (cars, pacemakers, toasters), the attack surface grows.

## Core Idea
**CIA Triad:**
1.  **Confidentiality:** Only authorized people can see the data (Encryption).
2.  **Integrity:** The data hasn't been tampered with (Hashing).
3.  **Availability:** The system is up and running (DDoS protection).

## Formal Definition (if applicable)
**Public Key Cryptography:** A system that uses a pair of keys: a public key which may be disseminated widely, and a private key which is known only to the owner.

## Intuition
- **Encryption:** Putting your message in a safe.
- **Hashing:** Taking a fingerprint of the message to prove it hasn't changed.
- **Authentication:** Checking ID (Password, 2FA).
- **Authorization:** Checking if the ID holder is allowed to enter the room.

## Examples
- **Phishing:** Tricking users into revealing passwords via fake emails.
- **Ransomware:** Encrypting a victim's files and demanding payment for the key.
- **Zero-Day Exploit:** An attack that targets a vulnerability unknown to the software vendor.

## Common Misconceptions
- "Hackers are geniuses in hoodies." (Most attacks are automated scripts or social engineering.)
- "I have nothing to hide." (Attackers want your computing power for botnets or your identity for fraud, not just your secrets.)

## Related Concepts
- **Penetration Testing:** Hired hackers trying to break in to find weaknesses.
- **Social Engineering:** Manipulating people into breaking security procedures.
- **Blockchain:** Using cryptography to create a tamper-proof ledger.

## Applications
- **National Security:** Cyberwarfare.
- **Privacy:** Protecting personal data (GDPR).
- **Commerce:** Secure credit card transactions.

## Criticism / Limitations
Security often comes at the cost of usability (complex passwords, 2FA). The "human element" is always the weakest link.

## Further Reading
- Anderson, *Security Engineering*
- Schneier, *Applied Cryptography*
