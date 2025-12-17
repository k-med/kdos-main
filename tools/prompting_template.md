You are generating a KDOS knowledge-base article for a Hugo + PaperMod site.

OUTPUT RULES (STRICT):
- Output Markdown ONLY.
- Include YAML front matter at the top, enclosed by --- lines.
- Use the exact front matter keys provided below (same spelling).
- Use the exact section headings provided below, in the same order.
- Do NOT omit any section. If a section is not applicable, write a brief "Not applicable." with one sentence explaining why.
- Tone: neutral, encyclopedic, dense with meaning, no hype, no emojis, no conversational filler.
- Prefer concrete definitions, clear distinctions, and compact examples.
- Use internal links where reasonable in Hugo format: [Some Topic](/knowledge/<domain>/<slug>/) only if you are confident about the slug; otherwise mention it without linking.
- Do not include any copyrighted text or long quotations.

FRONT MATTER TEMPLATE (fill in values):
---
title: "<TITLE>"
slug: "<kebab-case-slug>"
type: "knowledge"
status: "draft"
date_created: "<YYYY-MM-DD>"
last_updated: "<YYYY-MM-DD>"
domains:
  - "<domain-1>"
tags:
  - "<tag-1>"
difficulty: "<beginner|intermediate|advanced>"
reading_time: <integer minutes>
summary: >
  <1–2 sentence summary>
ai_generated: true
ai_prompt_version: "kdos-md-v1.0"
---

SECTION TEMPLATE (must follow exactly):
## Overview
## Core Idea
## Formal Definition (if applicable)
## Intuition
## Examples
## Common Misconceptions
## Related Concepts
## Applications
## Criticism / Limitations
## Further Reading

TOPIC:
<INSERT TOPIC>

TARGET DIFFICULTY:
<INSERT beginner|intermediate|advanced>

DOMAINS (1–3):
<INSERT domains>

TAGS (5–12):
<INSERT tags>

DATE (use today):
2025-12-17
