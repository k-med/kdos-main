---
title: "Computer Networks"
slug: "computer-networks"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains: ["Computer Science", "Engineering"]
tags:
  - "tcp-ip"
  - "osi-model"
  - "routing"
  - "packets"
  - "protocols"
  - "latency"
  - "bandwidth"
difficulty: "intermediate"
reading_time: 6
summary: >
  A computer network is a set of computers sharing resources located on or provided by network nodes. The computers use common communication protocols over digital interconnections to communicate with each other.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Networks connect the world. From the WiFi in your house to the undersea cables linking continents, networking is the plumbing of the digital age.

## Core Idea
**Packet Switching:** Instead of a dedicated line (like old phones), data is chopped into small chunks ("packets") that take different routes to the destination and are reassembled there. This is efficient and robust.

## Formal Definition (if applicable)
**OSI Model (Open Systems Interconnection):** A conceptual model that characterizes and standardizes the communication functions of a telecommunication or computing system without regard to its underlying internal structure and technology. It has 7 layers (Physical, Data Link, Network, Transport, Session, Presentation, Application).

## Intuition
Sending an email is like mailing a letter.
1.  **Application:** You write the letter.
2.  **Transport:** You put it in an envelope (TCP ensures it arrives).
3.  **Network:** The post office decides the route (IP address).
4.  **Physical:** The truck carries it.

## Examples
- **The Internet:** A network of networks.
- **LAN (Local Area Network):** Your home WiFi.
- **VPN (Virtual Private Network):** A secure tunnel through the public internet.

## Common Misconceptions
- "The Web and the Internet are the same." (The Internet is the infrastructure; the Web is a service running on top of it, like email or Skype.)
- "Bandwidth = Speed." (Bandwidth is width of the pipe; Latency is the speed of the water.)

## Related Concepts
- **DNS (Domain Name System):** The phonebook of the internet (translates google.com to 142.250.190.46).
- **HTTP/HTTPS:** The protocol for transferring web pages.
- **Firewall:** A security device that monitors network traffic.

## Applications
- **Streaming:** Netflix uses adaptive bitrate streaming to handle network fluctuations.
- **Gaming:** Low latency (ping) is critical.
- **IoT:** Connecting billions of devices.

## Criticism / Limitations
The internet was designed for trust, not security. Retrofitting security (like HTTPS and DNSSEC) is an ongoing battle.

## Further Reading
- Kurose & Ross, *Computer Networking: A Top-Down Approach*
- Tanenbaum, *Computer Networks*
