#!/usr/bin/env python3
"""
Build script for The Arena public documentation site.

This script:
1. Scans all markdown files in the repository
2. Filters files with `visibility: public` in frontmatter
3. Copies them to docs/ directory for MkDocs
4. Converts Obsidian [[wiki links]] to MkDocs format
5. Preserves directory structure
"""

import os
import re
import shutil
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any

# Repository root
REPO_ROOT = Path(__file__).parent.parent
DOCS_DIR = REPO_ROOT / "docs"
STATIC_DIR = REPO_ROOT / "static"

# Directories to exclude from scanning
EXCLUDE_DIRS = {".git", ".github", "node_modules", "docs", "scripts", "static"}

# Files to always exclude
EXCLUDE_FILES = {".gitignore", ".gitattributes"}


def parse_frontmatter(content: str) -> tuple[Optional[Dict[str, Any]], str]:
    """
    Parse YAML frontmatter from markdown content.
    
    Returns:
        tuple: (frontmatter_dict, content_without_frontmatter)
    """
    if not content.startswith("---"):
        return None, content
    
    try:
        # Find the end of frontmatter
        end_match = re.search(r'\n---\n', content[3:])
        if not end_match:
            return None, content
        
        end_pos = end_match.end() + 3
        frontmatter_text = content[3:end_pos-4]
        remaining_content = content[end_pos:]
        
        # Parse YAML
        frontmatter = yaml.safe_load(frontmatter_text)
        return frontmatter, remaining_content
    except yaml.YAMLError:
        return None, content


def build_file_index(docs_dir: Path) -> Dict[str, str]:
    """
    Build an index of all markdown files in docs directory.
    Returns a dict mapping filename -> relative path from docs root.
    
    Note: If multiple files have the same name, only the last one found
    will be indexed. Consider using unique filenames across directories.
    """
    file_index = {}
    if not docs_dir.exists():
        return file_index
    
    for md_file in docs_dir.rglob("*.md"):
        filename = md_file.name
        rel_path = md_file.relative_to(docs_dir)
        # Store as string for easy linking
        file_index[filename] = str(rel_path).replace('\\', '/')
    
    return file_index


def convert_wiki_links(content: str, current_file_path: Path, file_index: Dict[str, str]) -> str:
    """
    Convert Obsidian [[wiki links]] to MkDocs relative links.

    Handles:
    - [[filename]] -> [filename](path/to/filename.md) using file_index
    - [[folder/filename]] -> [filename](folder/filename.md)
    - [[filename|Display Text]] -> [Display Text](path/to/filename.md)

    Uses file_index to find the correct path for files.
    Calculates relative paths from current file location.
    """
    def replace_link(match):
        link_content = match.group(1)

        # Handle alias format [[link|alias]]
        if '|' in link_content:
            link, alias = link_content.split('|', 1)
            link = link.strip()
            alias = alias.strip()
        else:
            link = link_content.strip()
            alias = link.split('/')[-1]  # Use filename as display text

        # Ensure .md extension
        if not link.endswith('.md'):
            link = f"{link}.md"

        # If link already has a directory path, use it as-is
        if '/' in link:
            return f"[{alias}]({link})"

        # Look up in file index
        if link in file_index:
            target_path = file_index[link]
            target_path_obj = Path(target_path)

            # Get the directory of the current file (relative to docs root)
            current_dir = current_file_path.parent.relative_to(DOCS_DIR)
            target_dir = target_path_obj.parent

            # If target is in the same directory, use just the filename
            if current_dir == target_dir:
                return f"[{alias}]({target_path_obj.name})"

            # Otherwise, use relative path navigation
            # Count how many levels up we need to go
            up_levels = len(current_dir.parts)
            if up_levels == 0:
                # Current file is in root, use path as-is
                return f"[{alias}]({target_path})"
            else:
                # Build relative path with ../
                rel_parts = ['..'] * up_levels + list(target_path_obj.parts)
                rel_path = '/'.join(rel_parts)
                return f"[{alias}]({rel_path})"

        # Default to just the filename (may be a broken link if file not public)
        print(f"⚠ Warning: Could not resolve wiki link [[{link_content}]] - target may not be marked as public")
        return f"[{alias}]({link})"

    # Replace all [[...]] patterns
    content = re.sub(r'\[\[([^\]]+)\]\]', replace_link, content)
    return content


def is_public_file(filepath: Path) -> bool:
    """
    Check if a markdown file has visibility: public in frontmatter.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter, _ = parse_frontmatter(content)
        
        if frontmatter and isinstance(frontmatter, dict):
            visibility = frontmatter.get('visibility', '').lower()
            return visibility == 'public'
        
        return False
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False


def process_markdown_file(source_path: Path, docs_path: Path, file_index: Dict[str, str]):
    """
    Process a single markdown file: convert links and copy to docs.
    """
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert wiki links
        content = convert_wiki_links(content, source_path, file_index)
        
        # Ensure target directory exists
        docs_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write processed file
        with open(docs_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Processed: {source_path.relative_to(REPO_ROOT)} -> {docs_path.relative_to(REPO_ROOT)}")
    except Exception as e:
        print(f"✗ Error processing {source_path}: {e}")


def extract_referenced_assets(content: str) -> List[str]:
    """
    Extract image and asset references from markdown content.
    Returns list of relative paths to assets.
    """
    assets = []

    # Match markdown image syntax: ![alt](path)
    img_pattern = r'!\[.*?\]\(([^)]+)\)'
    for match in re.finditer(img_pattern, content):
        path = match.group(1)
        # Skip absolute URLs
        if not path.startswith(('http://', 'https://', '//')):
            assets.append(path)

    # Match HTML img tags: <img src="path">
    html_img_pattern = r'<img[^>]+src=["\']([^"\']+)["\']'
    for match in re.finditer(html_img_pattern, content):
        path = match.group(1)
        if not path.startswith(('http://', 'https://', '//')):
            assets.append(path)

    return assets


def build_docs():
    """
    Main build function: scan repo and build docs directory.
    """
    print("=" * 60)
    print("Building The Arena Public Documentation")
    print("=" * 60)

    # Clean docs directory
    if DOCS_DIR.exists():
        print(f"\nCleaning {DOCS_DIR}...")
        shutil.rmtree(DOCS_DIR)

    DOCS_DIR.mkdir(exist_ok=True)

    # Scan for markdown files
    print("\nScanning for public markdown files...")
    public_files = []

    for root, dirs, files in os.walk(REPO_ROOT):
        # Filter out excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        root_path = Path(root)

        for filename in files:
            if filename in EXCLUDE_FILES:
                continue

            if filename.endswith('.md'):
                filepath = root_path / filename

                if is_public_file(filepath):
                    public_files.append(filepath)
    
    if not public_files:
        print("\n⚠ No files with 'visibility: public' found!")
        print("Add 'visibility: public' to frontmatter of files you want to publish.")
        
        # Create a placeholder index
        index_content = """---
visibility: public
---

# The Arena - Public Documentation

Welcome to The Arena public documentation!

Currently, no documents are marked as public. To publish a document:

1. Add `visibility: public` to the frontmatter
2. Run the build script: `python scripts/build_docs.py`
3. Deploy the site

## About The Arena

A D&D 5e gladiatorial campaign set in Tarsus, where spectacle shapes survival 
and showmanship matters as much as steel.
"""
        index_path = DOCS_DIR / "index.md"
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        print(f"✓ Created placeholder: {index_path}")
        return
    
    print(f"\nFound {len(public_files)} public file(s)")
    
    # First pass: Copy files to docs directory (without link conversion)
    print("\nCopying files...")
    readme_found = False
    file_mappings = []  # Store (source, dest) tuples
    
    for source_path in public_files:
        # Calculate relative path from repo root
        rel_path = source_path.relative_to(REPO_ROOT)
        
        # Special handling for README.md - rename to index.md
        if rel_path.name == "README.md" and rel_path.parent == Path("."):
            docs_path = DOCS_DIR / "index.md"
            readme_found = True
        else:
            # Determine target path in docs
            docs_path = DOCS_DIR / rel_path
        
        # Ensure target directory exists
        docs_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Simple copy for now
        shutil.copy2(source_path, docs_path)
        file_mappings.append((source_path, docs_path))
        print(f"✓ Copied: {source_path.relative_to(REPO_ROOT)} -> {docs_path.relative_to(REPO_ROOT)}")
    
    # Build file index from copied files
    print("\nBuilding file index...")
    file_index = build_file_index(DOCS_DIR)
    print(f"Indexed {len(file_index)} file(s)")
    
    # Second pass: Process wiki links with file index
    print("\nConverting wiki links...")
    for source_path, docs_path in file_mappings:
        try:
            with open(docs_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Convert wiki links using file index (pass docs_path not source_path)
            content = convert_wiki_links(content, docs_path, file_index)

            # Write back
            with open(docs_path, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"✓ Processed links: {docs_path.relative_to(REPO_ROOT)}")
        except Exception as e:
            print(f"✗ Error processing links in {docs_path}: {e}")

    # Third pass: Copy referenced assets (images, etc.)
    print("\nCopying referenced assets...")
    assets_copied = 0
    for source_path, docs_path in file_mappings:
        try:
            with open(docs_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract asset references
            asset_refs = extract_referenced_assets(content)

            for asset_ref in asset_refs:
                # Resolve asset path relative to source file
                source_asset = (source_path.parent / asset_ref).resolve()

                # Skip if source doesn't exist
                if not source_asset.exists():
                    print(f"⚠ Warning: Asset not found: {source_asset.relative_to(REPO_ROOT)}")
                    continue

                # Target path in docs, maintaining relative structure
                target_asset = (docs_path.parent / asset_ref).resolve()

                # Ensure target directory exists
                target_asset.parent.mkdir(parents=True, exist_ok=True)

                # Copy asset
                shutil.copy2(source_asset, target_asset)
                print(f"✓ Copied asset: {source_asset.relative_to(REPO_ROOT)} -> {target_asset.relative_to(REPO_ROOT)}")
                assets_copied += 1

        except Exception as e:
            print(f"✗ Error copying assets for {docs_path}: {e}")

    if assets_copied > 0:
        print(f"\nCopied {assets_copied} asset(s)")
    
    # Create index.md if it doesn't exist and README wasn't public
    index_path = DOCS_DIR / "index.md"
    if not index_path.exists() and not readme_found:
        # Create a simple index
        index_content = """---
visibility: public
---

# The Arena - Public Documentation

Welcome to The Arena public documentation site.

Browse the navigation to explore public content.

## About The Arena

A D&D 5e gladiatorial campaign set in Tarsus, where spectacle shapes survival
and showmanship matters as much as steel.
"""
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        print(f"✓ Created index: {index_path}")

    # Copy static assets (CSS, JS, etc.)
    if STATIC_DIR.exists():
        print("\nCopying static assets...")
        for item in STATIC_DIR.rglob('*'):
            if item.is_file():
                # Calculate relative path from static dir
                rel_path = item.relative_to(STATIC_DIR)
                dest_path = DOCS_DIR / rel_path

                # Create parent directories
                dest_path.parent.mkdir(parents=True, exist_ok=True)

                # Copy file
                shutil.copy2(item, dest_path)
                print(f"✓ Copied static asset: {rel_path}")

    print("\n" + "=" * 60)
    print(f"Build complete! {len(public_files)} file(s) processed")
    print(f"Documentation ready in: {DOCS_DIR}")
    print("\nNext steps:")
    print("  1. Preview: mkdocs serve")
    print("  2. Build: mkdocs build")
    print("  3. Deploy: mkdocs gh-deploy")
    print("=" * 60)


if __name__ == "__main__":
    build_docs()
