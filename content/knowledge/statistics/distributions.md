---
title: "Distributions"
slug: "distributions"
type: "knowledge"
status: "seed"
date: 2025-12-18
domains: ["Statistics"]
tags: ["normal-distribution", "poisson", "binomial", "power-law", "bell-curve", "outliers"]
difficulty: "intermediate"
reading_time: "7 mins"
summary: "A function that provides the probabilities of occurrence of different possible outcomes for an experiment."
---

## Overview
**Distributions** are the shapes of data. If you plot a million data points, they usually form a recognizable pattern. Knowing the shape tells you what to expect.

## Core Idea
The core idea is **predictability**. Randomness isn't shapeless. It follows laws.
-   **Normal Distribution (Bell Curve):** Height, IQ, Errors. Most are average; few are extreme.
-   **Power Law (Pareto):** Wealth, City Sizes, Twitter Followers. A few giants, many midgets. (The 80/20 rule).

## Formal Definition
A mathematical function that gives the probabilities of occurrence of different possible outcomes.
-   **PDF (Probability Density Function):** For continuous data (Height).
-   **PMF (Probability Mass Function):** For discrete data (Dice rolls).

## Intuition
-   **Normal:** Additive processes. (Height is sum of many genes + diet + environment).
-   **Log-Normal:** Multiplicative processes. (Stock prices).
-   **Poisson:** Rare events in a fixed time. (Phone calls per hour, meteor strikes).

## Examples
-   **The Long Tail:** In the internet age, niche products (the tail of the distribution) sell more than hits. (Amazon vs. Walmart).
-   **Six Sigma:** Manufacturing philosophy based on the Normal Distribution (keeping defects 6 standard deviations away from the mean).

## Common Misconceptions
-   **Misconception:** Everything is a Bell Curve.
    -   **Correction:** Financial markets are **Fat Tailed** (Power Law). Extreme crashes happen way more often than a Bell Curve predicts. This mistake caused the 2008 crisis.

## Related Concepts
-   **[Central Limit Theorem](file:///home/kdos/Anvil/kdos-main/content/knowledge/statistics/central-limit-theorem.md):** Why the Bell Curve is everywhere.
-   **[Outlier](file:///home/kdos/Anvil/kdos-main/content/knowledge/statistics/outlier.md):** A point that doesn't fit the distribution.

## Applications
-   **Insurance:** Pricing risk based on distributions.
-   **Epidemiology:** Modeling disease spread.

## Criticism and Limitations
-   **Model Risk:** Using the wrong distribution (e.g., using Normal for stock prices) is dangerous.

## Further Reading
-   *The Black Swan* by Nassim Nicholas Taleb
-   *Statistical Distributions* by Evans et al.
