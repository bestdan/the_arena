---
visibility: public
---

# Publishing Public Documentation

This guide explains how to publish markdown files from The Arena repository as a public website.

## Overview

The Arena uses **MkDocs Material** to generate a beautiful, searchable documentation site from markdown files. Only files marked with `visibility: public` in their frontmatter are published.

## Quick Start

### 1. Mark Files as Public

Add `visibility: public` to the frontmatter of any markdown file you want to publish:

```yaml
---
tags: [arena, mechanics, homebrew]
visibility: public
created: 2025-11-25
---

# Your Content Here
```

### 2. Preview Locally

```bash
# Install dependencies (first time only)
pip install -r requirements.txt

# Build the docs directory from public files
python scripts/build_docs.py

# Serve the site locally at http://127.0.0.1:8000
mkdocs serve
```

### 3. Deploy to GitHub Pages

The site automatically deploys when you push to the `main` branch. The GitHub Actions workflow:
1. Scans for files with `visibility: public`
2. Builds the documentation site
3. Deploys to GitHub Pages

**Manual deployment:**
```bash
mkdocs gh-deploy
```

## Features

### 🔍 Search
Full-text search is automatically enabled. Users can search across all published content.

### 📊 Sortable Tables
Markdown tables automatically support sorting by clicking column headers.

Example:
```markdown
| Name | Level | Status |
|------|-------|--------|
| Kael | 5     | Active |
| Lyra | 4     | Injured |
```

### 🔗 Wiki Links
Obsidian-style `[[wiki links]]` are automatically converted to proper markdown links.

Supported formats:
- `[[filename]]` - Links to another file
- `[[folder/filename]]` - Links with path
- `[[filename|Display Text]]` - Links with custom text

### 🎨 Dark/Light Mode
Users can toggle between dark and light themes.

### 📱 Responsive Design
The site works beautifully on mobile, tablet, and desktop.

## Directory Structure

```
the_arena/
├── mkdocs.yml              # MkDocs configuration
├── requirements.txt        # Python dependencies
├── scripts/
│   └── build_docs.py      # Build script to filter public files
├── docs/                   # Generated - contains public files (gitignored)
├── site/                   # Generated - built website (gitignored)
└── .github/workflows/
    └── deploy-docs.yml    # Automated deployment
```

## Configuration

### MkDocs Configuration (mkdocs.yml)

The `mkdocs.yml` file controls:
- Site name and description
- Theme and colors
- Navigation structure
- Search settings
- Markdown extensions
- Plugins

### Build Script (scripts/build_docs.py)

The build script:
1. Scans all `.md` files in the repository
2. Parses frontmatter to find `visibility: public`
3. Copies public files to `docs/` directory
4. Converts `[[wiki links]]` to markdown links
5. Preserves directory structure

## Workflow

### Adding New Public Content

1. **Create or edit markdown file** with frontmatter:
   ```yaml
   ---
   visibility: public
   tags: [relevant, tags]
   ---
   ```

2. **Test locally**:
   ```bash
   python scripts/build_docs.py
   mkdocs serve
   ```

3. **Commit and push**:
   ```bash
   git add .
   git commit -m "Add new public content"
   git push
   ```

4. **Site updates automatically** via GitHub Actions

### Making Content Private

Remove `visibility: public` from frontmatter or change it to anything else (e.g., `visibility: private`).

## Advanced Features

### Tags
Files with tags in frontmatter are automatically indexed. Users can browse by tag.

### Navigation
Navigation is auto-generated from the directory structure. Files are sorted alphabetically within each directory.

### Custom Styling
Edit `mkdocs.yml` to customize:
- Colors: `theme.palette.primary` and `theme.palette.accent`
- Features: `theme.features` list
- Logo and favicon: `theme.logo` and `theme.favicon`

## Deployment Options

### GitHub Pages (Default)
- **Free** hosting
- Automatic deployment via GitHub Actions
- Custom domain support
- SSL included
- URL: `https://bestdan.github.io/the_arena/`

### Netlify (Alternative)
1. Connect your GitHub repo to Netlify
2. Build command: `python scripts/build_docs.py && mkdocs build`
3. Publish directory: `site`
4. Automatic deployments on push

### Self-Hosted
Build the site and deploy the `site/` directory to any web server:
```bash
python scripts/build_docs.py
mkdocs build
# Deploy site/ directory to your server
```

## Troubleshooting

### No files found
- Ensure files have `visibility: public` in frontmatter
- Check frontmatter formatting (must be valid YAML)
- Run `python scripts/build_docs.py` to see what's found

### Links not working
- Use relative paths for wiki links
- Ensure linked files are also marked public
- Check the build script output for conversion results

### Build fails
- Check Python version (3.11+ recommended)
- Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
- Check `mkdocs.yml` for syntax errors

### Search not working
- Search requires JavaScript
- Check browser console for errors
- Ensure site is served (not just opened as files)

## Examples

### Example Public File

```yaml
---
tags: [arena, mechanics, homebrew]
visibility: public
mechanic_type: combat
status: active
created: 2025-11-25
---

# Panache Mechanics

Showmanship matters in The Arena...

See also: [[crowds_favor|Crowd's Favor]]
```

### Example Table with Sorting

```markdown
| Gladiator | Fame | Status | Patron |
|-----------|------|--------|--------|
| Kael Ironheart | 850 | Champion | House Vex |
| Lyra Swiftblade | 620 | Active | House Maric |
| Theron Gray | 340 | Injured | None |
```

## Best Practices

1. **Consistent frontmatter**: Use the same field names across files
2. **Descriptive tags**: Help users find related content
3. **Wiki links**: Link related documents for easy navigation
4. **Test locally**: Always preview before pushing
5. **Clear structure**: Organize files in logical directories

## Support

For issues or questions:
1. Check this documentation
2. Review the build script output
3. Check MkDocs Material documentation: https://squidfunk.github.io/mkdocs-material/
4. Open an issue in the repository
