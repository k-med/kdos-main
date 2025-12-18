---
title: "Propositional Logic"
slug: "propositional-logic"
type: "knowledge"
status: "seed"
date: 2025-12-18
domains: ["Logic", "Mathematics"]
tags: ["truth-tables", "connectives", "tautologies", "contradictions", "inference-rules", "validity"]
difficulty: "beginner"
reading_time: "6 mins"
summary: "The branch of logic that studies ways of joining and/or modifying entire propositions, statements or sentences to form more complicated propositions, statements or sentences."
---

## Overview
**Propositional Logic** (also known as Sentential Logic) is the simplest form of logic. It deals with propositions (statements that can be true or false) and the relationships between them using logical connectives like AND, OR, NOT, and IF-THEN.

## Core Idea
The core idea is to analyze the **structure of arguments** based on how simple statements are combined, ignoring the internal structure of those statements.

## Formal Definition
Propositional logic is a formal system in which the atomic formulas are propositional variables (e.g., $P$, $Q$) and the compound formulas are built using logical connectives ($\land$, $\lor$, $\neg$, $\to$, $\leftrightarrow$).

## Intuition
Think of it as **Boolean algebra for language**. Just as arithmetic has operations like $+$ and $\times$ for numbers, propositional logic has operations for truth values. If "It is raining" ($P$) is true, and "I am wet" ($Q$) is true, then "$P$ AND $Q$" is true.

## Examples
-   **Modus Ponens:** If $P$ implies $Q$, and $P$ is true, then $Q$ is true.
    -   $P \to Q, P \vdash Q$
-   **De Morgan's Laws:** "Not ($P$ and $Q$)" is the same as "(Not $P$) or (Not $Q$)."
    -   $\neg(P \land Q) \iff (\neg P \lor \neg Q)$

## Common Misconceptions
-   **Misconception:** It can handle all logical reasoning.
    -   **Correction:** It cannot handle reasoning about objects and properties (e.g., "All men are mortal"). That requires Predicate Logic.
-   **Misconception:** "OR" means one or the other but not both.
    -   **Correction:** In logic, the standard "OR" ($\lor$) is inclusive (one, the other, or both). Exclusive OR (XOR) is a separate connective.

## Related Concepts
-   **[Predicate Logic](file:///home/kdos/Anvil/kdos-main/content/knowledge/logic/predicate-logic.md):** Extends propositional logic to include quantifiers and predicates.
-   **[Truth Table](file:///home/kdos/Anvil/kdos-main/content/knowledge/logic/truth-table.md):** A mathematical table used to determine if a compound statement is true or false.
-   **[Tautology](file:///home/kdos/Anvil/kdos-main/content/knowledge/logic/tautology.md):** A formula that is always true in every possible interpretation.

## Applications
-   **Computer Circuits:** Logic gates (AND, OR, NOT) are the physical implementation of propositional logic.
-   **Programming:** Boolean logic is fundamental to control flow (if/else statements).
-   **Philosophy:** Used to analyze the validity of arguments.

## Criticism and Limitations
-   **Expressiveness:** It is too simple to capture many forms of natural language reasoning (e.g., "Some cats are black").
-   **Binary Nature:** It assumes everything is strictly True or False, failing to capture nuance or uncertainty (addressed by Fuzzy Logic).

## Further Reading
-   *Logic: A Very Short Introduction* by Graham Priest
-   *Introduction to Logic* by Harry Gensler
