# Generating New Seed Ideas

To generate new seed ideas for a domain without creating duplicates, use the `generate_seed_prompt.py` script.

## Usage

```bash
python3 tools/generate_seed_prompt.py <Domain> [-t "Theme"] [-n <Number>]
```

### Arguments
-   `Domain`: The target Domain (e.g., "Physics", "Military").
-   `-t`, `--theme`: (Optional) A specific theme or sub-topic to focus on (e.g., "Quantum Mechanics", "Tanks").
-   `-n`, `--number`: The number of topics to generate (default: 10).

### Examples

**1. General Physics topics (10):**
```bash
python3 tools/generate_seed_prompt.py Physics
```

**2. Specific Military theme (5):**
```bash
python3 tools/generate_seed_prompt.py Military -t "Tanks of the Soviet Union" -n 5
```

**3. Specific History theme (20):**
```bash
python3 tools/generate_seed_prompt.py History -t "The Renaissance" -n 20
```

## Workflow

1.  **Run the script.**
2.  **Copy the output prompt.**
3.  **Feed it to the AI.**
4.  **Save the output** to `tools/seeds/<domain>-seed-v<version>.toml`.
    *   *Note:* You can create multiple seed files (v1, v2, v3).
    *   *Tip:* Once a seed file is fully processed (content generated), move it to `tools/seeds/archive/` to keep your workspace clean. The script will still scan the archive to prevent duplicates.
