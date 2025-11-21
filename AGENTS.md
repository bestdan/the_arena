# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is "The Arena" - a D&D 5e campaign set in a gladiatorial arena within Tarsus, the capital of an ancient, ever-expanding empire. The Arena serves as both entertainment and a refinery for heroes, taking criminals, prisoners of war, and volunteers and giving them a path to fame and freedom through combat.

This is a d&d "core rules" campaign. The general theme is for them to be combatants in an arena where they have to face new and harder challenges every week while having a hunger games style escalation and support from outside benefactors.

## Campaign Structure

**Player Setup:** Rotating cast of ~6 player characters with typically 4 active per session.

**Current Player Characters:**

- Imwe: Mony
- Torgana
- Orion Blackreef 
- Gladiator
- Father Crow 


## File Organization

- **Session Notes:** /episodes/ - Individual session write-ups
- **Campaign Intro:** `Intro.md` - World-building and campaign setup
- **Mechanics:** /mechanics/ - Custom homebrew systems
- **Character Tracking:** `Player Characters.md` - List of active PCs

## Custom Mechanics
I have created a few homebrew custom mechanics for The Arena with the intent to increase risk and dramatics. 

**Rolling with Panache**: 
/mechanics/panache-mechanic.md

**Crowd's Favor System**
/mechanics/crowds-favor-mechanic.md

**Last Stand**
/mechanics/last_stand.md

## Session Note Structure

Session notes follow this narrative format:

1. **Pre-session interactions** - Character development, NPC conversations, world-building
2. **Announcer dialogue** - Formatted in code blocks for dramatic framing
3. **Combat encounters** - Theatrical presentation with crowd reactions
4. **Post-combat aftermath** - Rewards, patron interest, reputation changes, consequences
5. **Between-session events** - Downtime activities leading to next session

### Announcer Dialogue Format

```
[Stage direction or crowd reaction]

"Announcer speech with dramatic flair..."

[Physical gestures or crowd response]
```

## Creating or brainstorming new session
When brainstorming ideas for new sessions: 

- add a new document in /ideas/ like `brainstorm_4.md`

For each session, come up with:
  - an overall hook or theme to the session
  - a description of how The Arena is rearranged or designed with environmental dangers, cover,
  etc
  - a deadly challenge-rated encounter for 4-6 players, including specific numbers and types of enemies,
  with a way to flex in case some players can't make it

## Key NPCs

- **Snak** - Gruff orc woman in leather armor vest. Manages new gladiators, provides equipment, rewards performance. Pragmatic, wants fighters to survive and succeed because dead fighters don't generate revenue. Has connections to get special equipment.

- **Merryn** - Elf woman archer. Joined Arena voluntarily for fame and glory. Loves the crowd and applause. Cutthroat and strategic: help her look good and she helps you survive; make her look bad and you become a liability. Skilled with bow.

- **Rohm** - Solid, thick-legged man with shoulder-length black hair. From horse-herding people of eastern steppes. POW protecting three young people (Tovo, Dec, Lira). Killed 12 soldiers before capture. Fierce protector, skilled with shield and spear.

- **Tovo, Dec, Lira** - Young people (16-18 years old) from the steppes under Rohm's protection. Families killed. Tovo is the oldest, Dec has a limp, Lira is youngest.

## Campaign Tone & Themes

- **High drama + tactical combat** - Every fight is a performance
- **Showmanship matters** - Style and flair affect crowd reaction and opportunities
- **Cooperation vs. glory** - Tension between teamwork and individual fame
- **Consequences are real** - NPCs die, patrons notice performance, reputation builds over time
- **Path to freedom** - Survivors with popularity can earn wealth, status, and freedom

## World-Building Notes

**The Empire:**

- Ancient and ever-present; no histories exist before it
- Living and dynamic, not decaying
- Grows steadily through diplomacy, then justified conquest
- Roads connect all territories, bringing goods and culture but erasing histories
- All who resist eventually end up in Tarsus

**Tarsus (Capital):**

- Where the Senate sits
- Heart of wealth, culture, theaters, universities, guilds
- Also processes "detritus" - criminals, traitors, POWs who won't submit

**The Arena:**

- Largest structure in Tarsus
- Not just combat, but refined theater with drama, plot arcs, betrayal, love
- Refines heroes from batches of fighters
- Survivors need fans and patrons to truly succeed
- Rich, comfortable life awaits successful gladiators

## Working in This Campaign

When creating or editing campaign content:

1. **Stay in The_Arena folder** - Don't reference or modify files outside this directory
2. **Maintain theatrical tone** - Arena combat is performance art, not just violence
3. **Track consequences** - Deaths, injuries, patron interest, reputation
4. **Use announcer framing** - Major moments get dramatic announcer commentary
5. **Remember the mechanics** - Panache and Crowd's Favor are central to gameplay
6. **Character relationships matter** - NPCs have motivations and remember PC actions
7. **Link related content** - Use Obsidian `[[wiki links]]` to connect NPCs, locations, sessions
8. Default to writing to new or existing \_.md files rather than responding in the UI directly.
