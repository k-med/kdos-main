---
title: "Linear Regression"
slug: "linear-regression"
type: "knowledge"
status: "draft"
date_created: "2025-12-17"
last_updated: "2025-12-17"
domains:
  - "Statistics"
  - "Machine Learning"
tags:
  - "predictive-modeling"
  - "relationship"
  - "dependent-variable"
  - "independent-variable"
difficulty: "intermediate"
reading_time: 6
summary: >
  Linear regression models the relationship between a dependent variable and one or more independent variables by fitting a linear equation to observed data.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Linear regression is the "Hello World" of machine learning and the workhorse of statistical modeling. It tries to draw the "best fit" straight line through a scatterplot of data points.

## Core Idea
Find the line $y = mx + b$ that minimizes the distance (error) between the line and the actual data points. This allows you to predict $y$ for a new $x$.

## Formal Definition (if applicable)
Simple Linear Regression: $y = \beta_0 + \beta_1 x + \epsilon$
- $y$: Dependent variable (Target)
- $x$: Independent variable (Feature)
- $\beta_0$: Intercept
- $\beta_1$: Slope (Coefficient)
- $\epsilon$: Error term (Residual)

## Intuition
If you plot "Hours Studied" vs "Exam Score," you'll likely see an upward trend. Linear regression draws the line that best summarizes this trend, allowing you to say: "For every extra hour studied, the score increases by 5 points on average."

## Examples
- **Real Estate**: Predicting house prices based on square footage.
- **Economics**: Estimating the impact of interest rates on inflation.

## Common Misconceptions
- **"Linear means straight line only"**: In simple regression, yes. But you can include polynomial terms ($x^2$) to model curves while still using "linear" regression techniques (linear in parameters).
- **"Correlation is enough"**: Regression gives you the *slope* (how much $y$ changes), whereas correlation only gives the *strength* of the relationship.

## Related Concepts
- [Correlation vs Causation](/knowledge/statistics/correlation-vs-causation/)
- Residuals
- R-squared ($R^2$)
- Overfitting

## Applications
Used for forecasting, determining causal relationships (in controlled settings), and quantifying trends.

## Criticism / Limitations
It assumes a linear relationship. If the data is curved (e.g., exponential growth), a straight line is a terrible model. It is also sensitive to outliers.

## Further Reading
- "An Introduction to Statistical Learning" by James, Witten, Hastie, and Tibshirani
