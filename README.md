# KDOS Workflow

This is the simplified workflow for managing the KDOS knowledge base.

## 1. Generate New Seed Ideas
Use the helper script to generate a prompt for new topics. This ensures you don't create duplicates.

```bash
python3 tools/generate_seed_prompt.py <Domain>
```
*Example:* `python3 tools/generate_seed_prompt.py Physics`

1.  Copy the output prompt.
2.  Paste it into your LLM (or give it to the agent).
3.  Save the resulting TOML to `tools/seeds/<domain>-seed-v<version>.toml`.

## 2. Generate Content
Use the agent to generate content from the seed file.

**Instruction to Agent:**
> "Generate content for [Domain] using the seed file `tools/seeds/<filename>.toml`."

The agent will:
1.  Read the seed file.
2.  Generate a Markdown file for each topic in `content/knowledge/<domain>/`.
3.  Use the standard KDOS template.

## 3. Validate & Deploy
1.  **Check:** Briefly review the generated files in `content/knowledge/`.
2.  **Commit:**
    ```bash
    git add .
    git commit -m "feat: add content for <domain>"
    git push
    ```
3.  **Deploy:** Cloudflare Pages will deploy automatically.

## 4. Maintenance
-   **Cleanup Domains:** If you suspect invalid domains have crept in:
    ```bash
    python3 tools/cleanup_domains.py
    ```
-   **Valid Domains List:** `tools/valid-domains.txt` is the source of truth.

---
**That's it.** No complex staging or manual copying required if you use the agent.
