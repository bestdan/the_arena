# Scripts

Automation scripts for The Arena campaign.

## Setup

Install dependencies:

```bash
pip3 install -r requirements.txt
```

## Available Scripts

### `update_favor_table.py`

Auto-generates the Crowd's Favor options table from a YAML data file.

**Usage:**
```bash
python3 scripts/update_favor_table.py
```

**What it does:**
- Reads favor options from `mechanics/crowds_favor_options.yaml`
- Regenerates the markdown table in `mechanics/crowds_favor.md`
- Automatically sorts by cost, then alphabetically by name
- Preserves all other content in the mechanics file

**Workflow:**
1. Edit `mechanics/crowds_favor_options.yaml` to add/modify/remove options
2. Run `python3 scripts/update_favor_table.py`
3. Table in the mechanics file is automatically updated

**Adding a new option:**

Edit `mechanics/crowds_favor_options.yaml`:
```yaml
options:
  # ... existing options ...
  - cost: 2
    name: New Move
    category: mobility
    action: bonus
    effect: "Description of what it does"
```

Then run `python3 scripts/update_favor_table.py` to regenerate the table.

**Benefits of separate data file:**
- Single source of truth for all favor options
- Cleaner mechanics file (no duplicated data in front matter)
- Easy to reuse data for other purposes (web apps, tools, etc.)
- Version control friendly (clear diffs when options change)

### `generate_favor_table.py`

Generates the interactive Crowd's Favor table for the docs site from YAML data.

**Usage:**
```bash
python3 scripts/generate_favor_table.py
```

**What it does:**
- Reads `mechanics/crowds_favor_options.yaml`
- Generates a markdown table with the `.favor-table` class
- Updates `docs/mechanics/crowds_favor.md`
- Sorts options by cost, then alphabetically by name

**When to run:**
- After adding/editing/removing entries in `crowds_favor_options.yaml`
- Before building the documentation site
- Can be added to a pre-commit hook or CI pipeline

**Interactive features (on the published site):**
- 🔍 **Search**: Filter by name, category, or effect text
- 📊 **Sort**: Click any column header to sort ascending/descending
- 🎯 **Filter**: Dropdown filters for Cost, Category, and Action type
- 📱 **Responsive**: Mobile-friendly layout with card view on small screens

**Technical Details:**

The interactive table system consists of:

1. **Data Source**: `mechanics/crowds_favor_options.yaml` - single source of truth
2. **Generator**: `scripts/generate_favor_table.py` - converts YAML to markdown
3. **Styling**: `docs/stylesheets/sortable-tables.css` - arena-themed styling
4. **Interactivity**: `docs/javascripts/sortable-tables.js` - filtering/sorting logic
5. **Configuration**: `mkdocs.yml` - includes CSS/JS in the build

The table uses the `.favor-table` class which triggers the JavaScript enhancement when the page loads.
