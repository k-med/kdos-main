---
title: "Correlation vs Causation"
slug: "correlation-vs-causation"
type: "knowledge"
status: "draft"
date_created: "2025-12-17"
last_updated: "2025-12-17"
domains:
  - "Statistics"
  - "Logic"
tags:
  - "causality"
  - "relationship"
  - "fallacies"
  - "data-interpretation"
difficulty: "beginner"
reading_time: 5
summary: >
  Correlation measures the strength of a relationship between two variables, but it does not imply that one causes the other.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
"Correlation does not imply causation" is perhaps the most famous phrase in statistics. It warns against the logical fallacy of assuming that because two things happen together, one must be causing the other.

## Core Idea
Two variables can be correlated for three main reasons:
1. A causes B.
2. B causes A.
3. C causes both A and B (Confounding variable).
4. Pure coincidence (Spurious correlation).
Statistics alone can detect correlation; it cannot prove causation without experimental design or causal inference methods.

## Formal Definition (if applicable)
- **Correlation**: A statistical measure (like Pearson's $r$) that describes the size and direction of a relationship between two or more variables.
$$ r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2 \sum(y_i - \bar{y})^2}} $$

- **Causation**: Indicates that one event is the result of the occurrence of the other event.

## Intuition
Ice cream sales and shark attacks are highly correlated. Does eating ice cream cause shark attacks? No. Both increase during the summer (the confounding variable).

## Examples
- **Roosters and Sunrise**: The rooster crows before the sun rises (correlation), but the rooster does not *cause* the sun to rise.
- **Sleeping with shoes on**: People who sleep with shoes on wake up with headaches. (Cause: They were likely drunk, which caused both the shoe-sleeping and the headache).

## Common Misconceptions
- **"Correlation implies NO causation"**: Just because correlation doesn't *prove* causation doesn't mean there *isn't* causation. Smoking is correlated with lung cancer, and it also causes it.
- **"Zero correlation means no relationship"**: It only means no *linear* relationship. They could have a strong non-linear relationship (e.g., a U-shape).

## Related Concepts
- Confounding Variable
- Spurious Correlation
- Causal Inference
- Randomized Controlled Trials (RCTs)

## Applications
Essential in observational studies, epidemiology, and economics to avoid drawing incorrect conclusions from data.

## Criticism / Limitations
While useful as a warning, the phrase is sometimes used to dismiss valid evidence. Hill's Criteria are often used in epidemiology to assess causal evidence from correlations.

## Further Reading
- "The Book of Why" by Judea Pearl
- Spurious Correlations (website by Tyler Vigen)
