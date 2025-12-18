---
title: "Data Compression"
slug: "data-compression"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Information Theory"
  - "Computer Science"
tags:
  - "lossless"
  - "lossy"
  - "huffman-coding"
  - "zip"
  - "jpeg"
  - "mp3"
difficulty: "intermediate"
reading_time: 6
summary: >
  Data compression is the process of encoding information using fewer bits than the original representation.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
How do you fit a movie on a DVD? Or a song on an iPod? By throwing away the parts you don't need (Lossy) or by finding patterns (Lossless).

## Core Idea
**Redundancy:** Most data repeats itself. "AAAAA" can be written as "5A". Compression removes redundancy.

## Formal Definition (if applicable)
**Lossless Compression:** The original data can be perfectly reconstructed (ZIP, PNG). Used for text and code.
**Lossy Compression:** Some data is lost forever, but the file is much smaller (JPEG, MP3). Used for images and audio where "good enough" is okay.

## Intuition
- **Huffman Coding:** Give short codes to common letters (e = 0) and long codes to rare letters (z = 11011). Like Morse Code (E = dot, Q = dash-dash-dot-dash).
- **Perceptual Coding:** The human ear can't hear quiet sounds right after a loud sound. MP3 deletes the quiet sounds.

## Examples
- **Run-Length Encoding (RLE):** "WWWWWWWWWWWWBWWWWWWWWWWWWBBB" -> "12W1B12W3B".
- **Lempel-Ziv (LZ77):** The algorithm inside ZIP files. It looks for repeated words and replaces them with pointers to the previous occurrence.

## Common Misconceptions
- "You can compress anything." (You can't compress random noise. If a file is already compressed, compressing it again might make it bigger.)
- "Lossy looks bad." (Modern codecs like HEVC or AV1 are almost indistinguishable from the original).

## Related Concepts
- **Kolmogorov Complexity:** The length of the shortest program that can output a string.
- **Entropy Rate:** The theoretical limit of compression.

## Applications
- **Streaming:** Netflix, YouTube, Spotify.
- **Storage:** SSDs compress data on the fly to save space.

## Criticism / Limitations
"Generation Loss." If you save a JPEG as a JPEG over and over, it turns into a blocky mess.

## Further Reading
- Sayood, *Introduction to Data Compression*
