---
title: "Bayesian Epistemology"
slug: "bayesian-epistemology"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains: ["Epistemology", "Statistics"]
tags:
  - "degrees-of-belief"
  - "updating"
  - "priors"
  - "evidence"
  - "probability"
  - "dutch-book-arguments"
difficulty: "advanced"
reading_time: 7
summary: >
  Bayesian epistemology is a formal approach to various topics in epistemology that has its roots in Thomas Bayes' work on probability. It replaces the traditional binary notion of belief with degrees of belief.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Belief isn't black and white. It's shades of grey. Bayesianism provides a mathematical framework for updating your confidence in a belief as you get new evidence.

## Core Idea
**Bayes' Theorem:**
$$ P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E)} $$
- $P(H|E)$: Posterior (Probability of Hypothesis given Evidence).
- $P(H)$: Prior (Probability of Hypothesis before Evidence).
- $P(E|H)$: Likelihood (Probability of Evidence if Hypothesis is true).

## Formal Definition (if applicable)
**Conditionalization:** The rule that says your new belief should equal your old belief conditional on the new evidence.

## Intuition
You hear a bark.
- **Hypothesis:** It's a dog.
- **Prior:** High (dogs are common).
- **Evidence:** Bark.
- **Update:** Confidence goes up.
You see it's a cat.
- **Update:** Confidence crashes (unless it's a very weird cat).

## Examples
- **Science:** Testing theories. A successful prediction increases the probability of the theory.
- **Law:** Updating the probability of guilt as clues are found.
- **AI:** Spam filters (Bayesian classifiers).

## Common Misconceptions
- "Priors are arbitrary." (They are subjective, but they should converge as evidence accumulates.)
- "It's too hard to calculate." (We do it intuitively, even if we don't do the math.)

## Related Concepts
- **Dutch Book Argument:** If your beliefs don't follow the laws of probability, someone can make a bet against you that you are guaranteed to lose. Therefore, rationality requires obeying probability.
- **Cromwell's Rule:** Never assign probability 0 or 1 to anything (except logical truths), or you can never change your mind.

## Applications
- **Decision Theory:** Expected Utility = Probability $\times$ Value.
- **Philosophy of Science:** Explaining confirmation and falsification.

## Criticism / Limitations
Problem of the Priors: Where do we start? If we start with crazy priors, we might never reach the truth.

## Further Reading
- Bovens & Hartmann, *Bayesian Epistemology*
- Talbott, *Bayesian Epistemology* (SEP)
