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

DOMAIN SELECTION RULES:
- Assign 1–3 domains maximum.
- Domains must come from KDOS Domain Taxonomy v1.0.
- Choose the discipline that would formally teach this topic.
- Do NOT invent new domains.

TAGGING RULES:
- Assign 5–12 tags.
- Use lowercase kebab-case.
- Prefer specific, timeless concepts.
- Do not repeat domains as tags.
- Do not invent meta-structure in tag names.
- Tags should represent concepts, methods, objects, schools, or applications.


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
  - "<domain-2>" # optional
  - "<domain-3>" # optional
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


FINAL SELF-CHECK (DO NOT OUTPUT RESULTS):
- Does the front matter match the schema exactly?
- Are there 1–3 valid domains?
- Are there 5–12 valid kebab-case tags?
- Are all required sections present, ordered, and non-empty?
- Does the summary describe the topic plainly and concretely?
- Is the tone encyclopedic and neutral?
If any answer is "no", revise internally before outputting.
