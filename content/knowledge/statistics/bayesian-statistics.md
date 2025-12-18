---
title: "Bayesian Statistics"
slug: "bayesian-statistics"
type: "knowledge"
status: "seed"
date: 2025-12-18
domains: ["Statistics", "Philosophy"]
tags: ["bayes-theorem", "priors", "posteriors", "updating", "subjectivity", "frequentist"]
difficulty: "advanced"
reading_time: "7 mins"
summary: "A theory in the field of statistics based on the Bayesian interpretation of probability where probability expresses a degree of belief in an event."
---

## Overview
**Bayesian Statistics** is a different philosophy of science. Unlike "Frequentist" statistics (which treats probability as long-run frequency), Bayesianism treats probability as **degree of belief**. It's about updating your opinion as you get new data.

## Core Idea
The core idea is **learning**. You start with a guess (**Prior**), look at the evidence (**Likelihood**), and calculate a new guess (**Posterior**).
$\text{Posterior} \propto \text{Likelihood} \times \text{Prior}$

## Formal Definition
Based on **Bayes' Theorem**:
$P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E)}$
-   $P(H|E)$: Probability of Hypothesis given Evidence.
-   $P(H)$: Prior probability (What you thought before).

## Intuition
-   **The Sunrise:** A Frequentist says "The sun has risen every day, so probability is high." A Bayesian says "I bet the sun rises. Oh, it rose? My bet is now stronger."
-   **The Doctor:** A patient tests positive for a rare disease.
    -   Frequentist: "The test is 99% accurate, so you're probably sick."
    -   Bayesian: "The disease is super rare (Prior), so even with a positive test, it's likely a false alarm."

## Examples
-   **Spam Filters:** "This email has the word 'Viagra'. My prior says 'Viagra' usually means spam. I update my belief: 99% chance it's spam."
-   **Search for MH370:** Searchers used Bayesian methods to update the search area as they found debris.

## Common Misconceptions
-   **Misconception:** It's subjective and unscientific.
    -   **Correction:** Priors *can* be subjective, but as you get more data, the Prior matters less and the truth wins out.
-   **Misconception:** It's too hard.
    -   **Correction:** It used to be computationally impossible, but modern computers (MCMC) make it easy.

## Related Concepts
-   **[Frequentist Statistics](file:///home/kdos/Anvil/kdos-main/content/knowledge/statistics/inferential-statistics.md):** The rival school (p-values, confidence intervals).
-   **[Epistemology](file:///home/kdos/Anvil/kdos-main/content/knowledge/philosophy/epistemology.md):** Bayesianism is a formal theory of knowledge.

## Applications
-   **AI:** Robots use Bayesian logic to navigate (SLAM).
-   **Codebreaking:** Alan Turing used Bayesian logic to crack Enigma.

## Criticism and Limitations
-   **The Prior:** Where does it come from? If you start with a crazy Prior, you might get a crazy result.

## Further Reading
-   *The Theory That Would Not Die* by Sharon Bertsch McGrayne
-   *Doing Bayesian Data Analysis* by John Kruschke
