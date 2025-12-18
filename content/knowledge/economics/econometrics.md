---
title: "Econometrics"
slug: "econometrics"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains: ["Economics", "Statistics"]
tags:
  - "regression-analysis"
  - "causal-inference"
  - "time-series"
  - "panel-data"
  - "instrumental-variables"
  - "identification"
difficulty: "advanced"
reading_time: 7
summary: >
  Econometrics is the application of statistical methods to economic data in order to give empirical content to economic relationships. More precisely, it is "the quantitative analysis of actual economic phenomena based on the concurrent development of theory and observation, related by appropriate methods of inference".
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Theory says "raising prices reduces demand." Econometrics asks "By how much?" It turns economic stories into numbers using data and statistics.

## Core Idea
**Causal Inference:** Correlation is not causation. Econometrics is obsessed with finding *causality*. Did the minimum wage cause unemployment, or did unemployment cause the minimum wage not to be raised?

## Formal Definition (if applicable)
**Regression Analysis:** A statistical process for estimating the relationships among variables. $Y = \beta_0 + \beta_1 X + \epsilon$

## Intuition
It's like being a detective. You have a crime scene (data) and you want to know who did it (cause). But there are many suspects (confounding variables). You use tools to isolate the true culprit.

## Examples
- **Randomized Controlled Trials (RCTs):** The gold standard. Flipping a coin to decide who gets the treatment.
- **Natural Experiments:** Using random events (like a lottery or a border change) to study effects.
- **Difference-in-Differences:** Comparing a treatment group to a control group before and after a policy change.

## Common Misconceptions
- "Data speaks for itself." (Data is dumb. You need a model to interpret it.)
- "P-value < 0.05 means it's true." (It just means it's unlikely to be random noise. It doesn't prove the hypothesis.)

## Related Concepts
- **Endogeneity:** When the independent variable is correlated with the error term (bad).
- **Instrumental Variables:** A tool to fix endogeneity.
- **Time Series:** Analyzing data over time (e.g., stock prices).

## Applications
- **Forecasting:** Predicting GDP growth.
- **Policy Evaluation:** Did the tax cut work?
- **Marketing:** Measuring the ROI of an ad campaign.

## Criticism / Limitations
"If you torture the data long enough, it will confess." (P-hacking). Models rely on assumptions that may not hold.

## Further Reading
- Angrist & Pischke, *Mostly Harmless Econometrics*
- Wooldridge, *Introductory Econometrics*
