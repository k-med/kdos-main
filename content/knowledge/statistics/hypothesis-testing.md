---
title: "Hypothesis Testing"
slug: "hypothesis-testing"
type: "knowledge"
status: "draft"
date_created: "2025-12-17"
last_updated: "2025-12-17"
domains:
  - "Statistics"
tags:
  - "statistical-inference"
  - "null-hypothesis"
  - "significance-testing"
  - "decision-making"
difficulty: "intermediate"
reading_time: 6
summary: >
  Hypothesis testing is a structured method for making decisions using data, involving the comparison of a null hypothesis against an alternative hypothesis.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Hypothesis testing is the backbone of scientific research and data-driven decision making. It provides a formal framework to determine whether observed patterns in data are likely real or just random noise.

## Core Idea
The core idea is to assume nothing interesting is happening (the Null Hypothesis) and then see if the data is so unusual that this assumption is likely false. It's like a criminal trial: the defendant (Null Hypothesis) is presumed innocent until proven guilty (rejected) by sufficient evidence (data).

## Formal Definition (if applicable)
A statistical test that uses sample data to decide between two competing hypotheses:

$$ H_0: \text{Null Hypothesis (Status Quo)} $$
$$ H_1: \text{Alternative Hypothesis (Claim)} $$

## Intuition
If you flip a coin 100 times and get 52 heads, you wouldn't suspect it's rigged. If you get 95 heads, you would. Hypothesis testing quantifies exactly where the line is between "plausible luck" and "suspiciously biased."

## Examples
- **A/B Testing**: Testing if a new website design ($H_1$) leads to more clicks than the old one ($H_0$).
- **Drug Trials**: Testing if a new medicine ($H_1$) cures more patients than a placebo ($H_0$).

## Common Misconceptions
- **"Proving" the Null**: You never "accept" or "prove" the null hypothesis; you only "fail to reject" it. Absence of evidence is not evidence of absence.
- **p=0.05 is magic**: The 0.05 threshold is arbitrary convention, not a law of nature.

## Related Concepts
- [P-value](/knowledge/statistics/p-value/)
- [Type I and Type II Errors](/knowledge/statistics/type-i-and-type-ii-errors/)
- [Confidence Intervals](/knowledge/statistics/confidence-intervals/)
- Statistical Significance

## Applications
Used everywhere from clinical trials and psychology experiments to manufacturing quality assurance and marketing analytics.

## Criticism / Limitations
Frequentist hypothesis testing is often criticized for its reliance on arbitrary thresholds (p-hacking) and for not telling us the probability that the hypothesis is actually true (which Bayesian methods do).

## Further Reading
- "The Lady Tasting Tea" by David Salsburg
- ASA Statement on p-Values
