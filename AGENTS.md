---
tags: [arena, documentation, meta, ai-instructions]
content_type: guide
audience: ai-agents
created: 2025-11-21
updated: 2025-11-23
---

# AGENTS: The Arena

LLM operators start here. Keep edits inside `The_Arena/`. Favor writing to Markdown files, linking with Obsidian wiki-link syntax, and preserving the campaign's theatrical, consequences-matter tone.

## Quickstart Context
- Baseline lore about the world can be found in `environment/the_empire.md` 
- Theme and Flavor in  `environment/flavor.md` 
- Mechanics to keep handy: `mechanics/panache.md`, `mechanics/crowds_favor.md`, `mechanics/last_stand.md`.
- for details about the physical arena itself, see `environment/the_arena.md`
- Cast snapshot: `players/characters.md`; key NPC sheets live in `npcs/`.
- When editing a folder, check its local `AGENTS.md` for scoped instructions.

## Campaign Snapshot (for light-weight context)
- Premise: D&D 2024 5e "core rules", 
- A repeating gladiatorial saga that blends spectacle with lethal advancement.
- Active roster rotates ~6 PCs, usually 4 per session.
- Themes: showmanship shapes fate; teamwork vs. solo glory; real stakes; fame and patronage as path to freedom.
- Tone: high-drama combat, announcer flair, crowd as character.

## Repo Map (load on demand)
- `sessions/` - session setups/encounters (narrative-first). See `sessions/AGENTS.md`.
- `mechanics/` - homebrew systems. See `mechanics/AGENTS.md`.
- `ideas/` - brainstorm seeds. See `ideas/AGENTS.md`.
- `npcs/` - NPC sheets. See `npcs/AGENTS.md`.
- `players/` - PC tracking. See `players/AGENTS.md`.

## Working Rules for All Agents
- Stay in-universe: crowd reactions, announcer interludes, and consequences should show up in scenes.
- Keep mechanics visible when they matter (Panache, Crowd’s Favor, Last Stand).
- Default to concise prose; add minimal headings and bullets for clarity.

## When to Use Claude Code Skill
- Multi-file rewrites or structural edits (session flow, mechanics refactors, link audits).
- Generating or updating scaffolds (new `AGENTS.md`, session templates, encounter stat blocks).
- Fast consistency passes (renaming links, aligning format) while keeping narrative tone intact.
