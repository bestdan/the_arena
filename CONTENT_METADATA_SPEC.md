# Content Metadata Specification for RAG Companion App

This document defines the metadata frontmatter format to be added to existing markdown files in The Arena repository to enable the RAG companion app's content visibility and access control system.

---

## Overview

Each markdown file that should be indexed by the RAG system needs YAML frontmatter at the top of the file. This frontmatter controls:
- **Visibility**: Who can access this content
- **Categorization**: Type and tags for better retrieval
- **Relationships**: Links to characters, sessions, and other entities

---

## Frontmatter Schema

### Required Fields

```yaml
---
visibility: public | player-specific | private
content_type: session | mechanic | npc | character | environment | idea
---
```

### Optional Fields (Recommended)

```yaml
---
# Visibility & Access
revealed: true | false                    # Has this been shown to players?
revealed_at: 2025-11-15                   # Date revealed (ISO format)

# Content Classification  
title: "Session 3: Thunder Above, Blood Below"
session_number: 3                         # For session content
tags: [combat, crowd-favor, aerial]       # Searchable tags

# Relationships
participants: [imwe, torgana, orion]      # Character IDs/names
related_npcs: [aurelius, father-crow]     # NPC references
related_mechanics: [panache, crowds-favor] # Mechanics used

# Metadata
author: bestdan                           # Content creator
created_at: 2025-11-10                    # Creation date
last_updated: 2025-11-15                  # Last modification
---
```

---

## Visibility Levels Explained

### `visibility: public`

**Who can access:** All authenticated users (players and GM)

**Use for:**
- Completed sessions that have been played and debriefed
- Published core mechanics (Panache, Crowd's Favor, Last Stand)
- Revealed NPC profiles
- General world/environment lore
- Active player character sheets

**Example:**
```yaml
---
visibility: public
revealed: true
revealed_at: 2025-11-15
content_type: session
session_number: 3
title: "Session 3: Thunder Above, Blood Below"
participants: [imwe, torgana, orion, gladiator]
tags: [combat, aerial, crowd-favor, storm-theme]
---
```

### `visibility: player-specific`

**Who can access:** Only players whose characters participated OR the GM

**Use for:**
- Session content with character-specific secrets or perspectives
- Private character notes or backstory elements
- Patron interactions specific to one character
- Personal injury/status updates

**Example:**
```yaml
---
visibility: player-specific
revealed: true
content_type: character
character_id: imwe
title: "Imwe - Private Notes"
tags: [backstory, patron-relationship, secrets]
---
```

### `visibility: private`

**Who can access:** GM only (never indexed in player-facing RAG)

**Use for:**
- Future session plans in `ideas/` folder
- Unrevealed plot twists and upcoming arcs
- GM-only NPC motivations and secrets
- Session content not yet played

**Example:**
```yaml
---
visibility: private
revealed: false
content_type: idea
title: "Lords of Lichdom - Future Boss Battle"
tags: [undead, bbeg, future-arc]
---
```

---

## Content Type Specifications

### `content_type: session`

**Files:** `sessions/session_*.md`

**Required Frontmatter:**
```yaml
---
visibility: public
revealed: true
content_type: session
session_number: 3
title: "Session 3: Thunder Above, Blood Below"
participants: [imwe, torgana, orion, gladiator]
---
```

**Optional but Recommended:**
```yaml
tags: [combat, crowd-favor, aerial, patron-appearance]
related_npcs: [aurelius, announcer]
related_mechanics: [panache, last-stand]
played_at: 2025-11-15
next_session: session_4_setup
---
```

### `content_type: mechanic`

**Files:** `mechanics/*.md`

**Required Frontmatter:**
```yaml
---
visibility: public
content_type: mechanic
title: "Panache Mechanics"
---
```

**Optional but Recommended:**
```yaml
tags: [combat, showmanship, risk-reward]
mechanic_category: core | optional | situational
introduced_in_session: 1
related_mechanics: [crowds-favor]
---
```

### `content_type: npc`

**Files:** `npcs/*.md`

**Required Frontmatter:**
```yaml
---
visibility: public | private
content_type: npc
title: "Patron Aurelius"
---
```

**Optional but Recommended:**
```yaml
npc_type: patron | announcer | rival | ally
revealed: true
first_appearance_session: 2
tags: [patron, noble, fire-magic]
related_characters: [imwe]  # Characters they've interacted with
---
```

### `content_type: character`

**Files:** `player_characters/*.md`

**Required Frontmatter:**
```yaml
---
visibility: public | player-specific
content_type: character
character_id: imwe
title: "Imwe - Human Fighter"
---
```

**Optional but Recommended:**
```yaml
player_name: "John Doe"  # Optional, links to user account
class: fighter
level: 3
status: active | injured | dead
fame_level: 2
sessions_participated: [1, 2, 3]
patron_relationships: [aurelius]
tags: [melee, defensive, tactical]
---
```

### `content_type: environment`

**Files:** `environment/*.md`

**Required Frontmatter:**
```yaml
---
visibility: public
content_type: environment
title: "The Empire - World Overview"
---
```

**Optional but Recommended:**
```yaml
tags: [lore, worldbuilding, tarsus]
related_locations: [arena, tarsus-city]
---
```

### `content_type: idea`

**Files:** `ideas/*.md`

**Required Frontmatter:**
```yaml
---
visibility: private
revealed: false
content_type: idea
title: "Cartographer's Curse - Arena Concept"
---
```

**Optional but Recommended:**
```yaml
tags: [maze, puzzle, trap-heavy]
difficulty_tier: deadly-for-level-5
encounter_type: boss | gauntlet | puzzle
status: brainstorm | drafted | ready | used
---
```

---

## Migration Strategy

### Step 1: Add Frontmatter to Existing Files

For each existing markdown file, add appropriate frontmatter based on its current status:

**Completed Sessions (already played):**
```yaml
---
visibility: public
revealed: true
content_type: session
session_number: 1
title: "Session 1: First Blood"
participants: [imwe, torgana, orion, gladiator, father-crow]
played_at: 2025-10-15
tags: [tutorial, boars, lizards, first-session]
---
```

**Core Mechanics (currently public):**
```yaml
---
visibility: public
content_type: mechanic
title: "Panache Mechanics"
tags: [combat, risk-reward]
---
```

**Future Ideas (not yet revealed):**
```yaml
---
visibility: private
revealed: false
content_type: idea
title: "Lords of Lichdom"
tags: [undead, boss-battle]
---
```

### Step 2: Validation Script

Create a simple script to validate frontmatter presence:

```javascript
// validate-frontmatter.js
const fs = require('fs');
const path = require('path');
const matter = require('gray-matter');

const REQUIRED_FIELDS = ['visibility', 'content_type'];
const VALID_VISIBILITY = ['public', 'player-specific', 'private'];
const VALID_CONTENT_TYPES = ['session', 'mechanic', 'npc', 'character', 'environment', 'idea'];

function validateFile(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const { data, isEmpty } = matter(content);
  
  if (isEmpty) {
    return { valid: false, error: 'Missing frontmatter' };
  }
  
  // Check required fields
  for (const field of REQUIRED_FIELDS) {
    if (!data[field]) {
      return { valid: false, error: `Missing required field: ${field}` };
    }
  }
  
  // Validate visibility value
  if (!VALID_VISIBILITY.includes(data.visibility)) {
    return { valid: false, error: `Invalid visibility: ${data.visibility}` };
  }
  
  // Validate content_type value
  if (!VALID_CONTENT_TYPES.includes(data.content_type)) {
    return { valid: false, error: `Invalid content_type: ${data.content_type}` };
  }
  
  return { valid: true };
}

// Usage: node validate-frontmatter.js
```

### Step 3: Update Guidelines in AGENTS.md

Add a section to the main AGENTS.md about metadata:

```markdown
## Content Metadata for RAG System

All markdown files should include YAML frontmatter for the RAG companion app.
See `CONTENT_METADATA_SPEC.md` for full specification.

Minimum required frontmatter:
```yaml
---
visibility: public | player-specific | private
content_type: session | mechanic | npc | character | environment | idea
---
```

When creating new content:
- Default `visibility: private` until content is revealed to players
- Set `revealed: true` and `revealed_at` when making content public
- Add relevant tags for better searchability
- Link participants and related entities
```

---

## Tag Taxonomy

### Session Tags
- **Combat Focus:** `combat`, `puzzle`, `social`, `exploration`
- **Mechanics:** `panache`, `crowds-favor`, `last-stand`, `blackmarket`
- **Theme:** `aerial`, `underground`, `water`, `urban`, `wildlands`
- **Tone:** `deadly`, `comedic`, `dramatic`, `horror`, `epic`
- **Special:** `patron-appearance`, `rivalry`, `betrayal`, `tournament`

### Mechanic Tags
- `core`, `optional`, `situational`
- `combat`, `social`, `downtime`
- `risk-reward`, `crowd-interaction`, `showmanship`

### NPC Tags
- **Role:** `patron`, `rival`, `ally`, `announcer`, `vendor`, `guard`
- **Type:** `noble`, `commoner`, `monster`, `authority`
- **Disposition:** `friendly`, `neutral`, `hostile`, `mysterious`

### Character Tags
- **Combat Style:** `melee`, `ranged`, `magic`, `support`, `tank`
- **Personality:** `bold`, `cautious`, `theatrical`, `tactical`, `reckless`
- **Status:** `active`, `injured`, `recovering`, `retired`, `deceased`

---

## Example Annotated Files

### Example 1: Completed Session

```markdown
---
visibility: public
revealed: true
revealed_at: 2025-11-15
content_type: session
session_number: 3
title: "Session 3: Thunder Above, Blood Below"
participants: [imwe, torgana, orion, gladiator]
tags: [combat, aerial, crowd-favor, storm-theme, deadly]
related_npcs: [aurelius, announcer]
related_mechanics: [panache, crowds-favor, last-stand]
played_at: 2025-11-15
---

The portcullis raises, thunder rumbles overhead...

[Rest of session content]
```

### Example 2: Core Mechanic

```markdown
---
visibility: public
content_type: mechanic
title: "Panache Mechanics"
tags: [core, combat, risk-reward, showmanship]
mechanic_category: core
introduced_in_session: 1
related_mechanics: [crowds-favor]
author: bestdan
created_at: 2025-10-01
---

When a combatant attempts an attack, check, or similar action...

[Rest of mechanic content]
```

### Example 3: Player Character

```markdown
---
visibility: public
content_type: character
character_id: imwe
title: "Imwe - Human Fighter"
player_name: "Alice"
class: fighter
subclass: battlemaster
level: 3
status: active
fame_level: 2
sessions_participated: [1, 2, 3]
patron_relationships: [aurelius]
tags: [melee, defensive, tactical, shield-specialist]
---

**Imwe** is a stoic human fighter from the northern provinces...

[Rest of character content]
```

### Example 4: Unrevealed Idea

```markdown
---
visibility: private
revealed: false
content_type: idea
title: "Lords of Lichdom - Epic Boss Battle"
tags: [undead, bbeg, high-level, multi-phase]
difficulty_tier: deadly-for-level-10
encounter_type: boss
status: brainstorm
target_session: future
---

The arena transforms into a necropolis...

[Rest of idea content - never indexed until revealed]
```

---

## Automated Frontmatter Generation

For bulk migration, here's a template generator based on file path:

```javascript
function generateFrontmatter(filePath) {
  const segments = filePath.split('/');
  const folder = segments[segments.length - 2];
  const filename = segments[segments.length - 1];
  
  const defaults = {
    sessions: {
      visibility: 'public',
      revealed: true,
      content_type: 'session',
      session_number: extractSessionNumber(filename),
      participants: [],  // Fill manually
      tags: []
    },
    mechanics: {
      visibility: 'public',
      content_type: 'mechanic',
      title: titleFromFilename(filename),
      tags: []
    },
    ideas: {
      visibility: 'private',
      revealed: false,
      content_type: 'idea',
      title: titleFromFilename(filename),
      status: 'brainstorm',
      tags: []
    },
    npcs: {
      visibility: 'public',  // Review manually
      content_type: 'npc',
      title: titleFromFilename(filename),
      tags: []
    },
    player_characters: {
      visibility: 'public',
      content_type: 'character',
      character_id: filename.replace('.md', ''),
      title: titleFromFilename(filename),
      tags: []
    },
    environment: {
      visibility: 'public',
      content_type: 'environment',
      title: titleFromFilename(filename),
      tags: []
    }
  };
  
  return defaults[folder] || { visibility: 'private', content_type: 'unknown' };
}
```

---

## RAG Ingestion Behavior by Visibility

| Visibility | Indexed in Vector DB? | Accessible to Players? | Accessible to GM? |
|------------|----------------------|------------------------|-------------------|
| `public` + `revealed: true` | ✅ Yes | ✅ Yes | ✅ Yes |
| `public` + `revealed: false` | ❌ No | ❌ No | ✅ Yes |
| `player-specific` + participant match | ✅ Yes (filtered) | ✅ Yes (if participant) | ✅ Yes |
| `player-specific` + no match | ❌ No | ❌ No | ✅ Yes |
| `private` (any `revealed` value) | ❌ No | ❌ No | ✅ Yes |

**Key Principles:**
- Default to `private` until explicitly revealed
- `revealed: true` is required for public visibility
- Player-specific content requires participant matching
- GM always has full access (separate query path)

---

## Future Enhancements

### Dynamic Visibility Transitions

```yaml
---
visibility: private
revealed: false
auto_reveal_after: 2025-12-01  # Automatically promote to public after date
auto_reveal_trigger: session_5_complete  # Or after certain event
---
```

### Partial Content Redaction

```yaml
---
visibility: public
revealed: true
redacted_sections:
  - heading: "Future Hooks"
    reason: "Contains unrevealed plot points"
  - heading: "GM Notes"
    reason: "Tactical information for GM only"
---
```

### Version History

```yaml
---
visibility: public
revealed: true
version: 2
changelog:
  - version: 2
    date: 2025-11-20
    changes: "Added aftermath section with patron reactions"
  - version: 1
    date: 2025-11-15
    changes: "Initial session write-up"
---
```

---

## Checklist for Content Creators

When creating or updating content:

- [ ] Add frontmatter to top of file
- [ ] Set `visibility` appropriately (default: `private`)
- [ ] Set `content_type` matching file location
- [ ] Add descriptive `title` (used in UI)
- [ ] Include relevant `tags` for searchability
- [ ] Link `participants` for session content
- [ ] Link `related_npcs` and `related_mechanics` where relevant
- [ ] Set `revealed: true` only when ready for players
- [ ] Update `revealed_at` date when publishing
- [ ] Validate frontmatter with script before commit

---

## Summary

This metadata specification enables the RAG companion app to provide intelligent, context-aware responses while maintaining strict content visibility controls. By consistently applying frontmatter to all markdown files, the system can:

1. **Filter content** by user access level
2. **Categorize content** for better retrieval
3. **Link related entities** for deeper context
4. **Track publication status** to prevent spoilers
5. **Enable rich querying** with tags and relationships

The specification is designed to be:
- **Lightweight**: Minimal required fields
- **Flexible**: Optional fields for enhanced functionality
- **Future-proof**: Extensible for new features
- **Developer-friendly**: Easy to validate and automate

---

**Document Version:** 1.0  
**Last Updated:** 2025-11-23  
**Related:** RAG_COMPANION_APP_DESIGN.md
