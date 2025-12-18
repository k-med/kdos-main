---
title: "Networking"
slug: "networking"
type: "knowledge"
status: "seed"
date: 2025-12-18
domains: ["Computer Science"]
tags: ["internet", "tcp-ip", "http", "dns", "packets", "routing"]
difficulty: "intermediate"
reading_time: "7 mins"
summary: "The practice of transporting and exchanging data between nodes over a shared medium in an information system."
---

## Overview
**Networking** is how computers talk to each other. It's the plumbing of the digital age. Without it, a computer is just a fancy calculator.

## Core Idea
The core idea is **Protocols**. Computers need agreed-upon rules (languages) to understand each other. "I speak TCP, do you?"

## Formal Definition
A computer network is a set of computers sharing resources located on or provided by network nodes.

## Intuition
-   **The Postal Service:**
    -   *Data:* The letter.
    -   *Packet:* The envelope.
    -   *IP Address:* The house address.
    -   *Router:* The post office sorting facility.
    -   *TCP:* The certified mail receipt (guarantees delivery).
    -   *UDP:* Throwing the letter on the porch (fast, but might get lost).

## Examples
-   **The Internet:** The network of networks.
-   **DNS (Domain Name System):** The phonebook of the internet. It turns "google.com" into "142.250.190.46".
-   **HTTP:** The protocol of the web. (GET, POST).

## Common Misconceptions
-   **Misconception:** The Web is the Internet.
    -   **Correction:** The Internet is the infrastructure (roads). The Web is just one service on top of it (traffic). Email is another.
-   **Misconception:** WiFi is the Internet.
    -   **Correction:** WiFi is just the wireless link to your router.

## Related Concepts
-   **[Distributed Systems](file:///home/kdos/Anvil/kdos-main/content/knowledge/computer-science/distributed-systems.md):** Networks enable distributed systems.
-   **[Cryptography](file:///home/kdos/Anvil/kdos-main/content/knowledge/computer-science/cryptography.md):** Securing the network.

## Applications
-   **Streaming:** Netflix uses UDP (or similar) because if you drop a pixel, it doesn't matter, but speed does.
-   **Banking:** Uses TCP because every penny must arrive.

## Criticism and Limitations
-   **Latency:** The speed of light is a hard limit. You can't ping Australia instantly.

## Further Reading
-   *Computer Networking: A Top-Down Approach* by Kurose and Ross
