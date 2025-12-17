---
title: "P-value"
slug: "p-value"
type: "knowledge"
status: "draft"
date_created: "2025-12-17"
last_updated: "2025-12-17"
domains:
  - "Statistics"
tags:
  - "statistical-significance"
  - "hypothesis-testing"
  - "probability"
  - "inference"
difficulty: "intermediate"
reading_time: 5
summary: >
  The p-value is the probability of observing results at least as extreme as those measured, assuming the null hypothesis is true.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
The p-value is one of the most widely used—and misunderstood—concepts in statistics. It serves as a measure of evidence against a null hypothesis.

## Core Idea
The p-value answers the question: "If the world were boring (null hypothesis is true), how surprising is my data?" A small p-value means the data is very surprising, suggesting the world might not be boring after all.

## Formal Definition (if applicable)
$$ p = P(\text{Data} \geq \text{Observed} | H_0) $$

The probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct.

## Intuition
Imagine you claim to be a basketball pro. I assume you are average ($H_0$).
- If you make 1 shot, I'm not impressed (High p-value).
- If you make 10 shots in a row, that would be extremely rare for an average player (Low p-value). I reject my assumption that you are average.

## Examples
- **p = 0.03**: There is a 3% chance of seeing this data if the null hypothesis were true. Usually considered statistically significant (since < 0.05).
- **p = 0.20**: There is a 20% chance. This is common random noise. We fail to reject the null.

## Common Misconceptions
- **"Probability the hypothesis is true"**: The p-value is NOT the probability that $H_0$ is true or false. It is a probability about the *data*, not the theory.
- **"Measure of effect size"**: A tiny p-value doesn't mean the effect is important; it just means the sample size was large enough to detect it.

## Related Concepts
- [Hypothesis Testing](/knowledge/statistics/hypothesis-testing/)
- Significance Level ($\alpha$)
- [Type I and Type II Errors](/knowledge/statistics/type-i-and-type-ii-errors/)

## Applications
Used to determine statistical significance in research papers, clinical trials, and business experiments.

## Criticism / Limitations
Over-reliance on p-values has led to the "replication crisis" in science. Researchers may "p-hack" (manipulate data) to get p < 0.05.

## Further Reading
- "The Cult of Statistical Significance" by Ziliak and McCloskey
- American Statistical Association (ASA) statement on p-values
