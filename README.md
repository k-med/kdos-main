# KDOS Content Production — Simplified Process Manual (v1.0)

This is the **exact operational loop** you should follow from now on.

---

## 0. One-time setup (already done)

You already have:

* Hugo + PaperMod configured
* Taxonomies locked
* Prompt template locked
* Validation rules locked

No more infrastructure work needed.

---

## 1. Decide what to generate

**You do this first, always.**

Create or choose a topic backlog, e.g.:

```
generation/topics/statistics-seed-v1.toml
```

This file defines:

* Topic titles
* Slugs
* Tags
* Domain(s)
* Difficulty

This is your **generation authority**.

---

## 2. Generate one KDOS entry (repeatable)

For **each topic** in the backlog:

### 2.1 Open a fresh AI prompt

Do **not** rely on long “continue” chains.

### 2.2 Paste in:

* The **prompting template**
* The **topic details** (title, slug, tags, domain, difficulty)

Ask:

> “Generate the KDOS knowledge entry for this topic. Output Markdown only.”

### 2.3 Receive Markdown output

The output should be:

* A complete `.md` file
* With YAML front matter
* With all required sections

---

## 3. Stage the file (important)

**Do NOT paste directly into `content/` yet.**

Save the file to:

```
generation/output/<batch-name>/<slug>.md
```

Example:

```
generation/output/statistics-seed-v1/bayesian-updating.md
```

This is your **quarantine zone**.

---

## 4. Validate (fast, but mandatory)

Open the `.md` file and confirm:

### Front matter

* All required keys present
* `slug == filename`
* `type = "knowledge"`
* 1–3 valid domains
* 5–12 valid tags (kebab-case)

### Body

* All required sections present
* Correct order
* No empty sections

If anything is wrong:

* ❌ Do not “patch” creatively
* Fix the prompt or topic definition
* Regenerate cleanly

---

## 5. Promote to live content

Once validated:

### 5.1 Move the file

From:

```
generation/output/<batch>/<slug>.md
```

To:

```
content/knowledge/<domain>/<slug>.md
```

Example:

```
content/knowledge/statistics/bayesian-updating.md
```

### 5.2 Commit

```
git add content/knowledge/statistics/bayesian-updating.md
git commit -m "KDOS: statistics seed v1 (bayesian-updating)"
git push
```

Cloudflare Pages deploys automatically.

---

## 6. Repeat in batches

Recommended rhythm:

| Phase     | Batch size    |
| --------- | ------------- |
| First run | 5–10 entries  |
| Stable    | 20–50 entries |
| Mature    | 100+ entries  |

One commit per batch keeps history clean.

---

## 7. When to use `hugo new` (rare)

Only use:

```
hugo new knowledge/<domain>/<slug>.md
```

When:

* You are writing **by hand**
* Or drafting experimental content
* Or creating meta pages

For AI-generated KDOS entries:

> **Never needed.**

---

## 8. The one rule that prevents chaos

> **AI outputs → staging → validation → content/**

Never skip staging.
Never write directly to `content/` without checking.

---

## TL;DR (print this)

1. Decide topics
2. Generate one `.md` per topic
3. Save to `generation/output/`
4. Validate
5. Move to `content/knowledge/<domain>/`
6. Commit & deploy

That’s it.

---

If you want, next I can:

* Generate your **first seed topic list**
* Generate your **first KDOS entry together**
* Or help you create a **tiny lint script** to automate validation

Just say which.
