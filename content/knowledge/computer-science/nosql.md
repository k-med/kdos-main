---
title: "NoSQL"
slug: "nosql"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Computer Science"
  - "Databases"
tags:
  - "mongodb"
  - "key-value"
  - "document"
  - "scalability"
  - "schema-less"
  - "big-data"
difficulty: "intermediate"
reading_time: 6
summary: >
  NoSQL (originally referring to "non-SQL" or "non-relational") databases provides a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in relational databases.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
For 30 years, databases were spreadsheets (SQL). Rows and columns. Strict rules. But then the internet happened. Google and Facebook had too much data and it was too messy for a spreadsheet. They invented NoSQL ("Not Only SQL"). It is flexible, fast, and messy.

## Core Idea
The core idea is **Flexibility**. In SQL, you have to define the schema ("User has a Name and Age") before you save data. In NoSQL, you can just dump data in. "User has a Name, Age, and... uh... a list of favorite Pokemon." NoSQL doesn't care.

## Formal Definition
A broad class of database management systems that do not use the relational model (tables).
Types:
1.  **Document (MongoDB):** Storing JSON files.
2.  **Key-Value (Redis):** A giant dictionary.
3.  **Graph (Neo4j):** Storing connections (Social Network).
4.  **Column-Family (Cassandra):** Storing massive amounts of data across thousands of servers.

## Intuition
-   **SQL:** A filing cabinet. Everything must be filed in the right folder, alphabetically.
-   **NoSQL:** A bucket. Just throw stuff in. It's faster to put things in, but harder to find them later if you aren't organized.

## Examples
-   **MongoDB:** The most popular NoSQL DB. Used by startups because it lets you change your data structure on the fly without breaking the app.
-   **Redis:** Stores data in RAM (memory) instead of on the Hard Drive. It is lightning fast. Used for caching (remembering your login session).
-   **Cassandra:** Used by Facebook and Netflix. It can run on 10,000 servers at once. If 100 servers die, the database keeps working.

## Common Misconceptions
-   **NoSQL is better:** It's not better; it's different. SQL is better for money (Banks) because it guarantees consistency (ACID). NoSQL is better for Big Data (Likes, Tweets) where speed matters more than perfection.

## Related Concepts
-   **CAP Theorem:** You can only have 2 of the 3: **C**onsistency, **A**vailability, **P**artition Tolerance. NoSQL usually chooses A and P (Always up, but maybe slightly out of date). SQL chooses C and A.

## Applications
-   **Real-Time Analytics:** Tracking clicks on a website.
-   **Content Management:** Storing blog posts and comments.

## Criticism / Limitations
-   **No Joins:** In SQL, you can easily say "Get all users who bought a shoe." In NoSQL, that is hard. You have to write code to do it manually.

## Further Reading
-   Sadalage, Pramod. *NoSQL Distilled*.
