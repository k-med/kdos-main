---
title: "Survival Analysis"
slug: "survival-analysis"
type: "knowledge"
status: "seed"
date: 2025-12-18
domains: ["Statistics", "Medicine"]
tags: ["time-to-event", "censoring", "hazard-rate", "kaplan-meier", "life-expectancy", "churn"]
difficulty: "advanced"
reading_time: "7 mins"
summary: "A branch of statistics for analyzing the expected duration of time until one or more events happen, such as death in biological organisms and failure in mechanical systems."
---

## Overview
**Survival Analysis** asks: "How long until...?" How long until a patient dies? How long until a machine breaks? How long until a customer cancels their subscription?

## Core Idea
The core idea is **censoring**. In a study, some people die, but others are still alive when the study ends. We don't know when they *will* die, only that they survived *at least* this long. Standard regression can't handle this; Survival Analysis can.

## Formal Definition
-   **Survival Function $S(t)$:** Probability of surviving past time $t$.
-   **Hazard Function $h(t)$:** Instantaneous risk of dying at time $t$.

## Intuition
-   **The Bathtub Curve:** Risk of death is high at birth (infant mortality), low in middle age, and high again in old age.
-   **Churn:** In business, "death" is a customer cancelling.

## Examples
-   **Cancer Trials:** Does Chemo A extend life longer than Chemo B?
-   **Engineering:** Reliability testing. How long will this lightbulb last?
-   **Recidivism:** How long until an ex-convict commits another crime?

## Common Misconceptions
-   **Misconception:** "Median survival is 6 months" means I will die in 6 months.
    -   **Correction:** It means 50% of people die before 6 months, 50% after. The distribution often has a long tail (some live years).

## Related Concepts
-   **[Probability](file:///home/kdos/Anvil/kdos-main/content/knowledge/statistics/probability.md):** The foundation.
-   **[Epidemiology](file:///home/kdos/Anvil/kdos-main/content/knowledge/medicine/epidemiology.md):** Heavy user of these methods.

## Applications
-   **SaaS Business:** Calculating Customer Lifetime Value (LTV).
-   **Actuarial Science:** Insurance premiums.

## Criticism and Limitations
-   **Assumption of Independence:** Assumes censoring is random (people didn't drop out of the study *because* they were sick).

## Further Reading
-   *Survival Analysis: A Self-Learning Text* by Kleinbaum and Klein
