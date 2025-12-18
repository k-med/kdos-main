---
title: "Digital Forensics"
slug: "digital-forensics"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Computer Science"
  - "Law"
tags:
  - "investigation"
  - "evidence"
  - "cybercrime"
  - "recovery"
  - "analysis"
  - "security"
difficulty: "intermediate"
reading_time: 6
summary: >
  Digital forensics is a branch of forensic science encompassing the recovery and investigation of material found in digital devices, often in relation to computer crime.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
When a crime happens, police look for fingerprints. When a cybercrime happens, they look for digital fingerprints. Deleted files, browser history, server logs. Digital Forensics is the science of recovering evidence from computers without altering it, so it stands up in court.

## Core Idea
The core idea is **Chain of Custody**. Proving that the hard drive you analyzed is the exact same hard drive that was seized from the suspect, and that no one tampered with it in between.

## Formal Definition
The recovery and investigation of material found in digital devices.
**Locard's Exchange Principle:** "Every contact leaves a trace." Even in the digital world.

## Intuition
-   **Deleting a file:** You didn't erase the data. You just removed the entry from the Table of Contents. The book pages are still there until you write over them. Forensics tools can read those "deleted" pages.

## Examples
-   **BTK Killer:** Caught because he sent a floppy disk to the police. Forensics found a deleted Word document on it that was registered to "Dennis."
-   **Corporate Espionage:** An employee steals trade secrets before quitting. Forensics can prove they plugged in a USB drive at 4:59 PM on their last day.

## Common Misconceptions
-   **Incognito Mode hides everything:** It stops your browser from saving history, but your ISP, your router, and the server still know exactly what you did.
-   **Wiping a drive is easy:** To truly erase data, you have to overwrite it with random 0s and 1s multiple times (DoD Standard). Or physically destroy the drive.

## Related Concepts
-   **Steganography:** Hiding data inside other data. (e.g., Hiding a text file inside a JPEG image).
-   **Metadata:** Data about data. The photo says "Me at the beach," but the metadata says "Taken with iPhone 12 at GPS coordinates X,Y on Date Z."

## Applications
-   **Data Recovery:** Helping people get their wedding photos back from a crashed hard drive.

## Criticism / Limitations
-   **Encryption:** If the suspect uses strong encryption (AES-256) and refuses to give the password, the evidence is gone forever. Math wins.

## Further Reading
-   Casey, Eoghan. *Digital Evidence and Computer Crime*.
