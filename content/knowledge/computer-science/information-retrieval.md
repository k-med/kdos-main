---
title: "Information Retrieval"
slug: "information-retrieval"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Computer Science"
  - "Library Science"
tags:
  - "search-engines"
  - "indexing"
  - "ranking"
  - "relevance"
  - "web-crawling"
  - "google"
difficulty: "intermediate"
reading_time: 6
summary: >
  Information retrieval (IR) is the activity of obtaining information system resources that are relevant to an information need from a collection of those resources. Searches can be based on full-text or other content-based indexing.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
We live in the Information Age. But information is useless if you can't find it. Information Retrieval (IR) is the science of search. It's how Google finds one specific page out of billions in 0.1 seconds. It's how Netflix recommends a movie.

## Core Idea
The core idea is **Indexing**. You can't scan every book in the library every time someone asks a question. You need an index (a lookup table).
-   **Inverted Index:** A list of every word, and which documents contain it.
    -   "Apple" -> Doc 1, Doc 5, Doc 99.
    -   "Banana" -> Doc 2, Doc 5.

## Formal Definition
The activity of obtaining information system resources that are relevant to an information need from a collection.
Key Metrics:
-   **Precision:** How many of the results were actually relevant? (Quality).
-   **Recall:** How many of the relevant documents did you find? (Quantity).

## Intuition
-   **Boolean Search:** "Cat AND Dog". Finds docs with both.
-   **Ranking:** The hard part. Which document is the *best* match?
-   **PageRank:** Google's billion-dollar idea. A page is important if other important pages link to it. It treats links as votes.

## Examples
-   **Google Search:** The ultimate IR system. It crawls the web, indexes it, and ranks it using hundreds of signals (keywords, speed, mobile-friendliness).
-   **TF-IDF (Term Frequency-Inverse Document Frequency):** A math formula to decide how important a word is.
    -   "The" appears everywhere (Low importance).
    -   "Platypus" appears rarely (High importance).
    -   If a document has "Platypus" 5 times, it's probably about platypuses.
-   **Vector Search:** The modern way (AI). Searching by meaning, not just keywords. (See NLP).

## Common Misconceptions
-   **SEO is cheating:** Search Engine Optimization is just helping the IR system understand your content.
-   **It searches the live web:** No, it searches the *index* (a copy of the web stored on Google's servers). That's why you sometimes see "Cached" pages.

## Related Concepts
-   **Web Crawler (Spider):** The bot that visits pages and follows links to find new pages.
-   **Recommender Systems:** "People who bought X also bought Y." A form of IR where the query is "What would I like?"

## Applications
-   **Legal Discovery:** Lawyers use IR to search millions of emails for evidence ("Find all emails mentioning 'fraud'").

## Criticism / Limitations
-   **Filter Bubbles:** If the search engine only shows you what you *want* to see (based on your history), you never see opposing viewpoints.

## Further Reading
-   Manning, Raghavan, Schütze. *Introduction to Information Retrieval*.
-   Levy, Steven. *In The Plex*. (The story of Google).
