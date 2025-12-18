# Batch Processing Workflow

## 1. Generating Seed Files (The 100-Topic Batches)
I have pre-generated the **prompts** for all 32 domains in `tools/seed_prompts/`.

**To generate the actual TOML seed files:**
Just ask me:
> "Generate the seed file for [Domain] using the saved prompt."

*I will read `tools/seed_prompts/[Domain]_prompt.txt` and generate the 100 topics.*

## 2. Generating Content (The "Easy Way")
Once you have seed files in `tools/seeds/`, you don't need to micromanage.

**The Command:**
> **"Process the pending seed files."**

**What I will do:**
1.  **Scan:** Look for `.toml` files in `tools/seeds/`.
2.  **Pick:** Select the first one (e.g., `physics-seed-v2.toml`).
3.  **Generate:** Create the Markdown content for all topics in that file.
4.  **Archive:** Move the processed `.toml` file to `tools/seeds/archive/`.
5.  **Repeat:** (If you ask me to continue).

## Summary
1.  **You:** "Generate seed file for Physics." -> **Me:** Creates `tools/seeds/physics-seed-v2.toml`.
2.  **You:** "Process pending seeds." -> **Me:** Generates content -> Moves seed to archive.
