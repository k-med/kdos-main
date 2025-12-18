import os
import re
import sys
import glob
import argparse

CONTENT_DIR = "/home/kdos/Anvil/kdos-main/content/knowledge"
SEEDS_DIR = "/home/kdos/Anvil/kdos-main/tools/seeds"
ARCHIVE_DIR = "/home/kdos/Anvil/kdos-main/tools/seeds/archive"
VALID_DOMAINS_FILE = "/home/kdos/Anvil/kdos-main/tools/valid-domains.txt"

def load_valid_domains():
    with open(VALID_DOMAINS_FILE, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def get_existing_titles_in_domain(target_domain):
    titles = set()
    target_domain_lower = target_domain.lower()
    
    # 1. Scan Content
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, 'r') as f:
                    content = f.read()
                    
                # Extract frontmatter
                fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
                if fm_match:
                    fm = fm_match.group(1)
                    
                    # Extract Title
                    title_match = re.search(r'title:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
                    if not title_match:
                        continue
                    title = title_match.group(1)
                    
                    # Extract Domains
                    domains = []
                    # Try inline first
                    inline_match = re.search(r'domains:\s*\[(.*?)\]', fm)
                    if inline_match:
                        d_str = inline_match.group(1)
                        domains = [d.strip().strip('"\'') for d in d_str.split(',') if d.strip()]
                    else:
                        # Try multiline
                        lines = fm.split('\n')
                        in_domains = False
                        for line in lines:
                            if line.strip().startswith('domains:'):
                                in_domains = True
                                continue
                            if in_domains:
                                if line.strip().startswith('-'):
                                    val = line.strip().lstrip('-').strip().strip('"\'')
                                    domains.append(val)
                                elif ':' in line: # New key
                                    break
                    
                    # Check if file belongs to target domain
                    if target_domain_lower in [d.lower() for d in domains]:
                        titles.add(title)

    # 2. Scan Seeds (Active and Archive)
    seed_files = glob.glob(os.path.join(SEEDS_DIR, "*.toml")) + glob.glob(os.path.join(ARCHIVE_DIR, "*.toml"))
    
    for file in seed_files:
        with open(file, 'r') as f:
            content = f.read()
            
        blocks = content.split('[[topics]]')
        for block in blocks[1:]: 
            # Extract topic
            t_match = re.search(r'topic\s*=\s*["\'](.*?)["\']', block)
            if not t_match:
                continue
            topic = t_match.group(1)
            
            # Extract domains
            domains = []
            d_match = re.search(r'domains\s*=\s*\[(.*?)\]', block)
            if d_match:
                d_str = d_match.group(1)
                domains = [d.strip().strip('"\'') for d in d_str.split(',') if d.strip()]
                
            if target_domain_lower in [d.lower() for d in domains]:
                titles.add(topic)
                    
    return sorted(list(titles))

def main():
    parser = argparse.ArgumentParser(description="Generate a prompt for creating new seed topics.")
    parser.add_argument("domain", help="The target Domain (e.g. 'Physics').")
    parser.add_argument("-t", "--theme", help="Optional specific theme (e.g. 'Quantum Mechanics').")
    parser.add_argument("-n", "--number", type=int, default=10, help="Number of topics to generate (default: 10).")
    
    args = parser.parse_args()
    
    valid_domains = load_valid_domains()
    
    # Validate domain roughly (case-insensitive check)
    if args.domain.lower() not in [d.lower() for d in valid_domains]:
        print(f"WARNING: '{args.domain}' is not in the valid-domains.txt list.")
        print("Valid domains are:")
        print(", ".join(valid_domains))
        print("-" * 40)

    existing = get_existing_titles_in_domain(args.domain)
    
    print(f"--- PROMPT FOR {args.domain.upper()} ---")
    
    if args.theme:
        print(f"I need to generate {args.number} new seed topics for the domain '{args.domain}', specifically focusing on the theme: '{args.theme}'.")
    else:
        print(f"I need to generate {args.number} new seed topics for the domain '{args.domain}'.")
        
    print(f"Here is the list of ALL topics that ALREADY EXIST in '{args.domain}' (do not generate these):")
    print("```")
    for t in existing:
        print(f"- {t}")
    print("```")
    
    if args.theme:
        print(f"\nPlease generate {args.number} NEW, distinct topics for '{args.domain}' related to '{args.theme}' that are not in the list above.")
    else:
        print(f"\nPlease generate {args.number} NEW, distinct topics for '{args.domain}' that are not in the list above.")
    
    print("\nCRITICAL INSTRUCTION FOR BREADTH & HOMOGENEITY:")
    print("- Span the WIDEST possible range within this theme/domain.")
    print("- Distribute the topics evenly to cover different aspects (e.g., different eras, different types, different theories).")
    print("- Avoid clustering around a single sub-topic.")
    print("- Ensure maximum distinctness between topics to prevent information overlap.")
    
    print("\nCRITICAL: You must ONLY use domains from the following allowed list:")
    print("```")
    print(", ".join(valid_domains))
    print("```")
    
    print("\nFormat the output as a TOML file following this schema:")
    print("""
[[topics]]
topic = "Topic Name"
difficulty = "beginner" # or intermediate, advanced
domains = ["Domain", "Related Domain"] # MUST be from the allowed list above
tags = ["tag1", "tag2", "tag3"]
""")

if __name__ == "__main__":
    main()
