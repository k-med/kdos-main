---
title: "Source Coding Theorem"
slug: "source-coding-theorem"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains: ["Information Theory", "Mathematics"]
tags:
  - "shannon"
  - "compression"
  - "entropy"
  - "limits"
  - "asymptotic-equipartition"
difficulty: "advanced"
reading_time: 7
summary: >
  Shannon's source coding theorem (or the noiseless coding theorem) establishes the limits to possible data compression, and the operational meaning of the Shannon entropy.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
This is the theorem that started it all. It says: "You can compress data up to its entropy, but no further."

## Core Idea
**Asymptotic Equipartition Property (AEP):** For a long sequence of random variables, the outcome will almost certainly belong to a "Typical Set." We only need to assign codes to the Typical Set. The "Atypical" outcomes are so rare we can ignore them (or use long codes).

## Formal Definition (if applicable)
$$ L \ge H(X) $$
The expected length $L$ of a code cannot be less than the entropy $H(X)$.

## Intuition
If you are packing a suitcase:
- **Entropy:** The volume of your clothes.
- **Compression:** Vacuum packing.
- **Theorem:** You can vacuum pack the air out, but you can't make the clothes disappear. There is a minimum size.

## Examples
- **English Text:** Entropy is ~1.5 bits per letter (if you consider context). Standard ASCII uses 8 bits. This means English can be compressed by ~80%.
- **Coin Flips:** If the coin is fair (H=1), you can't compress it. If it's biased (H<1), you can.

## Common Misconceptions
- "I found a compression algorithm that compresses *every* file." (Impossible. Counting argument: There are fewer short files than long files. You can't map many long files to few short files uniquely).

## Related Concepts
- **Rate-Distortion Theory:** The limit for *lossy* compression. (How much quality do you lose for a given size?).
- **Kraft's Inequality:** A condition for a code to be uniquely decodable.

## Applications
- **File Formats:** ZIP, GZIP, 7z.
- **Communication:** Optimizing bandwidth usage.

## Criticism / Limitations
It only applies to the limit of infinite block lengths. For short messages, you might not reach the entropy limit.

## Further Reading
- Shannon, *A Mathematical Theory of Communication*
