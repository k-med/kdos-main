---
title: "Tagging Rules"
slug: "tagging-rules"
type: "knowledge"
status: "stable"
date_created: 2025-12-17
last_updated: 2025-12-17
domains:
  - "meta"
tags:
  - "tagging"
  - "ontology"
  - "rules"
difficulty: "intermediate"
reading_time: 10
summary: "Rules and ontology for tagging KDOS entries."
ai_generated: false
ai_prompt_version: "kdos-md-v1.0"
---

Excellent. This is the **precision layer** of KDOS.
If domains are the *skeleton*, **tags are the nervous system**.

Below is **KDOS Tag Ontology + Tagging Rules v1.0**, designed to:

* Stay flexible without becoming chaotic
* Be AI-assignable with high accuracy
* Support search, cross-linking, synthesis, and future embeddings
* Scale to **hundreds of thousands of tags** without rot

---

# KDOS Tag Ontology & Tagging Rules v1.0

## 0. Mental model (lock this in)

* **Domain** = *discipline*
* **Tag** = *concept, object, method, school, or context*

If a domain answers *“what academic field?”*
a tag answers *“what specifically?”*

---

## 1. Tag categories (implicit, not stored)

Tags themselves are **flat strings**.
But conceptually, they fall into categories — this helps AI choose well.

### A. Conceptual tags

Abstract ideas and constructs.

Examples:

* probability
* causation
* entropy
* rationality
* emergence

---

### B. Method / technique tags

How something is done.

Examples:

* bayesian-inference
* monte-carlo
* regression
* optimization
* meditation

---

### C. Object / entity tags

Concrete or named things.

Examples:

* fourier-transform
* black-scholes
* newtonian-mechanics
* dna

---

### D. School / framework tags

Named traditions or paradigms.

Examples:

* stoicism
* keynesianism
* logical-positivism
* behaviorism

---

### E. Context / application tags

Where or why something is used.

Examples:

* trading
* clinical
* education
* policy
* engineering-design

---

### F. Meta tags

About knowledge itself.

Examples:

* methodology
* ontology
* epistemic-risk
* taxonomy

⚠️ **Do NOT encode category into the tag string.**
The category is *conceptual*, not structural.

---

## 2. Tag formatting rules (strict)

These rules are **non-negotiable**.

### 2.1 Canonical format

* lowercase
* kebab-case
* ASCII only
* no punctuation except `-`

✅ Good:

```
bayesian-inference
signal-processing
epistemic-uncertainty
```

❌ Bad:

```
Bayesian Inference
signal_processing
epistemic/uncertainty
```

---

### 2.2 Tag length

* Prefer **1–3 words**
* Avoid sentence-like tags

✅ `decision-theory`
❌ `how-to-make-better-decisions`

---

### 2.3 Plurals

* Use **singular** unless the plural is standard

✅ `derivative`
❌ `derivatives` (unless referring specifically to plural instruments)

---

## 3. Tag count per entry (important)

Each KDOS entry must have:

* **Minimum:** 5 tags
* **Maximum:** 12 tags
* **Ideal:** 7–10 tags

This ensures:

* Enough cross-linking
* No tag spam
* Consistent AI behavior

---

## 4. Tag scope rules (very important)

### 4.1 Avoid domain leakage

Do **not** restate domains as tags.

If domain = `statistics`, do NOT tag:

* statistics
* statistical-methods

Tags should be *below* the domain layer.

---

### 4.2 Prefer specific over general

Always choose the **most specific stable concept**.

Prefer:

* `bayesian-updating`
  over:
* `probability`

Use both only if:

* Both are genuinely central

---

### 4.3 Timelessness test

Ask: *Will this tag still make sense in 20 years?*

Good:

* `bayesian-inference`
* `stoicism`

Bad:

* `chatgpt`
* `latest-research`

---

## 5. Special tag classes (allowed)

These are explicitly allowed and encouraged.

### 5.1 Person tags

Format:

```
person-firstname-lastname
```

Example:

* `person-thomas-bayes`
* `person-aristotle`

Use only when the person is central.

---

### 5.2 Text / work tags

Format:

```
work-title-kebab
```

Example:

* `work-nicomachean-ethics`
* `work-principia-mathematica`

---

### 5.3 Formal object tags

For equations, laws, or theorems:

Examples:

* `bayes-theorem`
* `noether-theorem`
* `shannon-entropy`

---

## 6. Disallowed tags (hard rules)

Never use:

* Domain names (`mathematics`, `philosophy`)
* Content type (`article`, `post`, `note`)
* Quality judgements (`important`, `basic`)
* Time-relative tags (`modern`, `recent`)
* Platform names (`youtube`, `twitter`)

---

## 7. AI tagging rules (drop-in block)

Include this verbatim in generation prompts:

```
TAGGING RULES:
- Assign 5–12 tags.
- Use lowercase kebab-case.
- Prefer specific, timeless concepts.
- Do not repeat domains as tags.
- Do not invent meta-structure in tag names.
- Tags should represent concepts, methods, objects, schools, or applications.
```

---

## 8. Example: correct tagging

**Topic:** Bayesian Updating
**Domains:** statistics, epistemology

```toml
tags = [
  "bayesian-inference",
  "bayes-theorem",
  "prior-belief",
  "posterior-probability",
  "epistemic-uncertainty",
  "belief-revision",
  "decision-theory",
  "evidence"
]
```

This is *excellent* KDOS tagging.

---

## 9. Optional: Tag governance (future-proofing)

Later, you may add:

* `tags/_index.md` explaining tag rules
* A script that:

  * Normalizes synonyms
  * Flags near-duplicates (`bayesian-update` vs `bayesian-updating`)
* A “preferred tag list” (soft guidance, not enforcement)

But **do not over-engineer now**.

---