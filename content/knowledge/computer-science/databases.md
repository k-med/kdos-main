---
title: "Databases"
slug: "databases"
type: "knowledge"
status: "seed"
date: 2025-12-18
domains: ["Computer Science"]
tags: ["sql", "nosql", "acid", "transactions", "indexing", "normalization"]
difficulty: "intermediate"
reading_time: "7 mins"
summary: "An organized collection of data, generally stored and accessed electronically from a computer system."
---

## Overview
**Databases** are the memory of civilization. They store everything from your bank balance to your medical records.

## Core Idea
The core idea is **Integrity**. Data must be safe, consistent, and available. You don't want your bank balance to disappear because the power went out.

## Formal Definition
A systematic collection of data.
-   **DBMS (Database Management System):** The software that interacts with end users, applications, and the database itself to capture and analyze the data.

## Intuition
-   **The Filing Cabinet:** A database is a digital filing cabinet, but one that can find any paper in milliseconds.
-   **ACID:** The gold standard for reliability.
    -   *Atomicity:* All or nothing. (Transfer money: Debit A AND Credit B. If one fails, both fail).
    -   *Consistency:* Rules are obeyed.
    -   *Isolation:* Transactions don't interfere.
    -   *Durability:* Once saved, it stays saved (even if the building burns down).

## Examples
-   **SQL (Relational):** Tables with rows and columns. (MySQL, PostgreSQL). Good for structured data (Bank).
-   **NoSQL (Non-Relational):** Documents or Graphs. (MongoDB, Redis). Good for unstructured data (Social Media).

## Common Misconceptions
-   **Misconception:** Excel is a database.
    -   **Correction:** Excel is a spreadsheet. It lacks the integrity, security, and scalability of a real database.
-   **Misconception:** More data is always better.
    -   **Correction:** "Data swamps" are useless. Data needs structure and quality.

## Related Concepts
-   **[Data Structures](file:///home/kdos/Anvil/kdos-main/content/knowledge/computer-science/data-structures.md):** Databases use B-Trees and Hash Tables internally.
-   **[Distributed Systems](file:///home/kdos/Anvil/kdos-main/content/knowledge/computer-science/distributed-systems.md):** Sharding a database across multiple servers.

## Applications
-   **E-commerce:** Inventory and orders.
-   **Analytics:** Data Warehouses.

## Criticism and Limitations
-   **CAP Theorem:** You can't have it all (Consistency, Availability, Partition Tolerance). You have to choose two.

## Further Reading
-   *Designing Data-Intensive Applications* by Martin Kleppmann
