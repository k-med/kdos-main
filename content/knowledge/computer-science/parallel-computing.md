---
title: "Parallel Computing"
slug: "parallel-computing"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Computer Science"
  - "Systems"
tags:
  - "concurrency"
  - "threads"
  - "multi-core"
  - "gpu"
  - "supercomputing"
  - "performance"
difficulty: "advanced"
reading_time: 6
summary: >
  Parallel computing is a type of computation in which many calculations or the execution of processes are carried out simultaneously. Large problems can often be divided into smaller ones, which can then be solved at the same time.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
For 40 years, computers got faster by making the CPU clock speed higher (3GHz, 4GHz). Then we hit a wall (physics/heat). We couldn't make them faster, so we made them *wider*. We added more cores. Parallel computing is the art of doing many things at once.

## Core Idea
The core idea is **Divide and Conquer**. Breaking a big problem into 1,000 small chunks and giving each chunk to a different worker.

## Formal Definition
A type of computation in which many calculations or the execution of processes are carried out simultaneously.
**Amdahl's Law:** The theoretical limit of speedup. If 50% of your program *must* be run sequentially, you can never make it more than 2x faster, no matter how many processors you add.

## Intuition
-   **Serial Computing:** One guy painting a fence.
-   **Parallel Computing:** Ten guys painting a fence. It's 10x faster.
-   **The Catch:** They have to coordinate. If two guys try to paint the same spot, they bump heads (Race Condition). If one guy waits for another, they waste time (Deadlock).

## Examples
-   **Supercomputers:** The Frontier supercomputer has 8 million cores. It is used to simulate nuclear explosions and climate change.
-   **GPUs (Graphics Processing Units):** A CPU has 8 smart cores. A GPU has 4,000 dumb cores. They are perfect for graphics (painting pixels) and AI (matrix multiplication), which are "embarrassingly parallel" tasks.
-   **Web Servers:** Handling 10,000 users at once. Each user gets their own thread.

## Common Misconceptions
-   **More cores = Faster:** Only if the software is written to use them. Most games still rely heavily on a single core.
-   **Concurrency vs. Parallelism:**
    -   **Concurrency:** Dealing with many things at once (juggling).
    -   **Parallelism:** Doing many things at once (multiple jugglers).

## Related Concepts
-   **Race Condition:** A bug where the output depends on the timing of uncontrollable events. (e.g., Two threads try to withdraw money from a bank account at the exact same microsecond).
-   **MapReduce:** Google's algorithm for processing the whole internet. Map (split the work), Reduce (combine the results).

## Applications
-   **Crypto Mining:** Using GPUs to guess random numbers in parallel.
-   **Weather Forecasting:** You need the answer before the weather actually happens. Only parallel computing is fast enough.

## Criticism / Limitations
-   **Complexity:** Writing parallel code is incredibly hard. Debugging it is a nightmare because bugs are non-deterministic (they disappear when you look for them—Heisenbugs).

## Further Reading
-   Herlihy, Maurice. *The Art of Multiprocessor Programming*.
-   Mattson, Timothy. *Patterns for Parallel Programming*.
