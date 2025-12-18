---
title: "DevOps"
slug: "devops"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Computer Science"
  - "Management"
tags:
  - "ci-cd"
  - "automation"
  - "operations"
  - "culture"
  - "deployment"
  - "monitoring"
difficulty: "intermediate"
reading_time: 6
summary: >
  DevOps is a set of practices that combines software development (Dev) and IT operations (Ops). It aims to shorten the systems development life cycle and provide continuous delivery with high software quality.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
Historically, Developers (Dev) and System Administrators (Ops) were enemies. Devs wanted to change things (add features). Ops wanted to keep things stable (don't touch anything). DevOps is the peace treaty. It says: "You build it, you run it."

## Core Idea
The core idea is **Automation**. Automating the boring stuff (testing, deploying, configuring servers) so that humans can focus on the interesting stuff.

## Formal Definition
A set of practices that combines software development (Dev) and IT operations (Ops).
**The Three Ways:**
1.  **Flow:** Fast movement from Dev to Ops.
2.  **Feedback:** Fast information from Ops back to Dev.
3.  **Learning:** Continuous experimentation.

## Intuition
-   **Old Way:** Dev writes code, throws it over the wall to Ops. Ops tries to run it. It crashes. Ops blames Dev. Dev blames Ops.
-   **DevOps Way:** Dev writes code. A robot (CI/CD) tests it and deploys it. If it crashes, the Dev gets paged.

## Examples
-   **CI/CD (Continuous Integration / Continuous Deployment):** The pipeline. Code -> Test -> Build -> Deploy. Facebook deploys code 100 times a day.
-   **Infrastructure as Code (IaC):** Managing servers using code (Terraform). You don't click buttons in the AWS console; you write a script.

## Common Misconceptions
-   **It's a job title:** "We hired a DevOps Engineer." DevOps is a *culture*, not a role. Everyone should do it.

## Related Concepts
-   **SRE (Site Reliability Engineering):** Google's version of DevOps. "Treating operations as if it's a software problem."

## Applications
-   **Speed:** Companies that use DevOps can release features 100x faster than competitors.

## Criticism / Limitations
-   **Burnout:** Since developers are now responsible for the servers too, they are on call 24/7.

## Further Reading
-   Kim, Gene. *The Phoenix Project*. (A novel about IT. Surprisingly gripping).
-   Humble, Jez. *Continuous Delivery*.
