---
title: "Signal Processing"
slug: "signal-processing"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Engineering"
  - "Mathematics"
tags:
  - "fourier-transform"
  - "filtering"
  - "sampling"
  - "digital-signals"
  - "analog-signals"
  - "modulation"
difficulty: "advanced"
reading_time: 7
summary: >
  Signal processing is an electrical engineering subfield that focuses on analyzing, modifying, and synthesizing signals such as sound, images, and scientific measurements.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
How does your phone turn your voice into radio waves? How does Spotify compress music? How does an MRI see inside your body? It's all signal processing.

## Core Idea
**Fourier Transform:** Any complex wave can be broken down into a sum of simple sine waves. It converts a signal from the Time Domain (what happens when) to the Frequency Domain (what pitch is it).

## Formal Definition (if applicable)
**Nyquist-Shannon Sampling Theorem:** To perfectly reconstruct a signal, you must sample it at a rate at least twice its highest frequency. (CDs sample at 44.1 kHz to capture human hearing up to 22 kHz).

## Intuition
- **Filter:** Sunglasses filter out UV light. Audio filters remove hiss (high frequency) or rumble (low frequency).
- **Compression:** Removing parts of the signal humans can't perceive (MP3, JPEG).

## Examples
- **Noise Cancellation:** Headphones recording outside noise and playing the *inverse* wave to cancel it out.
- **Auto-Tune:** Pitch correction.
- **Image Processing:** Photoshop filters, edge detection in self-driving cars.

## Common Misconceptions
- "Digital is always better." (Analog vinyl records have infinite resolution, though they have noise. Digital is discrete.)
- "Zoom and Enhance." (You can't create information that isn't there. CSI lied to you.)

## Related Concepts
- **DSP (Digital Signal Processor):** A specialized chip for math.
- **Convolution:** A mathematical operation used in filtering and reverb.
- **Modulation:** Encoding information onto a carrier wave (AM/FM radio).

## Applications
- **Telecommunications:** 5G, Wi-Fi.
- **Audio/Video:** Streaming, recording.
- **Medical Imaging:** CT scans, Ultrasound.

## Criticism / Limitations
Processing introduces latency (delay). Heavy compression introduces artifacts (blocky video).

## Further Reading
- Oppenheim & Schafer, *Discrete-Time Signal Processing*
- Lyons, *Understanding Digital Signal Processing*
