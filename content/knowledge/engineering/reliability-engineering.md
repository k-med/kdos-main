---
title: "Reliability Engineering"
slug: "reliability-engineering"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Engineering"
  - "Statistics"
tags:
  - "failure"
  - "probability"
  - "maintenance"
  - "systems"
  - "quality"
  - "risk"
difficulty: "advanced"
reading_time: 6
summary: >
  Reliability engineering is a sub-discipline of systems engineering that emphasizes the ability of equipment to function without failure. Reliability describes the ability of a system or component to function under stated conditions for a specified period of time.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Things break. Reliability Engineers try to predict *when* they will break and *how* to prevent it. They are the pessimists of the engineering world. They assume everything will fail, and they design systems that can survive failure.

## Core Idea
The core idea is **Probability of Failure**. You can't make a machine perfect (0% failure). But you can make it reliable enough (99.999% success).

## Formal Definition
The discipline that emphasizes the ability of equipment to function without failure for a specified period of time.
Key Metric: **MTBF (Mean Time Between Failures)**.

## Intuition
-   **The Bathtub Curve:** Products fail early (Infant Mortality), then they work for a long time (Useful Life), then they wear out (End of Life). This looks like a bathtub.
-   **Redundancy:** Wearing a belt AND suspenders. If the belt breaks, the suspenders hold your pants up. Planes have 3 computers. If one fails, the others take over.

## Examples
-   **Aircraft Engines:** They are incredibly reliable. You are more likely to win the lottery than be in a plane crash caused by engine failure. This is due to rigorous reliability engineering.
-   **Server Farms:** Google expects hard drives to fail every day. They design the software so that when a drive dies, no data is lost.

## Common Misconceptions
-   **Reliability = Quality:** A car can be high quality (nice leather, smooth ride) but low reliability (breaks down every month).
-   **Testing finds all bugs:** You can't test for 10 years to see if a product lasts 10 years. You use **Accelerated Life Testing** (running it hot and fast) to simulate aging.

## Related Concepts
-   **FMEA (Failure Modes and Effects Analysis):** Brainstorming every possible way a thing can break and fixing it before it happens.
-   **Maintenance:**
    -   **Reactive:** Fix it when it breaks.
    -   **Preventive:** Change the oil every 3,000 miles.
    -   **Predictive:** Sensors tell you the bearing is vibrating and *will* break next week.

## Applications
-   **Nuclear Power:** Where failure is not an option.

## Criticism / Limitations
-   **Cost:** Redundancy is expensive. You don't put 3 engines in a Honda Civic.

## Further Reading
-   O'Connor, Patrick. *Practical Reliability Engineering*.
