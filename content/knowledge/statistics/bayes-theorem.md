---
title: "Bayes' Theorem"
slug: "bayes-theorem"
type: "knowledge"
status: "draft"
date_created: "2025-12-17"
last_updated: "2025-12-17"
domains:
  - "Statistics"
tags:
  - "conditional-probability"
  - "bayesian-inference"
  - "priors"
  - "posteriors"
difficulty: "advanced"
reading_time: 8
summary: >
  Bayes' Theorem provides a mathematical framework for updating the probability of a hypothesis as more evidence or information becomes available.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Bayes' Theorem is a way of thinking about probability not as a frequency, but as a degree of belief. It tells us how to update our beliefs when we see new data.

## Core Idea
Posterior Probability $\propto$ Likelihood $\times$ Prior Probability.
Your new belief (Posterior) depends on two things:
1. How likely the evidence is if your belief is true (Likelihood).
2. How likely you thought the belief was true before seeing the evidence (Prior).

## Formal Definition (if applicable)
$$ P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)} $$

Where:
- $P(A|B)$ is the probability of hypothesis A given data B (Posterior).
- $P(B|A)$ is the probability of data B given hypothesis A (Likelihood).
- $P(A)$ is the probability of hypothesis A being true beforehand (Prior).
- $P(B)$ is the probability of the data occurring under any hypothesis (Evidence).

## Intuition
You see a light in the sky (Data). Is it a UFO (Hypothesis)?
- **Likelihood**: If it were a UFO, it would definitely look like a light. High.
- **Prior**: UFOs are extremely rare. Very Low.
- **Posterior**: Even though the likelihood is high, the low prior drags the final probability down. It's probably just a plane.

## Examples
- **Medical Screening**: If a test is 99% accurate, and you test positive for a rare disease (1 in 10,000), you are still likely healthy. The base rate (prior) of the disease is so low that false positives outweigh true positives.

## Common Misconceptions
- **Base Rate Neglect**: Ignoring the prior probability (how common something is generally) and focusing only on the specific evidence.
- **Confusing $P(A|B)$ with $P(B|A)$**: The probability of a positive test given you have cancer is NOT the same as the probability you have cancer given a positive test.

## Related Concepts
- Conditional Probability
- Bayesian Inference
- Base Rate Fallacy
- Naive Bayes Classifier

## Applications
Used in machine learning (spam filters), medical diagnosis, search and rescue operations, and code breaking (Enigma).

## Criticism / Limitations
Bayesian methods require a Prior, which can be subjective. Critics argue this introduces bias, whereas Frequentist methods rely only on the data at hand.

## Further Reading
- "The Theory That Would Not Die" by Sharon McGrayne
- "Thinking, Fast and Slow" by Daniel Kahneman (on Base Rate Neglect)
