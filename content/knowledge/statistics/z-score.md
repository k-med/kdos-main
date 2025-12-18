---
title: "Z-score"
slug: "z-score"
type: "knowledge"
status: "draft"
date_created: "2025-12-17"
last_updated: "2025-12-17"
domains: ["Statistics"]
tags:
  - "standardization"
  - "normal-distribution"
  - "standard-score"
  - "data-normalization"
difficulty: "beginner"
reading_time: 4
summary: >
  A Z-score describes a value's relationship to the mean of a group of values, measured in terms of standard deviations from the mean.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
A Z-score (standard score) tells you exactly where a data point fits into a distribution. It allows you to compare apples to oranges by standardizing different scales onto a common metric.

## Core Idea
It answers: "How weird is this value?"
- **Z = 0**: Exactly average.
- **Z = +1**: One standard deviation above average.
- **Z = -2**: Two standard deviations below average.

## Formal Definition (if applicable)
$$ Z = \frac{x - \mu}{\sigma} $$

Where $x$ is the raw score, $\mu$ is the population mean, and $\sigma$ is the population standard deviation.

## Intuition
If you scored 80 on a math test and 80 on a history test, which was better?
- Math: Mean=70, SD=10. $Z = (80-70)/10 = +1.0$.
- History: Mean=60, SD=5. $Z = (80-60)/5 = +4.0$.
You did vastly better in history, because an 80 was 4 standard deviations above the mean (extremely rare), whereas in math it was just somewhat above average.

## Examples
- **Standardized Testing**: SAT and IQ scores are often normalized so percentiles can be calculated from Z-scores.
- **Outlier Detection**: A common rule of thumb is that any data point with a Z-score greater than +3 or less than -3 is an outlier.

## Common Misconceptions
- **"Z-scores require normal distribution"**: You can calculate a Z-score for any distribution, but the probabilities associated with Z-scores (like "95% are within +/- 1.96") only apply if the distribution is normal.

## Related Concepts
- [Normal Distribution](/knowledge/statistics/normal-distribution/)
- [Standard Deviation](/knowledge/statistics/standard-deviation/)
- Percentiles
- Standardization

## Applications
Used in data preprocessing for machine learning (normalization), comparing scores from different datasets, and identifying outliers.

## Criticism / Limitations
Z-scores are sensitive to the mean and standard deviation, which themselves are sensitive to outliers. In skewed distributions, Z-scores may be misleading.

## Further Reading
- Statistics textbooks on standardization
