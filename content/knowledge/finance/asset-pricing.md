---
title: "Asset Pricing"
slug: "asset-pricing"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains: ["Finance", "Economics"]
tags:
  - "capm"
  - "arbitrage-pricing-theory"
  - "risk-return"
  - "beta"
  - "valuation"
  - "efficient-market-hypothesis"
difficulty: "advanced"
reading_time: 7
summary: >
  Asset pricing is a branch of finance that tries to determine the fair price of an asset (like a stock or bond) based on its risk and expected return.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Why does Apple stock cost \$150 and Ford cost \$12? Is it just supply and demand, or is there a fundamental value? Asset pricing models try to find the "correct" price.

## Core Idea
**Risk-Return Tradeoff:** Higher risk must be compensated with higher expected return. No one buys a risky stock unless they think it will pay off big.

## Formal Definition (if applicable)
**CAPM (Capital Asset Pricing Model):**
$$ E(R_i) = R_f + \beta_i (E(R_m) - R_f) $$
- Expected Return = Risk-Free Rate + Beta $\times$ Market Risk Premium.
- **Beta ($\beta$):** A measure of how much the stock moves with the market. High beta = High risk.

## Intuition
- **Risk-Free Rate:** What you get for lending to the US government (safe).
- **Market Risk Premium:** The extra return you get for investing in the stock market (risky).
- **Beta:** If the market goes up 10%, does your stock go up 10% ($\beta=1$), 20% ($\beta=2$), or 5% ($\beta=0.5$)?

## Examples
- **Arbitrage:** Buying low in one market and selling high in another. (Risk-free profit).
- **Efficient Market Hypothesis (EMH):** Prices already reflect all available information, so you can't beat the market.

## Common Misconceptions
- "A good company is a good stock." (Not if the price is too high.)
- "Past performance predicts future results." (It usually doesn't.)

## Related Concepts
- **Alpha:** The return you get *above* what CAPM predicts (skill).
- **Sharpe Ratio:** Return per unit of risk.
- **Black-Scholes Model:** Pricing options.

## Applications
- **Portfolio Management:** Selecting stocks.
- **Corporate Finance:** Calculating the cost of capital.

## Criticism / Limitations
CAPM assumes markets are rational and efficient. Behavioral finance says they aren't. Fama-French models add more factors (size, value) to fix CAPM's flaws.

## Further Reading
- Cochrane, *Asset Pricing*
- Fama & French, *Common Risk Factors in the Returns on Stocks and Bonds*
