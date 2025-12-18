---
title: "Software Testing"
slug: "software-testing"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Computer Science"
  - "Engineering"
tags:
  - "qa"
  - "unit-testing"
  - "integration"
  - "debugging"
  - "verification"
  - "automation"
difficulty: "beginner"
reading_time: 6
summary: >
  Software testing is an investigation conducted to provide stakeholders with information about the quality of the software product or service under test. Software testing can also provide an objective, independent view of the software to allow the business to appreciate and understand the risks of software implementation.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Code is fragile. If you change one line, you might break something else 1,000 lines away. Software Testing is the safety net. It is the discipline of verifying that the code does what it is supposed to do. Without testing, software is just a ticking time bomb.

## Core Idea
The core idea is **Verification and Validation**.
-   **Verification:** "Are we building the product right?" (Does the code work?)
-   **Validation:** "Are we building the right product?" (Does the user want this?)

## Formal Definition
An investigation conducted to provide information about the quality of the software.
**Pyramid of Testing:** Unit Tests (Base) -> Integration Tests -> End-to-End Tests (Top).

## Intuition
-   **Unit Test:** Checking a single brick. "Is this brick solid?"
-   **Integration Test:** Checking a wall. "Do the bricks stick together?"
-   **End-to-End (E2E) Test:** Checking the house. "Can I open the front door and walk to the kitchen?"

## Examples
-   **TDD (Test Driven Development):** Writing the test *before* you write the code.
    1.  Write a test that fails (Red).
    2.  Write the code to pass the test (Green).
    3.  Clean up the code (Refactor).
-   **Regression Testing:** Running all old tests every time you make a change. This ensures you didn't break old features (Regress).
-   **Chaos Engineering:** Netflix Simian Army. They unleash a "Chaos Monkey" that randomly turns off servers in production to ensure the system can survive a crash.

## Common Misconceptions
-   **Testers break code:** No, the code was already broken. Testers just found the break.
-   **100% Coverage:** It is impossible to test every possible input. You aim for high coverage of the *critical* paths.

## Related Concepts
-   **QA (Quality Assurance):** The process of preventing bugs.
-   **CI/CD (Continuous Integration):** Running tests automatically every time a developer saves a file.

## Applications
-   **Space Shuttle:** The most tested software in history. It had 400,000 lines of code and almost zero bugs. It cost $1,000 per line of code to write.

## Criticism / Limitations
-   **Flaky Tests:** Tests that sometimes pass and sometimes fail (randomly). They destroy trust in the testing system.

## Further Reading
-   Myers, Glenford. *The Art of Software Testing*.
-   Beck, Kent. *Test Driven Development: By Example*.
