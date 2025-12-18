---
title: "Object-Oriented Programming"
slug: "object-oriented-programming"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Computer Science"
  - "Software Engineering"
tags:
  - "classes"
  - "objects"
  - "inheritance"
  - "polymorphism"
  - "encapsulation"
  - "abstraction"
difficulty: "beginner"
reading_time: 6
summary: >
  Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields (often known as attributes or properties), and code, in the form of procedures (often known as methods).
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Before OOP, code was a giant list of instructions (Spaghetti Code). OOP organized code into "Objects"—little bundles that contain both data (attributes) and behavior (methods). It models the real world. A "Car" object has a color (data) and can drive (behavior).

## Core Idea
The core idea is **Encapsulation**. Hiding the messy details inside the object. You don't need to know how the engine works to drive the car; you just need to know how to use the steering wheel (Interface).

## Formal Definition
A programming paradigm based on the concept of "objects", which can contain data and code.
Four Pillars:
1.  **Encapsulation:** Hiding data.
2.  **Abstraction:** Simplifying complexity.
3.  **Inheritance:** Sharing code between parents and children.
4.  **Polymorphism:** Treating different objects the same way.

## Intuition
-   **Class:** The blueprint (Cookie Cutter). "A Dog has 4 legs and barks."
-   **Object:** The instance (Cookie). "Fido is a specific Dog."
-   **Inheritance:** "A Poodle is a type of Dog." It gets all the Dog features for free, plus curly hair.

## Examples
-   **Java:** The language that made OOP famous. "Everything is an Object."
-   **Game Design:**
    -   Class: `Enemy`
    -   Subclass: `Orc` (inherits from Enemy, adds `Club`)
    -   Subclass: `Goblin` (inherits from Enemy, adds `Dagger`)
    -   Method: `Attack()` (Polymorphism: Orc swings club, Goblin stabs).

## Common Misconceptions
-   **Inheritance is always good:** Overusing inheritance leads to the "Banana Gorilla Jungle" problem. You wanted a banana, but you got a gorilla holding the banana and the entire jungle. (Composition is often better than Inheritance).

## Related Concepts
-   **Design Patterns:** Standard solutions to common OOP problems (Singleton, Factory, Observer).
-   **SOLID Principles:** Rules for writing good OOP code.

## Applications
-   **Enterprise Software:** OOP is great for managing huge codebases with hundreds of developers. It keeps things organized.

## Criticism / Limitations
-   **Verbosity:** OOP requires a lot of "boilerplate" code (getters, setters, factories).
-   **State Management:** Objects hold state (mutable data), which can lead to bugs when multiple parts of the code try to change the same object at the same time. (See Functional Programming).

## Further Reading
-   Gamma, Erich et al. *Design Patterns: Elements of Reusable Object-Oriented Software*. (The Gang of Four book).
-   Martin, Robert C. *Clean Code*.
