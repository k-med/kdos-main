---
title: "Central Limit Theorem"
slug: "central-limit-theorem"
type: "knowledge"
status: "draft"
date_created: "2025-12-17"
last_updated: "2025-12-17"
domains:
  - "Statistics"
  - "Probability Theory"
tags:
  - "sampling-distribution"
  - "normal-distribution"
  - "statistical-inference"
  - "large-numbers"
difficulty: "intermediate"
reading_time: 7
summary: >
  The Central Limit Theorem states that the sampling distribution of the sample mean approximates a normal distribution as the sample size becomes larger, regardless of the population's distribution.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
The Central Limit Theorem (CLT) is a fundamental theorem in probability theory and statistics. It explains why the normal distribution is so common in nature and why statistical inference is possible even when the population distribution is unknown.

## Core Idea
If you take sufficiently large random samples from a population with *any* shape of distribution (even a weird or skewed one) and calculate the mean for each sample, the distribution of those sample means will form a bell curve (normal distribution).

## Formal Definition (if applicable)
Let $X_1, X_2, ..., X_n$ be a random sample of size $n$ from a population with mean $\mu$ and finite variance $\sigma^2$. As $n \to \infty$, the distribution of the sample mean $\bar{X}$ approaches a normal distribution with mean $\mu$ and variance $\frac{\sigma^2}{n}$.

## Intuition
Imagine rolling a single die. The distribution is flat (uniform)—every number 1-6 is equally likely. But if you roll 10 dice and average them, getting a 1 or a 6 average is extremely rare. Most averages will cluster around 3.5. The more dice you roll, the more "bell-shaped" the distribution of averages becomes.

## Examples
- **Polling**: Even if political opinions are polarized (bimodal), the average result of many polls will follow a normal distribution, allowing for margin of error calculations.
- **Quality Control**: The average weight of batches of products will be normally distributed, even if individual product weights vary erratically.

## Common Misconceptions
- **"Data becomes normal"**: The CLT does *not* say the original data becomes normal. It says the *distribution of sample means* becomes normal.
- **"Sample size 30"**: While $n=30$ is a common rule of thumb, the required sample size depends on how skewed the original population is.

## Related Concepts
- [Normal Distribution](/knowledge/statistics/normal-distribution/)
- Law of Large Numbers
- Sampling Distribution
- Standard Error

## Applications
The CLT is the foundation of hypothesis testing and confidence intervals. It allows statisticians to use normal probability models to make inferences about population means without knowing the population's distribution.

## Criticism / Limitations
The CLT relies on samples being independent and identically distributed (i.i.d.). It also assumes finite variance; it does not apply to distributions with infinite variance (e.g., Cauchy distribution).

## Further Reading
- "The Central Limit Theorem" by various authors in probability theory.
- Visualizations of CLT (e.g., Seeing Theory).
