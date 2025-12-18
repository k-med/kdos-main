---
title: "Distributed Systems"
slug: "distributed-systems"
type: "knowledge"
status: "seed"
date: 2025-12-18
domains: ["Computer Science"]
tags: ["cloud-computing", "cap-theorem", "consensus", "microservices", "scalability", "fault-tolerance"]
difficulty: "advanced"
reading_time: "7 mins"
summary: "A system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another."
---

## Overview
**Distributed Systems** are teams of computers working together. The Cloud is a distributed system.

## Core Idea
The core idea is **Scalability**. A single computer has limits. A thousand computers can do anything. But coordinating them is a nightmare.

## Formal Definition
A model in which components located on networked computers communicate and coordinate their actions by passing messages.

## Intuition
-   **The Orchestra:** One musician is easy to manage. An orchestra needs a conductor (or a very good protocol) to stay in sync.
-   **The Two Generals Problem:** Two generals on opposite hills need to attack at the same time. They can only send messengers through the enemy valley. How can they be 100% sure the other got the message? (Spoiler: They can't).

## Examples
-   **Google Search:** It's not one computer; it's data centers full of them.
-   **Blockchain:** A distributed ledger where everyone agrees on the truth without a central authority.
-   **BitTorrent:** Peer-to-peer file sharing.

## Common Misconceptions
-   **Misconception:** The network is reliable.
    -   **Correction:** The **Fallacies of Distributed Computing**: The network is reliable, latency is zero, bandwidth is infinite... all lies.
-   **Misconception:** It's just "more computers."
    -   **Correction:** It introduces new classes of bugs (Race Conditions, Partial Failures). "A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable." (Leslie Lamport).

## Related Concepts
-   **[Networking](file:///home/kdos/Anvil/kdos-main/content/knowledge/computer-science/networking.md):** The foundation.
-   **[Concurrency](file:///home/kdos/Anvil/kdos-main/content/knowledge/computer-science/concurrency.md):** Managing parallel tasks.

## Applications
-   **Cloud Computing:** AWS, Azure.
-   **Big Data:** Hadoop, Spark.

## Criticism and Limitations
-   **Complexity:** Debugging is hell.

## Further Reading
-   *Distributed Systems* by Tanenbaum and van Steen
