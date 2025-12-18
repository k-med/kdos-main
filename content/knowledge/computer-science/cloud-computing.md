---
title: "Cloud Computing"
slug: "cloud-computing"
type: "knowledge"
status: "draft"
date_created: "2025-12-18"
last_updated: "2025-12-18"
domains:
  - "Computer Science"
  - "Systems"
tags:
  - "virtualization"
  - "aws"
  - "azure"
  - "saas"
  - "infrastructure"
  - "scalability"
difficulty: "beginner"
reading_time: 6
summary: >
  Cloud computing is the on-demand availability of computer system resources, especially data storage (cloud storage) and computing power, without direct active management by the user. Large clouds often have functions distributed over multiple locations, each of which is a data center.
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

## Overview
"The Cloud" is just a metaphor for "Someone Else's Computer." Instead of buying a server and keeping it in your closet, you rent a server from Amazon or Google by the second. It changed the world because it made computing a utility, like electricity. You plug in and pay for what you use.

## Core Idea
The core idea is **Abstraction**. You don't care about the hardware. You don't care if the hard drive fails (they replace it). You just care about the service.

## Formal Definition
The delivery of computing services—including servers, storage, databases, networking, software, analytics, and intelligence—over the Internet.
Models:
-   **IaaS (Infrastructure as a Service):** Renting the raw hardware (EC2).
-   **PaaS (Platform as a Service):** Renting the tools to build apps (Heroku).
-   **SaaS (Software as a Service):** Renting the finished app (Gmail, Netflix).

## Intuition
-   **Old Way:** Building your own power plant to run your toaster.
-   **Cloud Way:** Plugging your toaster into the wall socket.

## Examples
-   **Netflix:** They don't own any data centers. They run entirely on AWS (Amazon Web Services). When everyone logs on Friday night, Netflix automatically rents more servers. When everyone goes to sleep, they return them. This is **Elasticity**.
-   **Dropbox:** You save a file on your laptop, and it magically appears on your phone. The file lives in the cloud (S3).
-   **Google Docs:** The software isn't on your computer; it's in the browser.

## Common Misconceptions
-   **It's in the sky:** It's in giant, windowless warehouses in Virginia and Oregon, filled with humming racks of servers and massive air conditioners.
-   **It's less secure:** Often, it's *more* secure. Amazon has better security engineers than your small business does.

## Related Concepts
-   **Serverless:** You don't even rent a server. You just upload a function of code. It runs for 100 milliseconds and shuts down. You pay $0.000001.
-   **Edge Computing:** Moving the cloud closer to the user (to the cell tower) to reduce lag.

## Applications
-   **Startups:** Uber and Airbnb could not exist without the cloud. They didn't need millions of dollars to buy servers; they just used a credit card.

## Criticism / Limitations
-   **Vendor Lock-in:** Once you build your app on AWS, it is very hard to move it to Microsoft Azure. You are stuck.
-   **Outages:** If AWS goes down (US-East-1), half the internet breaks.

## Further Reading
-   Carr, Nicholas. *The Big Switch: Rewiring the World, from Edison to Google*.
