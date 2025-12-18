---
title: "Semantic Web"
slug: "semantic-web"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Computer Science"
  - "Information Science"
tags:
  - "rdf"
  - "ontologies"
  - "linked-data"
  - "meaning"
  - "web-3.0"
  - "metadata"
difficulty: "advanced"
reading_time: 6
summary: >
  The Semantic Web is an extension of the World Wide Web through standards set by the World Wide Web Consortium (W3C). The goal of the Semantic Web is to make Internet data machine-readable.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
The current Web (Web 2.0) is for humans. We read text and look at pictures. The Semantic Web (Web 3.0) is for machines. It is about tagging data so that computers understand what it *means*. Instead of just "Paris," the computer knows "Paris is a City, located in France, population 2M."

## Core Idea
The core idea is **Linked Data**. Connecting concepts, not just documents.
-   **Current Web:** Link from Page A to Page B.
-   **Semantic Web:** Link from Concept A (Person) to Concept B (Place) with a relationship (Born In).

## Formal Definition
An extension of the Web to make data machine-readable.
Standards: **RDF (Resource Description Framework)**, **OWL (Web Ontology Language)**, **SPARQL**.

## Intuition
-   **HTML:** `<h1>Shakespeare</h1>` (Computer knows it's big text, but doesn't know who Shakespeare is).
-   **RDF:** `<Shakespeare> <is a> <Writer>`. (Computer understands the relationship).

## Examples
-   **Google Knowledge Graph:** When you search "Leonardo da Vinci," the box on the right side with his birth date and paintings is powered by semantic data. Google understands that he is an entity, not just a keyword.
-   **Siri:** "Who is the President of the US?" Siri answers because she understands the semantic relationship "President" -> "US".

## Common Misconceptions
-   **It failed:** The grand vision of a fully semantic web didn't happen (too much work to tag everything). But the technology is used everywhere behind the scenes (Schema.org).

## Related Concepts
-   **Ontology:** A formal naming and definition of the types, properties, and interrelationships of the entities. A map of meaning.
-   **JSON-LD:** The modern way to embed semantic data in websites for SEO.

## Applications
-   **Healthcare:** Linking patient records across different hospitals. "Heart Attack" in one database means the same as "Myocardial Infarction" in another.

## Criticism / Limitations
-   **Trust:** If anyone can say anything about anything, how do you know what is true? (The "Fake News" problem for data).

## Further Reading
-   Berners-Lee, Tim. *Weaving the Web*. (By the inventor of the Web).
-   Allemang, Dean. *Semantic Web for the Working Ontologist*.
