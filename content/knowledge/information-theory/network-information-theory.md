---
title: "Network Information Theory"
slug: "network-information-theory"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains: ["Information Theory"]
tags:
  - "broadcast-channel"
  - "multiple-access-channel"
  - "interference"
  - "relay"
  - "capacity-region"
difficulty: "advanced"
reading_time: 7
summary: >
  Network information theory deals with information transmission over a network of communication channels. It extends Shannon's point-to-point theory to multi-user systems.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Shannon solved the problem for one sender and one receiver. But what if multiple people are talking at once? (Like a cocktail party or a Wi-Fi network).

## Core Idea
**Interference:** In a network, my signal is your noise. The goal is to manage this interference to maximize the total throughput.

## Formal Definition (if applicable)
**Multiple Access Channel (MAC):** Many senders, one receiver (e.g., Cell phones talking to a tower).
**Broadcast Channel (BC):** One sender, many receivers (e.g., TV tower, or a teacher talking to a class).

## Intuition
- **Time Division (TDMA):** Take turns speaking.
- **Frequency Division (FDMA):** Speak at different pitches.
- **Code Division (CDMA):** Speak different languages at the same time (the brain filters it out).

## Examples
- **The Internet:** A mesh of routers.
- **Sensor Networks:** Thousands of tiny sensors relaying data.
- **MIMO (Multiple Input Multiple Output):** Using multiple antennas to send multiple streams of data at once (Spatial Multiplexing).

## Common Misconceptions
- "Interference is always bad." (Network Coding shows that sometimes mixing signals is good. If A wants to send to B, and B to A, they can send A+B to a relay, saving a slot).

## Related Concepts
- **Relay Channel:** Using a helper to boost the signal.
- **Interference Alignment:** Cleverly aligning signals so they cancel out at the unintended receiver.

## Applications
- **5G/6G:** Designing the next generation of mobile networks.
- **Ad-hoc Networks:** Military or disaster relief comms without infrastructure.

## Criticism / Limitations
Most problems in network information theory are still open (unsolved). We don't know the capacity of even simple 3-node networks.

## Further Reading
- El Gamal & Kim, *Network Information Theory*
