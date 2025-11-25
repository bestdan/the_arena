#!/usr/bin/env python3
"""
Generate interactive Crowd's Favor table from YAML data.
This ensures the YAML is the single source of truth.
"""

import yaml
from pathlib import Path


def load_favor_options(yaml_path: Path) -> list[dict]:
    """Load favor options from YAML file."""
    with open(yaml_path, 'r') as f:
        data = yaml.safe_load(f)
    return data.get('options', [])


def generate_markdown_table(options: list[dict]) -> str:
    """Generate markdown table from favor options."""
    # Sort by cost, then by name
    sorted_options = sorted(options, key=lambda x: (x['cost'], x['name']))

    # Build simple markdown table (JavaScript will add interactivity)
    lines = [
        '| Cost | Name | Category | Action | Effect |',
        '|------|------|----------|--------|--------|'
    ]

    for opt in sorted_options:
        cost = opt['cost']
        name = opt['name']
        category = opt['category']
        action = opt['action']
        effect = opt['effect']

        # Escape pipes in effect text
        effect = effect.replace('|', '\\|')

        lines.append(f'| {cost} | {name} | {category} | {action} | {effect} |')

    return '\n'.join(lines)


def update_markdown_file(md_path: Path, yaml_path: Path):
    """Update the markdown file with the new table."""
    options = load_favor_options(yaml_path)
    table_markdown = generate_markdown_table(options)

    # Read existing file
    with open(md_path, 'r') as f:
        content = f.read()

    # Find the table section
    start_marker = '## Spending Crowd\'s Favor'

    if start_marker not in content:
        print(f"Warning: Could not find '{start_marker}' in {md_path}")
        return

    # Split at the marker
    before_table = content.split(start_marker)[0]

    # Check if there's content after the table (next ## heading)
    after_section = content.split(start_marker)[1]
    next_section_parts = after_section.split('\n## ', 1)

    # Build new content
    new_content = before_table + start_marker + '\n\n' + table_markdown

    if len(next_section_parts) > 1:
        # There's another section after the table
        new_content += '\n\n## ' + next_section_parts[1]

    # Write back
    with open(md_path, 'w') as f:
        f.write(new_content)

    print(f"✓ Updated {md_path} with {len(options)} favor options")


def main():
    """Main entry point."""
    repo_root = Path(__file__).parent.parent
    yaml_path = repo_root / 'mechanics' / 'crowds_favor_options.yaml'
    md_path = repo_root / 'docs' / 'mechanics' / 'crowds_favor.md'

    if not yaml_path.exists():
        print(f"Error: YAML file not found at {yaml_path}")
        return 1

    if not md_path.exists():
        print(f"Error: Markdown file not found at {md_path}")
        return 1

    update_markdown_file(md_path, yaml_path)
    return 0


if __name__ == '__main__':
    exit(main())
