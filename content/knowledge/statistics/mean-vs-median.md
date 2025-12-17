---
title: "Mean vs Median"
slug: "mean-vs-median"
type: "knowledge"
status: "draft"
date_created: "2025-12-17"
last_updated: "2025-12-17"
domains:
  - "Statistics"
tags:
  - "central-tendency"
  - "descriptive-statistics"
  - "mean"
  - "median"
  - "outliers"
  - "skewness"
  - "data-distribution"
  - "robust-statistics"
difficulty: "beginner"
reading_time: 4
summary: >
  Mean and median are measures of central tendency that summarize a dataset’s typical value, differing primarily in how they respond to skewness and outliers.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Mean and median are two foundational statistics used to describe the center of a numerical dataset. While both aim to capture a “typical” value, they behave differently depending on the distribution of the data.

## Core Idea
The mean averages all values and is sensitive to extreme observations, whereas the median identifies the middle value and is robust to outliers. Choosing between them depends on the data’s distribution and the analytical goal.

## Formal Definition (if applicable)
For a dataset \(x_1, x_2, \dots, x_n\):

- **Mean (arithmetic mean)**:  
  \[
  \bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
  \]
- **Median**:  
  The middle value after sorting the data; if \(n\) is even, it is the average of the two central values.

## Intuition
The mean asks, “What value would make the total balance out evenly?”  
The median asks, “What value splits the data into two equal halves?”  
As a result, the mean is pulled toward extremes, while the median resists them.

## Examples
- Dataset: \( \{2, 3, 3, 4, 100\} \)  
  Mean = 22.4, Median = 3.  
  The large outlier inflates the mean but leaves the median largely unchanged.
- In a symmetric distribution without outliers, mean and median are equal or very close.

## Common Misconceptions
- “The mean always represents the typical value.”  
  This fails in skewed distributions.
- “Median ignores most of the data.”  
  While it depends on order rather than magnitude, it still reflects the dataset’s central position.

## Related Concepts
- Mode
- Skewness
- Outliers
- Trimmed mean
- Robust statistics

## Applications
- **Income and wealth**: Median income better reflects typical earners in skewed distributions.
- **Quality control**: Mean is useful when deviations in either direction matter equally.
- **Exploratory data analysis**: Comparing mean and median helps diagnose skewness.

## Criticism / Limitations
Neither statistic captures variability or distribution shape. Relying solely on mean or median can obscure multimodality or dispersion, requiring complementary measures such as variance or quantiles.

## Further Reading
- Introductory statistics textbooks on descriptive statistics
- Discussions of robust measures of central tendency in statistical methodology
