---
title: "Information Theory"
slug: "information-theory"
type: "knowledge"
status: "seed"
date: 2025-12-18
domains: ["Systems", "Mathematics", "Computer Science"]
tags: ["entropy", "bits", "shannon", "signal-to-noise", "compression", "redundancy"]
difficulty: "advanced"
reading_time: "7 mins"
summary: "The mathematical study of the quantification, storage, and communication of information."
---

## Overview
**Information Theory** answers the question: "What is information?" It treats information as a physical quantity, like mass or energy. It is the foundation of the digital age (Internet, CDs, JPGs).

## Core Idea
The core idea is **surprise**. Information is the resolution of uncertainty. If I tell you "The sun rose today," that's low information (predictable). If I tell you "Aliens landed," that's high information (surprising).

## Formal Definition
Founded by Claude Shannon in 1948. It defines the fundamental limits on signal processing and communication operations such as data compression.
-   **Bit:** The basic unit of information (0 or 1).
-   **Entropy:** The measure of uncertainty or randomness.

## Intuition
-   **20 Questions:** The game is about extracting information. Each "Yes/No" answer cuts the search space in half. That is 1 bit of information.
-   **English Language:** English is redundant. "Th qck brwn fx." You can still read it. This redundancy allows us to communicate even in a noisy room (error correction).

## Examples
-   **ZIP Files:** Compression works by removing redundancy. If a file has "AAAAA", you can store it as "5A".
-   **Phone Calls:** Your voice is digitized, compressed, sent as bits, and reconstructed.
-   **DNA:** The genetic code is a digital information storage system.

## Common Misconceptions
-   **Misconception:** Information = Meaning.
    -   **Correction:** Shannon explicitly ignored meaning. "The dog ate the homework" and "Xyz abc def ghijklmn" can have the same *information content* (bits) even if one is nonsense.
-   **Misconception:** More data = More information.
    -   **Correction:** If the data is all the same (redundant), it contains very little information.

## Related Concepts
-   **[Entropy](file:///home/kdos/Anvil/kdos-main/content/knowledge/physics/entropy.md):** Shannon borrowed the term from thermodynamics.
-   **[Cybernetics](file:///home/kdos/Anvil/kdos-main/content/knowledge/systems/cybernetics.md):** Closely related field.

## Applications
-   **Data Compression:** MP3, JPEG.
-   **Cryptography:** Encryption.
-   **Neuroscience:** How the brain codes stimuli.

## Criticism and Limitations
-   **Semantic Gap:** It handles the *transmission* of symbols perfectly but says nothing about the *interpretation* of those symbols.

## Further Reading
-   *The Information* by James Gleick
-   *A Mathematical Theory of Communication* by Claude Shannon
