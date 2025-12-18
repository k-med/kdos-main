---
title: "Channel Capacity"
slug: "channel-capacity"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Information Theory"
  - "Telecommunications"
tags:
  - "shannon-limit"
  - "bandwidth"
  - "noise"
  - "signal-to-noise-ratio"
  - "error-free-communication"
difficulty: "advanced"
reading_time: 7
summary: >
  Channel capacity is the tightest upper bound on the rate of information that can be reliably transmitted over a communication channel.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
How fast can you talk over a noisy phone line? Claude Shannon proved there is a speed limit. Below that limit, you can communicate perfectly (with error correction). Above it, you can't.

## Core Idea
**Shannon-Hartley Theorem:**
$$ C = B \log_2 (1 + \frac{S}{N}) $$
- $C$: Capacity (bits per second).
- $B$: Bandwidth (Hz).
- $S/N$: Signal-to-Noise Ratio.

## Formal Definition (if applicable)
**Noisy Channel Coding Theorem:** It is possible to transmit information with arbitrarily low error probability at any rate $R < C$.

## Intuition
Think of a pipe.
- **Bandwidth ($B$):** The width of the pipe.
- **Signal ($S$):** The pressure of the water.
- **Noise ($N$):** Leaks or turbulence.
To get more water (info) through, you can widen the pipe (more bandwidth) or pump harder (more signal power).

## Examples
- **Wi-Fi:** Gets slower when you are far away (Signal drops) or when the microwave is on (Noise increases).
- **5G:** Uses massive bandwidth (mmWave) to achieve high capacity.
- **Deep Space Network:** Communicating with Voyager 1 requires huge antennas (High S) and very slow data rates (Low B) because the signal is so weak.

## Common Misconceptions
- "We can always compress more." (No, entropy is the hard limit for compression, and capacity is the hard limit for transmission.)
- "Error-free means no errors happen." (Errors happen, but we can detect and fix them so the *decoded* message is error-free.)

## Related Concepts
- **Bit Error Rate (BER):** The percentage of bits that get flipped.
- **Modulation:** How we encode bits onto waves (AM, FM, QAM).

## Applications
- **Internet:** Every modem, router, and fiber optic cable is designed around this limit.
- **Storage:** Hard drives use channel coding to read data correctly even if the disk is scratched.

## Criticism / Limitations
The theorem tells you *that* a code exists, but not *how* to find it. It took 50 years (Turbo Codes, LDPC) to get close to the limit.

## Further Reading
- Cover & Thomas, *Elements of Information Theory*
