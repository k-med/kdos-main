---
title: "Predicate Logic"
slug: "predicate-logic"
type: "knowledge"
status: "seed"
date: 2025-12-18
domains: ["Logic", "Mathematics"]
tags: ["quantifiers", "variables", "predicates", "relations", "first-order-logic", "models"]
difficulty: "intermediate"
reading_time: "7 mins"
summary: "An extension of propositional logic that uses quantifiers and predicates to express statements about objects and their properties."
---

## Overview
**Predicate Logic** (usually First-Order Logic) extends propositional logic by breaking down statements into subjects (objects) and predicates (properties or relations). It introduces quantifiers like "For all" ($\forall$) and "There exists" ($\exists$).

## Core Idea
The core idea is to formalize reasoning about **collections of objects**. Instead of just saying "Socrates is mortal" is a proposition $P$, we say "For all $x$, if $x$ is a man, then $x$ is mortal."

## Formal Definition
Predicate logic is a formal system that uses quantified variables over non-logical objects and allows the use of sentences that contain variables. It includes:
-   **Constants:** $a, b, c$ (specific objects)
-   **Variables:** $x, y, z$ (placeholders)
-   **Predicates:** $P(x), R(x,y)$ (properties/relations)
-   **Quantifiers:** $\forall$ (universal), $\exists$ (existential)

## Intuition
Propositional logic treats sentences as black boxes. Predicate logic **opens the box**. It allows us to see the internal structure: "All humans are mortal" becomes $\forall x (Human(x) \to Mortal(x))$.

## Examples
-   **Syllogism:**
    1.  All men are mortal: $\forall x (Man(x) \to Mortal(x))$
    2.  Socrates is a man: $Man(Socrates)$
    3.  Therefore, Socrates is mortal: $Mortal(Socrates)$
-   **Mathematics:** "For every number $x$, there is a number $y$ such that $y > x$": $\forall x \exists y (y > x)$.

## Common Misconceptions
-   **Misconception:** $\forall x \exists y$ is the same as $\exists y \forall x$.
    -   **Correction:** Order matters! "Everyone loves someone" ($\forall x \exists y L(x,y)$) is different from "There is someone everyone loves" ($\exists y \forall x L(x,y)$).
-   **Misconception:** It can express everything.
    -   **Correction:** First-order logic cannot quantify over properties themselves (e.g., "For every property $P$..."). That requires Second-Order Logic.

## Related Concepts
-   **[Propositional Logic](file:///home/kdos/Anvil/kdos-main/content/knowledge/logic/propositional-logic.md):** The simpler logic that predicate logic is built upon.
-   **[Quantifier](file:///home/kdos/Anvil/kdos-main/content/knowledge/logic/quantifier.md):** A symbol that specifies the quantity of specimens in the domain of discourse that satisfy an open formula.
-   **[Model Theory](file:///home/kdos/Anvil/kdos-main/content/knowledge/logic/model-theory.md):** The study of the relationship between formal theories and their interpretations (models).

## Applications
-   **Mathematics:** The standard language for axiomatizing mathematical theories (like ZFC Set Theory).
-   **Computer Science:** Used in databases (SQL is based on relational calculus, a form of predicate logic) and AI (knowledge representation).
-   **Linguistics:** Used to model the semantics of natural language.

## Criticism and Limitations
-   **Undecidability:** Unlike propositional logic, there is no algorithm that can decide the validity of every first-order logic formula (Church's Theorem).
-   **Complexity:** It can be computationally expensive to reason with.

## Further Reading
-   *Language, Proof and Logic* by Dave Barker-Plummer et al.
-   *Mathematical Logic* by H.-D. Ebbinghaus
