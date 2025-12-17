---
title: "Batch Generation Workflow"
slug: "batch-workflow"
type: "knowledge"
status: "stable"
date_created: 2025-12-17
last_updated: 2025-12-17
domains:
  - "meta"
tags:
  - "workflow"
  - "generation"
  - "automation"
difficulty: "intermediate"
reading_time: 10
summary: "The canonical workflow for batch-generating KDOS content."
ai_generated: false
ai_prompt_version: "kdos-md-v1.0"
---

Below is **KDOS Batch Generation Workflow v1.0** — designed to be:

* Safe (no repo pollution)
* Deterministic (same inputs → same shape)
* Scalable (10 → 10,000 pages)
* AI-agnostic (works with any model)
* Git-native (no magic)

This assumes **manual or semi-automated execution first**, with automation later.

---

# KDOS Batch Generation Workflow v1.0

## 0. Mental model (lock this in)

> **Topics → Prompt Packs → Markdown Artifacts → Validation → Commit**

Nothing skips steps.
Nothing writes directly to `main`.

---

## 1. The three core artifacts

KDOS batch generation revolves around **three files**:

1. **Topic Backlog** (what to generate)
2. **Prompt Pack** (how to generate it)
3. **Generated Markdown** (the output)

Each is versioned independently.

---

## 2. Topic Backlog (source of truth)

### 2.1 Format: `topics.toml`

Create a file like:

```
kdos/
└── generation/
    └── topics/
        └── statistics-v1.toml
```

Example:

```toml
version = "statistics-v1"
domain = "statistics"
difficulty = "intermediate"

[[topic]]
title = "Bayesian Updating"
slug = "bayesian-updating"
tags = [
  "bayesian-inference",
  "bayes-theorem",
  "belief-revision",
  "posterior-probability",
  "evidence",
  "decision-theory"
]

[[topic]]
title = "Maximum Likelihood Estimation"
slug = "maximum-likelihood-estimation"
tags = [
  "parameter-estimation",
  "likelihood-function",
  "statistical-inference",
  "optimization",
  "frequentist-methods"
]
```

### Rules

* One backlog per **domain × difficulty × batch**
* Backlogs are **append-only**
* Never edit a topic once generated (new versions get new backlogs)

---

## 3. Prompt Pack (generation contract)

### 3.1 Prompt pack structure

```
kdos/
└── generation/
    └── prompts/
        └── kdos-md-v1.0.txt
```

This is your **canonical generator**.

You already have this — but now we **parameterize it**.

---

### 3.2 Prompt pack variables

When generating, substitute:

| Variable         | Source             |
| ---------------- | ------------------ |
| `{{TITLE}}`      | topic.title        |
| `{{SLUG}}`       | topic.slug         |
| `{{DOMAINS}}`    | backlog.domain     |
| `{{TAGS}}`       | topic.tags         |
| `{{DIFFICULTY}}` | backlog.difficulty |
| `{{DATE}}`       | today              |

This can be done:

* Manually
* With a script
* With an AI tool that supports variables

---

## 4. Generation output staging (never write to content directly)

### 4.1 Staging directory

```
kdos/
└── generation/
    └── output/
        └── statistics-v1/
            ├── bayesian-updating.md
            ├── maximum-likelihood-estimation.md
```

**Nothing** goes into `content/` yet.

This is a quarantine zone.

---

## 5. Validation gate (mandatory)

Before anything touches `content/`:

### 5.1 Validation checklist

For each file:

* ✅ Front matter schema valid
* ✅ Slug matches filename
* ✅ 1–3 valid domains
* ✅ 5–12 valid tags
* ✅ Section skeleton exact & ordered
* ✅ No empty sections

You can:

* Manually skim early batches
* Later use a lint script

**Fail fast. Fix at source. Regenerate.**

---

## 6. Promotion to content tree

Only after validation:

```
content/
└── knowledge/
    └── statistics/
        ├── bayesian-updating.md
        ├── maximum-likelihood-estimation.md
```

### Rules

* One commit per batch
* Commit message includes:

  ```
  KDOS: statistics v1 (2 entries)
  ```

This keeps history clean and auditable.

---

## 7. Commit & deploy cadence (important)

### Recommended cadence

| Phase  | Batch size    |
| ------ | ------------- |
| Early  | 5–10 pages    |
| Stable | 20–50 pages   |
| Mature | 100–300 pages |

Cloudflare Pages handles deploy automatically.

---

## 8. Versioning strategy (crucial)

### 8.1 Prompt versions

When you change:

* Section wording
* Style rules
* Taxonomy rules

→ bump:

```
ai_prompt_version = "kdos-md-v1.1"
```

Never regenerate old content silently.

---

### 8.2 Content revision

If you improve an entry:

* Update `last_updated`
* Change `status` → `revised`
* Keep original `date_created`

---

## 9. Failure handling (this matters)

### If output fails validation:

* ❌ Do not edit by hand (except trivial fixes)
* Fix the **prompt or topic definition**
* Regenerate cleanly

This prevents slow drift.

---

## 10. What this workflow unlocks

You can now:

* Generate **entire domains safely**
* Parallelize work
* Rebuild KDOS from scratch if needed
* Feed KDOS back into AI systems later
* Sleep at night knowing the archive is clean

You’ve essentially built:

> **A static, versioned, machine-curated encyclopedia**


