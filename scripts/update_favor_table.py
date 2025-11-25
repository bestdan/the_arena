#!/usr/bin/env python3
"""
Auto-generate the Crowd's Favor table from YAML data file.

Usage:
    python scripts/update_favor_table.py

This script reads mechanics/crowds_favor_options.yaml and regenerates
the markdown table in mechanics/crowds_favor_mechanic.md.
"""

import re
import yaml
from pathlib import Path


def load_favor_options(data_file: Path) -> list[dict]:
    """Load favor options from YAML data file."""
    with open(data_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    return data.get('options', [])


def generate_table(favor_options: list[dict]) -> str:
    """Generate markdown table from favor options."""

    # Sort by cost, then by name
    sorted_options = sorted(favor_options, key=lambda x: (x['cost'], x['name']))

    # Build table
    lines = [
        "| Cost | Name | Category | Action | Effect |",
        "|------|------|----------|--------|--------|"
    ]

    for option in sorted_options:
        cost = option['cost']
        name = option['name']
        category = option['category']
        action = option['action']
        effect = option['effect']

        lines.append(f"| {cost} | {name} | {category} | {action} | {effect} |")

    return "\n".join(lines)


def update_favor_table(mechanic_file: Path, favor_options: list[dict]) -> None:
    """Update the Crowd's Favor table in the mechanics file."""

    # Read the file
    content = mechanic_file.read_text(encoding='utf-8')

    # Generate new table
    new_table = generate_table(favor_options)

    # Find and replace the existing table
    # Pattern matches from "## Spending Crowd's Favor" to the end of the table
    table_pattern = r'(## Spending Crowd\'s Favor\s*\n\s*\n)(.*?)(\n*$|\n*##)'

    def replacement(match):
        header = match.group(1)
        trailing = match.group(3) if match.group(3) else ''
        return f"{header}{new_table}{trailing}"

    new_content = re.sub(table_pattern, replacement, content, flags=re.DOTALL)

    # Write back
    mechanic_file.write_text(new_content, encoding='utf-8')
    print(f"✓ Updated table in {mechanic_file}")
    print(f"  {len(favor_options)} options processed")


def main():
    # Determine the repo root (assuming script is in scripts/ folder)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent

    # Paths to data file and mechanic file
    data_file = repo_root / "mechanics" / "crowds_favor_options.yaml"
    mechanic_file = repo_root / "mechanics" / "crowds_favor_mechanic.md"

    if not data_file.exists():
        print(f"Error: {data_file} not found")
        return 1

    if not mechanic_file.exists():
        print(f"Error: {mechanic_file} not found")
        return 1

    try:
        # Load favor options from data file
        favor_options = load_favor_options(data_file)
        if not favor_options:
            print("Error: No favor options found in data file")
            return 1

        # Update the mechanic file with the table
        update_favor_table(mechanic_file, favor_options)
        return 0
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
