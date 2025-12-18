---
title: "Confidence Intervals"
slug: "confidence-intervals"
type: "knowledge"
status: "draft"
date_created: "2025-12-17"
last_updated: "2025-12-17"
domains: ["Statistics"]
tags:
  - "estimation"
  - "statistical-inference"
  - "uncertainty"
  - "interval-estimation"
difficulty: "intermediate"
reading_time: 6
summary: >
  A confidence interval provides a range of values that is likely to contain a population parameter, quantifying the uncertainty of an estimate.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Point estimates (like a sample average) are rarely exactly right. Confidence intervals (CIs) acknowledge this uncertainty by providing a range—an interval—that we are "confident" covers the true value.

## Core Idea
Instead of saying "The average height is 175cm," we say "We are 95% confident the true average height is between 173cm and 177cm." It turns a single guess into a net that catches the truth with a specified probability.

## Formal Definition (if applicable)
A $100(1-\alpha)\%$ confidence interval is an interval computed from sample data such that, if the sampling were repeated many times, $100(1-\alpha)\%$ of the generated intervals would contain the true population parameter.

$$ P(L \leq \theta \leq U) = 1 - \alpha $$

## Intuition
Imagine throwing a ring at a stick in the ground (the true parameter). You can't see the stick perfectly. A confidence interval is the size of the ring. A wider ring (higher confidence) is more likely to catch the stick, but gives you less precision about where the stick is.

## Examples
- **Election Polling**: "Candidate A is polling at 48% with a margin of error of +/- 3%." This is a confidence interval of [45%, 51%].
- **Product Testing**: "The average battery life is 10 hours +/- 0.5 hours."

## Common Misconceptions
- **"95% chance the true value is in *this* interval"**: This is technically incorrect in frequentist statistics. The true value is fixed; the *interval* is random. Once calculated, the interval either contains the value or it doesn't. The "95%" refers to the reliability of the method, not the specific interval.
- **"We capture 95% of the data"**: No, CIs are about the *mean* (parameter), not the individual data points.

## Related Concepts
- [Standard Deviation](/knowledge/statistics/standard-deviation/)
- Standard Error
- [Central Limit Theorem](/knowledge/statistics/central-limit-theorem/)
- Margin of Error

## Applications
Used in reporting scientific results to convey precision. A narrow CI implies a precise estimate; a wide CI implies high uncertainty.

## Criticism / Limitations
Often misinterpreted by the public and even researchers. Bayesian credible intervals are an alternative that actually allows for probability statements about the parameter.

## Further Reading
- "Statistical Intervals" by Hahn and Meeker
- Explanations of Frequentist vs Bayesian intervals
