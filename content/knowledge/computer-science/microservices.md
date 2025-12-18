---
title: "Microservices"
slug: "microservices"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Computer Science"
  - "Software Engineering"
tags:
  - "architecture"
  - "decoupling"
  - "services"
  - "scalability"
  - "deployment"
  - "containers"
difficulty: "advanced"
reading_time: 6
summary: >
  Microservices are a variant of the service-oriented architecture (SOA) architectural style that structures an application as a collection of loosely coupled services. In a microservices architecture, services are fine-grained and the protocols are lightweight.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
In the past, apps were "Monoliths." One giant block of code. If you wanted to change the font on the login page, you had to redeploy the entire bank. Microservices break the app into tiny, independent pieces. The "Login" service is separate from the "Payment" service. They talk to each other, but they don't touch.

## Core Idea
The core idea is **Decoupling**. Making sure that if one part breaks, the whole ship doesn't sink. (Bulkheads).

## Formal Definition
An architectural style that structures an application as a collection of loosely coupled services.
Properties: **Independently Deployable**, **Organized around Business Capabilities**.

## Intuition
-   **Monolith:** A Swiss Army Knife. It does everything, but if the scissors break, you have to throw the whole knife away.
-   **Microservices:** A toolbox. You have a hammer, a screwdriver, and a wrench. If the hammer breaks, you just buy a new hammer. The screwdriver still works.

## Examples
-   **Netflix:** The poster child. They have 1,000+ microservices. One service just recommends movies. One service just processes credit cards. One service just encodes video.
-   **Uber:** When you request a ride, it hits hundreds of services (Driver Matching, Maps, Payments, Notifications).

## Common Misconceptions
-   **It's always better:** No. For small startups, it is overkill ("Distributed Monolith"). It adds massive complexity (network latency, debugging). Start with a Monolith; break it up later.

## Related Concepts
-   **Containers (Docker):** The box that holds the microservice.
-   **Kubernetes:** The captain that manages the thousands of containers.

## Applications
-   **Scalability:** If the "Login" service is slow, you can just add 10 more Login servers without touching the rest of the app.

## Criticism / Limitations
-   **Complexity:** "You replaced one function call with a network request." Now you have to worry about timeouts, retries, and network failures.

## Further Reading
-   Newman, Sam. *Building Microservices*.
