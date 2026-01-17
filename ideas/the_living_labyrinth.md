---
tags: [arena, encounter-idea, cooperation, puzzle, shifting-walls, memory, environmental]
encounter_type: objective
party_size: "3-5"
level_range: "5-7"
difficulty: deadly
mechanics: [crowds-favor, panache]
status: ready
created: 2026-01-17
---
# The Living Labyrinth

- **Hook:** Stone walls rise and fall from the arena floor every 30 seconds, creating an ever-shifting maze. Exit portals appear briefly in different locations, but only the correct portal (marked by riddle clues) leads to freedom. The others? Death traps. Meanwhile, hunters stalk the corridors. Can they map the pattern, solve the riddles, and escape before the walls crush them—or the hunters do?
- **Party:** 3-5 PCs. Tests memory, spatial reasoning, communication under pressure, and combat in confined spaces. The maze "learns" from their movements.

## Arena Layout

- Square arena (100 feet × 100 feet) divided into a 5×5 grid (each cell 20×20 feet).
- **Rising Walls:** Stone walls rise from the floor (10 feet tall) every round, creating a new maze pattern.
- **Wall Cycle:** Every 2 rounds on initiative count 20, walls SINK into floor (all paths open briefly for 6 seconds). Then NEW walls rise in different configuration.
- **Three Patterns Repeat:** Maze rotates through Pattern A → Pattern B → Pattern C → Pattern A (each pattern lasts 2 rounds, then shifts).
- **Central Chamber:** One cell (center of grid, position C3) never has walls—always open, provides sanctuary but no strategic value.
- **Exit Portals:** Three shimmering portals appear randomly during wall cycles (positions marked by glowing runes on floor).
  - **True Exit:** Leads to victory (must be identified via riddle).
  - **False Exits (2):** Lead to death traps (fire, spikes, drowning chamber).
- **Vision:** Walls are opaque stone—can't see through them. Only hear sounds from adjacent cells.

## Wall Patterns (Repeating Cycle)

### Pattern A - The Spiral (Rounds 1-2, 7-8, 13-14)
- Walls form a spiral from outer edge to center.
- Longest continuous path, but forces PCs to circle toward center.
- **Exit Portals:** Appear in A1 (false-fire), C5 (false-spikes), E3 (TRUE).

### Pattern B - The Cross (Rounds 3-4, 9-10, 15-16)
- Walls form a large cross shape, dividing arena into quadrants.
- Creates four isolated sections; PCs may be separated.
- **Exit Portals:** Appear in B2 (TRUE), D4 (false-spikes), E1 (false-fire).

### Pattern C - The Labyrinth (Rounds 5-6, 11-12, 17-18)
- Complex maze with multiple dead ends and loops.
- Most confusing pattern; easy to get lost.
- **Exit Portals:** Appear in A5 (false-drowning), C1 (false-fire), D5 (TRUE).

### Wall Transition (Initiative 20, even rounds)
- All walls SINK into floor simultaneously (6-second window).
- PCs have one turn to reposition freely before NEW walls rise.
- Enemies use this to reposition and ambush.
- Announcer shouts: "THE MAZE SHIFTS! RUN!"

## Riddle Clues (Identify True Exit)

**Three stone pillars** in central chamber (C3) each bear one riddle line (can be read when PCs reach center):

1. "Seek the door that faces rising light" (East side—columns 5)
2. "Where walls embrace but do not cage" (Positions adjacent to center or open areas)
3. "The path that does not burn or pierce, but breathes" (Not fire/spikes—implies air/breathing = true exit)

**Combined Meaning:**
- **Pattern A:** True exit at E3 (East side, open spiral, safe passage).
- **Pattern B:** True exit at B2 (West of center, but it's the "breathing" one that doesn't trap).
- **Pattern C:** True exit at D5 (East edge, adjacent to open path).

**Clue Distribution:**
- Pillar 1 (North side of C3): "Seek the door that faces rising light"
- Pillar 2 (South side of C3): "Where walls embrace but do not cage"
- Pillar 3 (East side of C3): "The path that does not burn or pierce, but breathes"

PCs must reach center, read all three clues, remember them, navigate to correct portal during its pattern phase.

## False Exit Consequences

**Fire Portal:**
- Stepping through = teleported to 10×10 burning chamber (walls of fire).
- Takes 4d10 fire damage immediately, 2d10 fire damage at start of each turn.
- Can escape by succeeding DC 15 Strength check (force way back through portal) or having ally pull them out (athletics check).
- Chamber visible to crowd; dramatic spectacle.

**Spike Portal:**
- Stepping through = teleported to 10×10 spike pit.
- Falls onto spikes: 6d6 piercing damage, impaled (restrained, DC 16 Athletics to pull free, takes 2d6 piercing each round impaled).
- Can be rescued by ally who enters portal and helps (two-person Athletics check DC 13).

**Drowning Portal (Pattern C only):**
- Stepping through = teleported to flooding chamber (water rapidly filling).
- DC 14 Athletics to swim, must hold breath (Con rounds), 1d10 bludgeoning from water pressure each round.
- Chamber has one-way valve—can't re-enter portal from inside.
- Must be rescued by allies destroying the portal from outside (AC 15, 50 HP) or waiting for pattern shift (portal disappears, PC ejected back to arena at 0 HP if failed Con saves).

## Enemies (Maze Stalkers)

### 3 PCs:
- 4 **Maze Goblins** (CR 1/4; know maze patterns by instinct, use shortcuts, ambush from behind walls).
- 2 **Minotaur Scouts** (reskin Minotaurs to CR 2; smaller, faster, reckless charge in corridors, gore attacks).
- 1 **Stone Guardian** (reskin Gargoyle; CR 2; merges with walls during shifts, immune to maze crushing, multiattack).

### 4-5 PCs:
- 6 Maze Goblins.
- 2 Minotaur Scouts.
- 2 Stone Guardians.
- 1 **Labyrinth Shambler** (reskin Shambling Mound; CR 5; absorbs lightning, engulf, moves through walls during transitions).

### Enemy Tactics:
- **Maze Goblins:** Memorize patterns; lead PCs into dead ends, then attack from behind; flee during wall shifts to reposition.
- **Minotaur Scouts:** Charge down corridors (10-foot charge, gore attack); trap PCs against walls; use labyrinthine rage (advantage when below half HP).
- **Stone Guardians:** Hide within walls during shifts (invisible), emerge to attack isolated PCs, retreat when outnumbered.
- **Labyrinth Shambler:** Phases through walls during transitions (not stopped by maze), engulfs PCs in tight corridors, blocks escape routes.

## Crushing Hazard

**If PC is standing where a wall rises:**
- DC 15 Dexterity save to move to adjacent cell before wall fully rises.
- Failure: Crushed against existing wall, 3d10 bludgeoning damage, knocked prone in random adjacent cell.
- **Trapped:** If PC fails save AND both adjacent cells also have walls rising, they're TRAPPED (restrained between walls, 4d10 bludgeoning, DC 17 Strength to break free before walls crush them; allies can help with DC 15 combined check).

## Memory and Mapping Challenge

**Pattern Recognition:**
- Smart PCs will notice patterns repeat (A-B-C-A-B-C).
- Can map layouts during first cycle (rounds 1-6), use knowledge in later cycles.
- **Skill Checks:** Intelligence (Investigation) DC 13 to memorize a pattern after seeing it once; DC 10 to recognize when pattern repeats.

**Communication Under Pressure:**
- PCs separated by walls can't see each other—must shout coordinates and status.
- Enemies will mimic PC voices (Deception DC 14) to misdirect: "False exit at A1!" (actually true exit).
- PCs must develop code words or trust recognition.

## Objectives

- **Primary:** Identify true exit portal via riddles and escape through it before round 18 (when maze collapses entirely).
- **Secondary:** All PCs escape together (no one left behind).
- **Bonus:** Defeat Labyrinth Shambler before escaping (extra Favor).

## Crowd Favor Hooks

- Reach central chamber and read all three riddle clues within first 6 rounds: +2 [[crowds_favor|Favor]] for efficiency.
- Correctly identify true exit on first attempt (no false portal mistakes): +3 Favor for brilliance.
- Memorize all three maze patterns by round 7: +2 Favor for memory.
- Rescue ally from false exit trap: +2 Favor per rescue.
- Survive crushing hazard without taking damage (successful Dex save): +1 Favor per save.
- Kill enemy during wall transition (6-second window when all walls are down): +2 Favor for timing.
- Navigate entire fight without being separated from party: +2 Favor for coordination.
- [[panache|Panache]] dive through true exit portal as final dramatic escape: +3 Favor.
- Create shorthand map system with teammates (drawn or verbal) that proves effective: +1 Favor for teamwork.

## Announcer Beats

- Opening: "THE LIVING LABYRINTH! Stone rises! Stone falls! Can they solve the puzzle—or be CRUSHED by it?!"
- First wall shift: "THE MAZE SHIFTS! Walls fall—WALLS RISE! New paths! New dangers!"
- First false exit: "NO! A TRAP! The portal betrays! Fire consumes! / Spikes impale! / Water drowns!"
- True riddle read: "They reach the center! They read the ancient words! Do they UNDERSTAND?"
- Crushing hazard: "TOO SLOW! The walls CLOSE! They're caught between stone and stone!"
- Pattern recognition: "BRILLIANT! They've mapped the maze! They KNOW what's coming!"
- Final escape: "THE TRUE EXIT! They've solved it! FREEDOM! The maze bows before their intellect!"
- Defeat: "The walls claim them! Crushed in the Living Labyrinth! The stone remembers their names!"

## GM Tips

- **Visual Aid:** Use grid map with removable wall pieces or VTT layers. Show pattern shifts clearly.
- **Countdown Timer:** Use actual 30-second timer (or count down at table) to create urgency during transitions.
- **Pattern Cards:** Pre-draw three maze patterns on cards; flip to new pattern when walls shift.
- **Memory Rewards:** If PCs take notes or draw maps, reward them with advantage on navigation checks.
- **Voice Confusion:** When enemies mimic PCs, have players make Insight checks to detect lies.
- **Crushing Drama:** Narrate crushing hazards viscerally: "Walls SLAM toward you—MOVE!"
- **Central Safety:** Remind PCs center is always open (safe fallback point if overwhelmed).
- **Riddle Accessibility:** If PCs struggle, have crowd chant hints: "THE EAST! SEEK THE EAST!"
- **Pacing:** First cycle = learning patterns. Second cycle = solving riddles. Third cycle = final escape.

## Tactical Elements

- **Split Party Risk:** Cross pattern separates PCs into quadrants; enemies exploit isolation.
- **Choke Points:** Narrow corridors favor defenders; use to bottleneck Minotaur charges.
- **Transition Advantage:** 6-second open window allows repositioning, rescues, or coordinated strikes.
- **Central Hub:** C3 is strategic meeting point but offers no cover; enemies know PCs will come here.
- **False Exit Traps:** Can be used tactically—shove enemies through false portals (enemies also die/injured).

## Aftermath Seeds

- **Maze-Mind:** PC who successfully memorized all patterns gains "Labyrinthine Intuition"—advantage on Survival checks to navigate dungeons/mazes for 1 week.
- **Patron Interest:** Architect's guild fascinated by PCs' spatial reasoning; offers contract to test deadly building designs (pays well, very risky).
- **Rumor:** Living Labyrinth was prototype prison for dangerous criminals—walls were meant to adapt to escape attempts. Someone wanted this tech tested on disposable gladiators.
- **Downtime:** Stone pillars can be purchased from arena (500 gp total)—contain minor divination magic, grant one *augury* cast per day (combined).
- **Injury:** PC crushed by walls develops claustrophobia (disadvantage on saves vs. fear in enclosed spaces for 1 month, then fades).
- **Legendary Moment:** If all PCs escaped on first attempt with zero false exits entered, crowd declares them "Maze-Breakers"; future puzzle bouts pay double.
- **Political:** Rival gladiators claim maze was rigged (true exits moved mid-fight)—arena must investigate, PCs called as witnesses.
- **Cursed Stone:** PC who entered false exit 2+ times haunted by phantom walls (visual hallucinations of walls closing in during rests; no mechanical effect, just unsettling).
- **Loot:** Defeating Labyrinth Shambler yields **Moss Cloak** (advantage on Stealth checks in natural terrain, can cast *pass without trace* 1/day).
