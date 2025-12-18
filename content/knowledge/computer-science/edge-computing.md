---
title: "Edge Computing"
slug: "edge-computing"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Computer Science"
  - "Networking"
tags:
  - "latency"
  - "distributed"
  - "iot"
  - "processing"
  - "cloud"
  - "bandwidth"
difficulty: "intermediate"
reading_time: 6
summary: >
  Edge computing is a distributed computing paradigm that brings computation and data storage closer to the sources of data. This is expected to improve response times and save bandwidth.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
The Cloud is great, but it's far away (physically). If you are a self-driving car, you can't wait 100 milliseconds for a server in Virginia to tell you to brake. You need the answer *now*. Edge Computing is moving the brain from the cloud to the device (the Edge).

## Core Idea
The core idea is **Proximity**. Speed of light is fast, but not infinite. By processing data right where it is created, you eliminate lag (latency).

## Formal Definition
A distributed computing paradigm that brings computation and data storage closer to the location where it is needed, to improve response times and save bandwidth.

## Intuition
-   **Cloud:** Sending your film to a lab to get developed. (High quality, slow).
-   **Edge:** Using a Polaroid camera. (Instant).

## Examples
-   **Self-Driving Cars:** They generate 1GB of data per second. They can't upload that to the cloud. They have a supercomputer in the trunk to process it instantly.
-   **Netflix:** They don't stream movies from California. They put "Edge Servers" inside your local ISP's building. The movie is physically only a few miles away from your house.
-   **Smart Cameras:** A security camera that recognizes faces *on the camera itself*, rather than sending the video to the cloud. This is faster and more private.

## Common Misconceptions
-   **It replaces the Cloud:** No, they work together. The Edge does the fast, real-time stuff. The Cloud does the heavy, long-term analysis. "Fog Computing" is the layer between them.

## Related Concepts
-   **5G:** The network that enables Edge Computing. It provides the high bandwidth needed to connect millions of edge devices.
-   **CDN (Content Delivery Network):** The original edge computing. Caching static files (images, CSS) all over the world.

## Applications
-   **AR/VR:** If you turn your head and the virtual world lags by even 20ms, you get motion sickness. Edge computing is required to render the graphics fast enough.

## Criticism / Limitations
-   **Maintenance:** It's easy to manage one giant data center. It's hard to manage 10,000 tiny servers scattered across a city.

## Further Reading
-   Satyanarayanan, Mahadev. *The Emergence of Edge Computing*.
