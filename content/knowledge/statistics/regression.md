---
title: "Regression"
slug: "regression"
type: "knowledge"
status: "seed"
date: 2025-12-18
domains: ["Statistics"]
tags: ["linear-regression", "correlation", "prediction", "variables", "r-squared", "modeling"]
difficulty: "intermediate"
reading_time: "7 mins"
summary: "A set of statistical processes for estimating the relationships between a dependent variable and one or more independent variables."
---

## Overview
**Regression Analysis** is the crystal ball of statistics. It allows us to predict the future (or the unknown) based on relationships between variables. It draws the "line of best fit."

## Core Idea
The core idea is **relationship**. How does $X$ affect $Y$? If I study one more hour ($X$), how much will my grade increase ($Y$)?

## Formal Definition
**Linear Regression:** $Y = mx + b$.
-   $Y$: Dependent Variable (Outcome).
-   $X$: Independent Variable (Predictor).
-   $m$: Slope (Effect size).
-   $b$: Intercept (Starting point).

## Intuition
-   **The Scatterplot:** Imagine dots on a graph. Regression draws the line that goes through the middle of the cloud, minimizing the distance to all points.
-   **Correlation ($r$):** How tight are the dots to the line? (1 = Perfect line, 0 = Random cloud).
-   **$R^2$:** How much of the variation is explained? ($R^2 = 0.8$ means "We understand 80% of what's going on").

## Examples
-   **Real Estate:** Predicting house prices based on Square Footage, Bedrooms, and Zip Code.
-   **Health:** Predicting life expectancy based on Smoking, Diet, and Exercise.

## Common Misconceptions
-   **Misconception:** Regression proves causation.
    -   **Correction:** Ice cream sales correlate with shark attacks (both go up in summer). Regression finds the link, but not the cause.
-   **Misconception:** You can extrapolate forever.
    -   **Correction:** If you grow 2 inches a year as a kid, regression predicts you'll be 10 feet tall by age 40.

## Related Concepts
-   **[Machine Learning](file:///home/kdos/Anvil/kdos-main/content/knowledge/computer-science/machine-learning.md):** Regression is the simplest ML algorithm.
-   **[Econometrics](file:///home/kdos/Anvil/kdos-main/content/knowledge/economics/econometrics.md):** Using regression for economics.

## Applications
-   **Business:** Sales forecasting.
-   **Algorithmic Trading:** Predicting stock prices.

## Criticism and Limitations
-   **Overfitting:** Making a model so complex it fits the noise, not the signal.
-   **Linearity:** The world is often curved, not linear.

## Further Reading
-   *The Art of Statistics* by David Spiegelhalter
-   *Introduction to Statistical Learning* by James et al.
