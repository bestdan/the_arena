---
tags: [arena, documentation, meta, github]
content_type: instructions
audience: ai-agents
created: 2025-11-23
updated: 2025-11-23
---

# GitHub Copilot Instructions for The Arena

## Repository Overview
This is **The Arena**, a D&D 5e gladiatorial campaign set in Tarsus. The repository contains session notes, homebrew mechanics, NPCs, player characters, and brainstorming materials for a theatrical, high-stakes arena combat campaign.

## Campaign Context
- **System:** D&D 5e core rules with custom mechanics
- **Setting:** Gladiatorial arena in Tarsus where spectacle shapes fate
- **Theme:** Showmanship matters; teamwork vs. solo glory; real stakes with lethal consequences
- **Tone:** High-drama combat with announcer flair, crowd as active character
- **Active Roster:** ~6 PCs rotating, typically 4 per session
- **Path to Freedom:** Fame and patronage earned through arena performances

## Key Custom Mechanics
When suggesting code or content, be aware of these homebrew systems:
- **Panache** (`mechanics/panache.md`) - Showmanship and style matter in combat
- **Crowd's Favor** (`mechanics/crowds_favor.md`) - Audience reactions affect outcomes
- **Last Stand** (`mechanics/last_stand.md`) - Dramatic final moments with mechanical benefits

## Repository Structure
```
├── sessions/          # Full session setups and encounters (narrative-first)
├── ideas/            # Brainstorm seeds for future sessions
├── mechanics/        # Homebrew rule systems
├── npcs/             # NPC character sheets
├── player_characters/ # PC tracking and sheets
└── AGENTS.md         # Detailed instructions for AI agents (see below)
```

## Writing Style Guidelines
**Always maintain the theatrical, consequences-matter tone:**
- Use announcer-style interludes and dramatic flair
- Include crowd reactions as part of scenes
- Show real consequences (injuries, deaths, patron interest, reputation shifts)
- Write concisely with minimal headings; use bullets for clarity
- Use Obsidian `[[wiki links]]` for cross-references to mechanics and NPCs
- Keep mechanics visible when they matter to the narrative

### Example Announcer Block
```
[Crowd rises, banners snapping]

"Welcome back to the blood-soaked sands!"

[Trumpets blare; nobles lean forward]
```

## Content Creation Guidelines

### For Session Ideas (`ideas/`)
Include:
- Hook/theme: why this bout matters to crowd or patrons
- Arena layout: terrain, hazards, cover, moving parts
- Enemy roster: scaled for 4-6 PCs with flex options
- Crowd Favor hooks: how the audience can be swayed
- Announcer beats: dramatic moments to narrate
- GM tips: pacing, mechanics integration
- Aftermath seeds: patron interest, rumors, consequences

### For Session Notes (`sessions/`)
Structure should include:
1. Pre-session interactions (character moments, NPC conversations)
2. Announcer dialogue (use code blocks for hype)
3. Combat encounters (deadly for 4-6 PCs, spotlight style)
4. Post-combat aftermath (rewards, patrons, reputation, injuries/deaths)
5. Between-session events (downtime seeding next setup)

### For Mechanics (`mechanics/`)
- Prioritize clarity: trigger, effect, resolution, tracking
- Balance anchored in 5e core; risky but not opaque
- Include usage examples for edge cases
- Show crowd reaction/style integration
- Flag Panache/Crowd Favor hooks explicitly

## Important References
**Start here for detailed context:**
- `/AGENTS.md` - Main agent instructions and campaign snapshot
- Each subfolder has its own `AGENTS.md` with scoped instructions
- Load `environment/the_empire.md` for baseline lore and arena framing
- Check `player_characters/characters.md` for current cast

## Continuity Tracking
Always track and maintain:
- Injuries and deaths from previous sessions
- Patron relationships and debts
- Reputation shifts and crowd sentiment
- Fame levels and advancement toward freedom
- Outstanding wagers or sponsorships

## Link Format
Use Obsidian-style wiki links: `[[filename]]` or `[[folder/filename]]`
Examples: `[[panache]]`, `[[npcs/patron_name]]`, `[[Crowd's Favor]]`

## Code Suggestions
When suggesting file edits or new content:
- Stay in-universe with dramatic, theatrical language
- Reference existing mechanics rather than creating new ones
- Maintain consistency with established NPCs and world details
- Ensure deadly but fair balance (this is 5e with stakes)
- Show consequences visibly in the narrative

---

For comprehensive context and folder-specific rules, always reference the local `AGENTS.md` files throughout the repository.
