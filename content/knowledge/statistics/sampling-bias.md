---
title: "Sampling Bias"
slug: "sampling-bias"
type: "knowledge"
status: "draft"
date_created: "2025-12-17"
last_updated: "2025-12-17"
domains: ["Statistics"]
tags:
  - "selection-bias"
  - "data-collection"
  - "survey-methodology"
  - "representative-sample"
difficulty: "beginner"
reading_time: 5
summary: >
  Sampling bias occurs when some members of a population are systematically more likely to be selected in a sample than others, leading to a non-representative sample.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Sampling bias is a systematic error in data collection. If your sample doesn't look like the population you care about, your conclusions will be wrong, no matter how fancy your statistics are.

## Core Idea
"Garbage in, garbage out." If you only ask rich people about the economy, you'll think the economy is doing great. The method of selection skewed the result.

## Formal Definition (if applicable)
A bias in which a sample is collected in such a way that some members of the intended population have a lower or higher sampling probability than others.

## Intuition
Imagine trying to determine the average size of fish in a lake, but your net has large holes. You will only catch big fish and conclude that "all fish in this lake are huge." The tool (net) introduced a bias.

## Examples
- **Dewey Defeats Truman (1948)**: A phone survey predicted Dewey would win. But in 1948, only wealthy people had phones, and they leaned Republican. The sample was biased.
- **Online Reviews**: People are more likely to leave a review if they love or hate a product. The "average" experience is under-represented.

## Common Misconceptions
- **"Large sample size fixes bias"**: No! A large biased sample is just a *precisely wrong* answer. Asking 1 million people on Twitter about an election is worse than asking 1,000 random people.

## Related Concepts
- [Central Limit Theorem](/knowledge/statistics/central-limit-theorem/) (requires random sampling)
- Survivorship Bias
- Selection Bias
- Random Sampling

## Applications
Critical in survey design, political polling, and training AI models (to avoid algorithmic bias).

## Criticism / Limitations
It is often impossible to get a perfectly random sample. Researchers must instead acknowledge bias and try to correct for it (e.g., weighting).

## Further Reading
- "How to Lie with Statistics" by Darrell Huff
