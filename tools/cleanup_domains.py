import os
import re

VALID_DOMAINS_FILE = "/home/kdos/Anvil/kdos-main/tools/valid-domains.txt"
CONTENT_DIR = "/home/kdos/Anvil/kdos-main/content/knowledge"

def load_valid_domains():
    with open(VALID_DOMAINS_FILE, 'r') as f:
        return set(line.strip() for line in f if line.strip())

def process_file(filepath, valid_domains):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    if not lines or lines[0].strip() != '---':
        return False

    try:
        frontmatter_end_idx = lines.index('---\n', 1)
    except ValueError:
        return False

    frontmatter = lines[1:frontmatter_end_idx]
    
    # Find domains section
    domains_start_idx = -1
    domains_end_idx = -1
    
    for i, line in enumerate(frontmatter):
        if line.strip().startswith('domains:'):
            domains_start_idx = i
            break
            
    if domains_start_idx == -1:
        return False

    # Determine end of domains section
    # It ends at the next line that is NOT indented (if multi-line) or just the same line (if inline)
    
    current_domains = []
    
    # Check for inline list
    inline_match = re.search(r'domains:\s*\[(.*?)\]', frontmatter[domains_start_idx])
    if inline_match:
        domains_end_idx = domains_start_idx + 1
        raw_domains = inline_match.group(1).split(',')
        current_domains = [d.strip().strip('"\'') for d in raw_domains if d.strip()]
    else:
        # Multi-line list
        # Look ahead for indented lines
        j = domains_start_idx + 1
        while j < len(frontmatter):
            line = frontmatter[j]
            if not line.strip(): # Skip empty lines
                j += 1
                continue
            if line.startswith(' ') or line.startswith('\t') or line.strip().startswith('-'):
                # It's an item
                # Extract value. Could be "- Item" or "- 'Item'" or "  - Item"
                val = line.strip().lstrip('-').strip().strip('"\'')
                if val:
                    current_domains.append(val)
                j += 1
            else:
                # New key
                break
        domains_end_idx = j

    # Filter domains
    new_domains = []
    has_changes = False
    
    # Check if we need to change anything
    # 1. Are there invalid domains?
    # 2. Is the format multi-line? (We want to standardize to inline)
    
    invalid_found = False
    for domain in current_domains:
        if domain in valid_domains:
            new_domains.append(domain)
        else:
            print(f"Removing invalid domain '{domain}' from {filepath}")
            invalid_found = True
            has_changes = True

    # Even if no invalid domains, if it was multi-line, we might want to standardize.
    # But strictly speaking, we only need to write if we change the content.
    # However, to be safe and consistent, let's rewrite if it was multi-line OR if we removed something.
    
    is_multiline = (domains_end_idx - domains_start_idx) > 1
    
    if invalid_found or is_multiline:
        # Construct new line
        new_domains_str = ', '.join([f'"{d}"' for d in new_domains])
        new_line = f'domains: [{new_domains_str}]\n'
        
        # Replace the block
        # We are modifying 'frontmatter' list
        # Remove old lines
        del frontmatter[domains_start_idx:domains_end_idx]
        # Insert new line
        frontmatter.insert(domains_start_idx, new_line)
        
        # Reconstruct file
        new_content = "---\n" + "".join(frontmatter) + "---\n" + "".join(lines[frontmatter_end_idx+1:])
        
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True

    return False

def main():
    valid_domains = load_valid_domains()
    print(f"Loaded {len(valid_domains)} valid domains.")
    
    count = 0
    for root, dirs, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                if process_file(filepath, valid_domains):
                    count += 1
                    
    print(f"Updated {count} files.")

if __name__ == "__main__":
    main()
