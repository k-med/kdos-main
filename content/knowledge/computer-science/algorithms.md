---
title: "Algorithms"
slug: "algorithms"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Computer Science"
  - "Mathematics"
tags:
  - "sorting"
  - "searching"
  - "complexity"
  - "big-o-notation"
  - "recursion"
  - "dynamic-programming"
difficulty: "intermediate"
reading_time: 6
summary: >
  An algorithm is a finite sequence of well-defined, computer-implementable instructions, typically to solve a class of problems or to perform a computation.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Algorithms are the recipes of computing. They tell the computer exactly what steps to take to transform input into output. Efficiency is key—a good algorithm can solve a problem in seconds that a bad one couldn't solve in a million years.

## Core Idea
**Big O Notation:** A mathematical notation used to describe the limiting behavior of a function when the argument tends towards a particular value or infinity. It classifies algorithms according to how their run time or space requirements grow as the input size grows.

## Formal Definition (if applicable)
**Algorithm:** A procedure for solving a mathematical problem in a finite number of steps that frequently involves recursive operations.

## Intuition
Sorting a deck of cards:
- **Bubble Sort:** Compare adjacent cards and swap if wrong. Repeat until sorted. (Slow: $O(n^2)$)
- **Merge Sort:** Split the deck in half, sort each half, then merge them. (Fast: $O(n \log n)$)

## Examples
- **Dijkstra's Algorithm:** Finding the shortest path between nodes in a graph (like GPS finding a route).
- **PageRank:** Google's algorithm for ranking web pages.
- **RSA:** An encryption algorithm used for secure data transmission.

## Common Misconceptions
- "Algorithms are objective." (They reflect the biases of their creators and the data they are trained on.)
- "Complex is better." (Simple algorithms are often more robust and easier to debug.)

## Related Concepts
- **Recursion:** A function calling itself.
- **Heuristic:** A technique designed for solving a problem more quickly when classic methods are too slow (approximate solution).
- **NP-Completeness:** A class of problems for which no efficient solution is known.

## Applications
- **Search Engines:** Retrieving relevant results.
- **Recommendation Systems:** Netflix suggesting movies.
- **Financial Trading:** High-frequency trading algorithms.

## Criticism / Limitations
"Black Box" algorithms (especially in AI) can make decisions that are difficult to explain or justify, raising ethical concerns.

## Further Reading
- Cormen et al., *Introduction to Algorithms* (CLRS)
- Knuth, *The Art of Computer Programming*
