---
title: "Output Validation & Lint Rules"
slug: "output-validation-and-lint-rules"
type: "knowledge"
status: "stable"
date_created: 2025-12-17
last_updated: 2025-12-17
domains:
  - "meta"
tags:
  - "validation"
  - "linting"
  - "quality-control"
difficulty: "intermediate"
reading_time: 10
summary: "Rules for validating AI-generated KDOS content."
ai_generated: false
ai_prompt_version: "kdos-md-v1.0"
---

Excellent. We’ll now **close the loop** and make KDOS *self-defending*.

What follows is **KDOS AI Output Validation + Lint Rules v1.0** — this is what prevents entropy when you scale to thousands (or tens of thousands) of pages.

This layer turns KDOS from “AI-assisted writing” into a **deterministic publishing system**.

---

# KDOS AI Output Validation & Lint Rules v1.0

## Purpose (why this exists)

This system ensures that **every `.md` file** entering the KDOS archive:

* Is structurally valid
* Obeys taxonomy rules
* Is future-proof
* Can be regenerated safely
* Does not silently degrade quality

Think of this as **`go vet` for knowledge**.

---

## 1. Validation levels (mental model)

There are **three levels of validation**:

1. **Hard Fail (Reject)**
2. **Soft Fail (Warn)**
3. **Advisory (Improve Later)**

Only **Hard Fail** blocks publishing.

---

## 2. Hard Fail Rules (must reject output)

If **any** of these fail → do not commit the file.

### 2.1 Front matter schema validation

Required keys **must exist**:

```text
title
slug
type
status
date_created
last_updated
domains
tags
difficulty
reading_time
summary
ai_generated
ai_prompt_version
```

Rules:

* `type` must equal `"knowledge"`
* `status` ∈ {`draft`, `stable`, `revised`}
* `difficulty` ∈ {`beginner`, `intermediate`, `advanced`}
* `reading_time` must be integer > 0
* `ai_generated` must be boolean

---

### 2.2 Slug validation

* Must be kebab-case
* Must match filename
* Must be globally unique

Reject if:

```
slug != filename
```

---

### 2.3 Domain validation

Rules:

* 1–3 domains
* Domains must exist in **KDOS Domain Taxonomy v1.0**
* No invented domains

Reject if:

* `domains = []`
* `len(domains) > 3`
* Unknown domain present

---

### 2.4 Tag validation (structural)

Rules:

* 5–12 tags
* All lowercase
* Kebab-case
* No spaces
* No domain names

Reject if:

* `len(tags) < 5` or `> 12`
* Any tag violates format rules
* Any tag matches a domain

---

### 2.5 Section skeleton validation

The following headings **must appear exactly once and in order**:

```text
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
```

Reject if:

* Any section missing
* Any section renamed
* Any extra top-level sections added

---

### 2.6 Empty-section rule (hard)

Sections may be brief, but **cannot be empty**.

Minimum content per section:

* At least **1 sentence**
* OR explicit: `Not applicable.` + explanation

Reject empty headings.

---

## 3. Soft Fail Rules (warn, but allow publish)

These should trigger a warning, not rejection.

### 3.1 Overlapping tags

Warn if:

* Near-duplicates detected
  (`bayesian-update` vs `bayesian-updating`)
* Tags are overly generic
  (`method`, `system`, `thing`)

---

### 3.2 Weak summary

Warn if:

* Summary > 3 sentences
* Summary contains vague language:

  * “important”
  * “powerful”
  * “interesting”
  * “various”

---

### 3.3 Domain ambiguity

Warn if:

* Entry plausibly fits >3 domains
* Domains selected seem misaligned with content density

---

### 3.4 Missing internal links

Warn if:

* `Related Concepts` lists items already present in KDOS
* But no internal links are used

---

## 4. Advisory Rules (quality improvement)

These never block publishing.

### 4.1 Reading time mismatch

Warn if:

* Word count implies reading time off by >40%

---

### 4.2 Example density

Advise if:

* `Examples` section has only one example
* Topic is abstract and benefits from more

---

### 4.3 Criticism balance

Advise if:

* `Criticism / Limitations` is overly thin
* Or reads as apologetic rather than analytical

---

## 5. AI self-check block (extremely powerful)

Add this **at the end of generation prompts**:

```
FINAL SELF-CHECK (DO NOT OUTPUT RESULTS):
- Does the front matter match the schema exactly?
- Are there 1–3 valid domains?
- Are there 5–12 valid kebab-case tags?
- Are all required sections present, ordered, and non-empty?
- Does the summary describe the topic plainly and concretely?
- Is the tone encyclopedic and neutral?
If any answer is "no", revise internally before outputting.
```

This single block dramatically improves first-pass validity.

---

## 6. Optional: Simple lint script (pseudo-code)

You can implement this later in Python, Node, or Go.

```pseudo
parse_front_matter(md)
assert required_keys_present
assert slug == filename
assert domains ⊆ DOMAIN_LIST and 1 ≤ len(domains) ≤ 3
assert 5 ≤ len(tags) ≤ 12
assert all tags kebab-case
assert section_order_exact
assert no_empty_sections
```

Even a **100-line script** will catch 95% of failures.

---

## 7. Publish rule (important)

Only entries that pass **all Hard Fail rules** may be:

* Committed to `main`
* Deployed via Cloudflare
* Counted as “stable KDOS knowledge”

Drafts may exist locally, but **the repo is sacred**.

---

## 8. What this unlocks

With validation in place, you can now:

* Batch-generate safely
* Refactor content mechanically
* Re-run prompts without fear
* Eventually embed KDOS into AI systems confidently

You’ve now built:

* A schema
* An ontology
* A governance layer

This is no longer a “site”.

---

## Next recommended step (very high leverage)

👉 **Batch generation workflow**

* Topic list → prompt packs
* Rate-limited generation
* Validation gate
* Commit strategy

If you want, next we’ll design:

* A **topic backlog format**
* A **prompt pack system**
* A **safe batch-generation cadence**

Say **“Design KDOS batch generation workflow”** and we proceed.
