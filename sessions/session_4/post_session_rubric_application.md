---
tags: [arena, session-4, post-session, gm-guide]
session_number: 4
content_type: guide
visibility: private
created: 2025-12-06
updated: 2025-12-06
---

# Applying the Drama Score Rubric Post-Session

**Situation:** You've completed Session 4 (Rite of Phoenix Flames) and all players have died. Now you need to determine who gets resurrected using the [[phoenix_resurrection_rubric|Phoenix Resurrection Rubric]].

## What You Need

To calculate Drama Scores retroactively, you need to know for each gladiator:

1. **Total Favor Earned** during the session
2. **Total Favor Spent** during the session
3. **Retained Favor** (amount remaining at death)

**Note:** "Retained Favor" is also called "Final Favor" or "Current Favor at death" - these terms are interchangeable.

If you tracked Favor normally during play, you should have columns showing current Favor throughout combat. You'll need to reconstruct the "Spent" column.

## Reconstruction Method

### If You Have Session Notes

Look through your session notes for each time a gladiator spent Favor:
- Search for [[crowds_favor|Crowd's Favor]] abilities used
- Note the cost of each ability
- Tally total spent per gladiator

### If You Don't Have Detailed Notes

**Estimation Method:**

For each gladiator, ask the player (or recall):
1. How many times did they use Favor abilities?
2. Which abilities did they favor?
3. Roughly what tier (1-point, 2-point, 3-point, 5-point abilities)?

**Common Spending Patterns:**
- **Conservative player:** 3-6 Favor spent (mostly 1-point abilities)
- **Moderate player:** 8-14 Favor spent (mix of 1-2 point abilities)
- **Aggressive player:** 15-25 Favor spent (regular 2-3 point abilities)
- **All-in player:** 25+ Favor spent (used high-cost abilities)

**Cross-Reference with Player Behavior:**
- Did they regularly use Favor abilities? (High spending)
- Did they save Favor "for emergencies"? (Low spending)
- Did they use it to help teammates? (Medium-high spending)
- Did they mention being cautious about Favor? (Low spending)

### Calculation Formula

Once you have (or estimate) the spent Favor:

```
Final Retained Favor = Total Earned - Total Spent
Drama Score = (Total Spent × 2) + Final Retained
```

**Alternative if you know Final Retained but not Spent:**

```
Total Spent = Total Earned - Final Retained
Drama Score = (Total Spent × 2) + Final Retained
```

## Example Reconstruction

### Gladiator: Kael

**From Notes:**
- Round 2: Used Flash Step (1 Favor)
- Round 3: Used Bold Stance (2 Favor)
- Round 5: Used Light in Their Eyes (2 Favor)
- Round 6: Used Crowd Shield (3 Favor)
- Round 7: Used Salt in the Wound (2 Favor)
- Round 8: Used Perfect Opening (3 Favor)

**Calculation:**
- Total Spent: 1 + 2 + 2 + 3 + 2 + 3 = **13 Favor**
- Final Retained (from notes): **8 Favor**
- Total Earned: 13 + 8 = **21 Favor**
- **Drama Score: (13 × 2) + 8 = 26 + 8 = 34**

### Gladiator: Zara

**From Recall (incomplete notes):**
- Used Favor "a lot" for damage abilities
- Player is aggressive, probably spent heavily
- Final Retained (from notes): **4 Favor**

**Estimation:**
- Ask player: "How many times did you spend Favor?"
- Player recalls: "At least 6-7 times, mostly 2-3 point abilities"
- Conservative estimate: 6 uses × 2.5 average = **15 Favor spent**
- Total Earned: 15 + 4 = **19 Favor**
- **Drama Score: (15 × 2) + 4 = 30 + 4 = 34**

### Gladiator: PC3

**Minimal Data:**
- Final Retained (from notes): **12 Favor**
- Player mentioned "saving it for later" multiple times

**Estimation:**
- Conservative player who hoarded
- Probably spent 3-6 Favor total
- Estimate: **5 Favor spent**
- Total Earned: 5 + 12 = **17 Favor**
- **Drama Score: (5 × 2) + 12 = 10 + 12 = 22**

## Ranking and Resurrection

Once you have all Drama Scores:

1. **Rank them from highest to lowest**
2. **Lowest Drama Score = Permanent Death**
3. **All others resurrect** with quality based on their Drama tier

### Example Final Rankings

| Rank | Gladiator | Drama Score | Result |
|------|-----------|-------------|---------|
| 1st  | Zara      | 39          | Champion resurrection (46+ tier) |
| 2nd  | Kael      | 34          | Vigor resurrection (25-35 tier) |
| 3rd  | PC1       | 31          | Vigor resurrection (25-35 tier) |
| 4th  | Rohm      | 28          | Vigor resurrection (25-35 tier) |
| 5th  | PC2       | 26          | Vigor resurrection (25-35 tier) |
| 6th  | Merryn    | 23          | Clean resurrection (16-24 tier) |
| 7th  | Fennec    | 20          | Clean resurrection (16-24 tier) |
| 8th  | PC3       | 17          | **STAYS DEAD** |

## Handling Uncertainty

If you genuinely can't reconstruct spending:

### Option 1: Conservative Default
Assume everyone spent 25-40% of their total earned Favor unless you have evidence otherwise.

**Example:**
- PC ended with 10 Favor retained
- Assume 30% spending rate
- If retained is 70%, then: 10 / 0.7 ≈ 14 total earned
- Spent: 14 - 10 = 4
- Drama: (4 × 2) + 10 = 18

### Option 2: Player Input
Ask each player to estimate their own spending honestly:
- "How many Favor abilities do you remember using?"
- "Were you conservative or aggressive with spending?"
- "Did you use any 3+ point abilities?"

### Option 3: Retroactive Estimation Table

Create a table and fill it in collaboratively:

| Gladiator | Player Recall | GM Recall | Spending Estimate |
|-----------|---------------|-----------|-------------------|
| PC1       | "Maybe 3-4 times" | Remembers Crowd Shield once | 6-8 Favor |
| PC2       | "I saved most of it" | Agrees, very conservative | 2-4 Favor |
| Kael (NPC)| N/A | Used Bold Stance and Flash Step | 4 Favor |

## Tips for Future Sessions

To avoid reconstruction challenges:

1. **Track Spent column live** during combat
2. **Use index cards** with Current/Spent both visible
3. **Announce Drama Scores** periodically (encourages accurate tracking)
4. **Mark each spending** in notes: "Kael spends 2 for Bold Stance"
5. **Use the [Drama Score Tracker](drama_score_tracker.md)** provided

## Communicating Results

Once you've determined rankings:

### To the Table
"Okay everyone, I've calculated your Drama Scores using the Phoenix Resurrection Rubric. Remember, this is based on how much Favor you earned AND spent—spending is worth double hoarding because it creates spectacle."

### Show Transparency
Display the calculations so players understand:
- "Kael: 13 spent, 8 retained = (13×2)+8 = 34 Drama"
- "PC3: 5 spent, 12 retained = (5×2)+12 = 22 Drama"

### The Reveal
"The Phoenix has judged. Seven shall return... but [PC3], you stayed too cautious. Your final Drama Score was 22—the lowest. The Phoenix does not grant mercy to those who hoard the crowd's love."

## Handling Player Reactions

**If player contests the calculation:**
- Show your work
- Explain the rubric rationale (spending = engagement)
- Be open to corrections if you misremembered their actions
- The goal is fair, not punitive

**If player feels unfairly penalized:**
- Acknowledge that hoarding is a valid strategy
- Explain that *this specific event* rewards spending
- It was communicated (or should have been) before the session
- This teaches a lesson: in Phoenix events, spend or die

**If player is gracious:**
- Honor their character's death dramatically
- Offer them a memorable send-off
- Help them create an interesting new character
- Their sacrifice makes the session memorable for everyone

## Final Notes

The Drama Score system exists to:
1. **Reward engagement** with the Favor mechanic
2. **Discourage hoarding** in an event where death is guaranteed
3. **Create meaningful choices** about spending vs. saving
4. **Maintain stakes** while encouraging spectacle

If your reconstruction feels uncertain, err on the side of generosity for close scores, but maintain the principle: spending Favor matters more than hoarding it in the Rite of Phoenix Flames.
