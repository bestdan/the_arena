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
