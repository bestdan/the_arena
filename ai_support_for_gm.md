
## AI Support for GMs

This repository is designed to work seamlessly with AI assistants (Claude, GitHub Copilot, etc.) for brainstorming and session management.

### Brainstorming New Encounters

The `ideas/` folder contains 30+ encounter concepts ready to be developed into full sessions. Each idea includes:
- Arena layout and terrain features
- Enemy rosters with scaling options
- Crowd hooks and announcer moments
- Aftermath seeds for patron interest

AI agents can help:
- Generate new encounter concepts following the established format
- Develop ideas into full session write-ups with stat blocks
- Create announcer dialogue and crowd reaction beats
- Design terrain features and hazards that encourage dramatic moments

### Running Sessions

AI support for active gameplay:
- Quick NPC dialogue generation in the campaign's theatrical voice
- On-the-fly encounter adjustments based on party composition
- Patron interaction and political intrigue development
- Tracking injuries, reputation, and continuity between sessions

### Repository Structure

```
├── sessions/          # Full session setups and encounters (narrative-first)
├── ideas/            # Brainstorm seeds for future sessions
├── mechanics/        # Homebrew rule systems
├── npcs/             # NPC character sheets
├── players/ # PC tracking and sheets
├── environment/      # World lore and arena details
└── AGENTS.md         # Detailed instructions for AI assistants
```

Each folder has its own `AGENTS.md` with specialized instructions for that content type, ensuring AI assistants maintain consistency in tone, mechanics, and campaign continuity.

### Getting Started with AI Support

1. **Load context**: Start with `/AGENTS.md` plus `environment/the_empire.md` for baseline understanding
2. **Check mechanics**: Reference the three core homebrew systems for integration opportunities
3. **Maintain tone**: Keep the theatrical, announcer-style voice and show consequences visibly
4. **Track continuity**: Injuries, deaths, patron relationships, and reputation matter across sessions
5. **Use wiki links**: Connect content with Obsidian-style wiki links for easy navigation

The campaign is built for collaboration between human creativity and AI assistance, letting GMs focus on player interactions while AI handles content generation, consistency checks, and rapid iteration on encounter design.