---
title: "Type I and Type II Errors"
slug: "type-i-and-type-ii-errors"
type: "knowledge"
status: "draft"
date_created: "2025-12-17"
last_updated: "2025-12-17"
domains: ["Statistics"]
tags:
  - "hypothesis-testing"
  - "false-positive"
  - "false-negative"
  - "error-analysis"
difficulty: "intermediate"
reading_time: 5
summary: >
  Type I error is a false positive (rejecting a true null), while Type II error is a false negative (failing to reject a false null).
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
In any binary decision process based on probability, there is a risk of being wrong. Statisticians classify these mistakes into two distinct types: False Positives (Type I) and False Negatives (Type II).

## Core Idea
- **Type I (False Positive)**: Crying wolf. You say there is an effect when there isn't.
- **Type II (False Negative)**: Missing the fire. You say there is no effect when there actually is.

## Formal Definition (if applicable)
- **Type I Error ($\alpha$)**: Rejecting $H_0$ when $H_0$ is actually true.
$$ \alpha = P(\text{Reject } H_0 | H_0 \text{ is true}) $$

- **Type II Error ($\beta$)**: Failing to reject $H_0$ when $H_0$ is actually false.
$$ \beta = P(\text{Fail to reject } H_0 | H_0 \text{ is false}) $$

## Intuition
Think of a courtroom trial:
- $H_0$: Defendant is innocent.
- **Type I Error**: Convicting an innocent person. (Usually considered worse in law).
- **Type II Error**: Letting a guilty person go free.

## Examples
- **Medical Testing**:
    - Type I: Telling a healthy patient they have a disease (False Alarm).
    - Type II: Telling a sick patient they are healthy (Missed Diagnosis).
- **Spam Filters**:
    - Type I: Marking a real email as spam.
    - Type II: Letting a spam email into the inbox.

## Common Misconceptions
- **"We can eliminate errors"**: You generally cannot minimize both simultaneously. Lowering the risk of Type I error (stricter standards) usually increases the risk of Type II error (missing real effects), and vice versa.

## Related Concepts
- [Hypothesis Testing](/knowledge/statistics/hypothesis-testing/)
- Statistical Power ($1 - \beta$)
- Significance Level ($\alpha$)
- Sensitivity and Specificity

## Applications
Critical in designing tests where the cost of errors is asymmetric. For example, in cancer screening, a Type II error (missing cancer) is often more dangerous than a Type I error (false alarm).

## Criticism / Limitations
The binary classification simplifies complex decision landscapes where "degrees of belief" might be more appropriate.

## Further Reading
- Signal Detection Theory
- Decision Theory textbooks
