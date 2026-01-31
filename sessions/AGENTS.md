---
tags: [arena, documentation, meta, sessions]
content_type: instructions
audience: ai-agents
created: 2025-11-21
updated: 2025-11-21
---

# AGENTS: sessions/

Use this guide when drafting or revising session notes. Keep the Arena theatrical and consequence-heavy.

## Load This Context First
- `AGENTS.md` and `environment/the_empire.md` for world framing.
- Mechanics: `mechanics/panache.md`, `mechanics/crowds_favor.md`, `mechanics/last_stand.md`.
- Current cast: `players/characters.md`; add relevant `npcs/*.md` for featured characters. Pay attention to `status` of NPCs and do not include dead NPCs.
- Inspect the notes from the previous session, `session_x_notes.md` for deaths, plot points etc

## Organization
- create 5 files per session using the templates available at `@templates/`
  - `session_x_setup_players.md` which holds pre-session setup to be shared with the players - Snak's explanation of the session, advice. 
  - `session_x_setup_gm.md` which holds pre-session info for the game master. 
  - `session_x_game.md` holds details of how to run the sessions: npcs, enemies, environment changes etc
  - `session_x_notes.md` holds notes from the played session, actions taken favor granted, items taken, plot lines developed etc
  - `index.md` should just be links to each of the files, if they are public. Not summary.
  - `.pages` for the github index page to render correctly, just put the index, nothing more
  - `session_x_snak_shop.md`: follow the advices in @items/AGENTS.md
Within each template file, look for lua braces `{{}}` for content to fill in 


## Session Format (keep consistent)
1. Pre-game interactions: character moments, NPC conversations, world hooks.
2. Announcer dialogue: use comment blocks for hype. Be quick, do not overindulge in crowd commentary. 
3. Combat encounters: deadly for 3-6 PCs considering their level; spotlight crowd reactions and style.
4. Post-combat aftermath: rewards, patron interest, reputation shifts, injuries or deaths.
5. Between-session events: downtime that seeds the next setup.


## Writing Rules
- Keep the crowd and announcer present to reinforce spectacle.
- Call out when custom mechanics apply ([[panache|Panache]], [[crowds_favor|Crowd Favor]], [[last_stand|Last Stand]]).
- Track consequences and continuity (wounds, debts, patron favors). Consult previous sessions notes.
- Link named NPCs, locations, and mechanics using Obsidian wiki-link syntax.
- Aim for concise headings and bullets where it helps scanning; otherwise flow with narrative prose.

When writing NPC dialog, follow the rules in /sessions/npc_writing_rules.md

**Important **
- By default, new sessions should have `visibility: private` in front matter.
- Never link to files which do not have `visibility: public` in their front matter. 