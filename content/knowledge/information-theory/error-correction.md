---
title: "Error Correction"
slug: "error-correction"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Information Theory"
  - "Computer Science"
tags:
  - "parity-bit"
  - "hamming-code"
  - "reed-solomon"
  - "checksum"
  - "reliability"
  - "ecc-memory"
difficulty: "intermediate"
reading_time: 6
summary: >
  Error detection and correction or error control are techniques that enable reliable delivery of digital data over unreliable communication channels.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Scratched CDs still play. QR codes still work if you tear off a corner. How? Because they contain extra information (redundancy) that allows the computer to reconstruct the missing parts.

## Core Idea
**Parity Bit:** Adding a 1 or 0 to the end of a string to make the total number of 1s even.
- Data: 101 (Two 1s -> Even). Parity: 0. Send: 1010.
- Data: 111 (Three 1s -> Odd). Parity: 1. Send: 1111.
If you receive 1011 (Odd), you know there is an error. (But you don't know *where*).

## Formal Definition (if applicable)
**Hamming Distance:** The number of positions at which two strings differ.
- 10**1**1
- 10**0**1
Distance = 1. To correct $n$ errors, you need a code with distance $2n+1$.

## Intuition
Imagine a language where the only valid words are "AAAAA" and "BBBBB". If you hear "AAABA", you assume they meant "AAAAA". You corrected the error.

## Examples
- **Hamming Code:** Can detect 2 errors and correct 1.
- **Reed-Solomon Code:** Used in CDs, DVDs, and QR codes. Can correct bursts of errors (like a scratch).
- **Turbo Codes / LDPC:** Used in 4G/5G and Wi-Fi. They get very close to the Shannon Limit.

## Common Misconceptions
- "It fixes everything." (If there are too many errors, the correction will fail or, worse, "correct" it to the wrong value.)

## Related Concepts
- **Checksum (CRC):** Detects errors but doesn't fix them. (Used in Ethernet/IP).
- **RAID:** Using multiple hard drives to protect against failure.

## Applications
- **Space Probes:** Sending data from Mars requires powerful error correction.
- **ECC RAM:** Memory that fixes cosmic ray flips in servers.

## Criticism / Limitations
It adds overhead. You have to send more bits, which slows down the effective speed.

## Further Reading
- MacKay, *Information Theory, Inference, and Learning Algorithms*
