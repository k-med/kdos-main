---
title: "Functional Programming"
slug: "functional-programming"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Computer Science"
  - "Mathematics"
tags:
  - "lambda-calculus"
  - "immutability"
  - "haskell"
  - "recursion"
  - "pure-functions"
  - "paradigm"
difficulty: "intermediate"
reading_time: 6
summary: >
  Functional programming is a programming paradigm where programs are constructed by applying and composing functions. It is a declarative programming paradigm in which function definitions are trees of expressions that map values to other values, rather than a sequence of imperative statements which update the running state of the program.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Most coding (Imperative) is like a recipe: "Do this, then do that, then change this variable." Functional Programming (FP) is like math: "f(x) = y." It avoids "side effects" (changing things outside the function). It is cleaner, safer, and easier to debug, but it requires a different way of thinking.

## Core Idea
The core idea is **Immutability**. Once you create a variable, you can never change it. If you want to change it, you have to create a *new* variable.
-   **Imperative:** `x = x + 1` (x is now different).
-   **Functional:** `y = x + 1` (x stays the same forever).

## Formal Definition
A programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data.
Based on **Lambda Calculus**.

## Intuition
-   **Imperative:** A factory assembly line. The car moves down the line, and robots bolt parts onto it. The car changes at every step.
-   **Functional:** A series of pipes. Water flows in, goes through a filter, then a heater, then a bottler. The water doesn't "change" in place; it flows through transformations.

## Examples
-   **Haskell:** The purest FP language. It forces you to write pure functions. If you try to change a variable, the compiler yells at you.
-   **Map/Filter/Reduce:** The holy trinity of FP.
    -   **Map:** Apply a function to every item in a list (Double every number).
    -   **Filter:** Keep only items that match a rule (Keep evens).
    -   **Reduce:** Combine all items into one (Sum them up).
-   **Excel:** The world's most popular functional language. The value of a cell depends only on the other cells it references. It updates automatically.

## Common Misconceptions
-   **It's slow:** Creating new variables instead of changing old ones sounds slow, but modern compilers optimize it (Garbage Collection).
-   **It's academic:** It's used in finance and big data (Spark) because it handles parallel processing perfectly (no race conditions).

## Related Concepts
-   **Recursion:** FP doesn't use loops (`for`, `while`). It uses recursion (a function calling itself) to repeat things.
-   **Higher-Order Functions:** Functions that take other functions as arguments.

## Applications
-   **Concurrency:** Since data never changes, you can run the code on 1,000 cores at once without worrying about one core overwriting what another core is reading.

## Criticism / Limitations
-   **Learning Curve:** It is hard to unlearn imperative habits. Monads (a way to handle side effects) are notoriously confusing.

## Further Reading
-   Abelson, Hal and Sussman, Gerald. *Structure and Interpretation of Computer Programs*. (The wizard book).
-   Lipovaca, Miran. *Learn You a Haskell for Great Good!*.
