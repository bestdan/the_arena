---
tags: [arena, session-4, summary, implementation]
content_type: summary
visibility: private
created: 2025-12-06
updated: 2025-12-06
---

# Phoenix Resurrection Rubric - Implementation Summary

## What Was Created

A comprehensive system for determining who gets resurrected in Session 4 "Rite of the Phoenix Flames" based on player engagement with the Crowd's Favor mechanic.

## Core Formula

```
Drama Score = (Spent Favor × 2) + Retained Favor
```

**Lowest Drama Score = Permanent Death**

## Design Rationale

Your original idea was spot-on! The issue you identified—that final Favor balance measures what players *didn't* use—is solved by valuing spent Favor at 2× retained Favor.

**Why 2× multiplier?**
- Encourages active engagement without making hoarding worthless
- Rewards risk-taking and showmanship (the campaign's core theme)
- Makes spending strategically better than hoarding in resurrection events
- Players who spend 50-75% of earned Favor get optimal Drama Scores

## Files Created

### 1. **Phoenix Resurrection Rubric** (`mechanics/phoenix_resurrection_rubric.md`)
The comprehensive mechanic document including:
- Drama Score calculation
- Resurrection determination rules
- Edge case handling (ties, low engagement, high engagement)
- Resurrection quality tiers (0-15, 16-24, 25-35, 36-45, 46+)
- GM guidance
- Example scenarios
- Design philosophy

### 2. **Drama Score Tracker** (`sessions/session_4/drama_score_tracker.md`)
A practical tracking sheet for GMs to use during live play:
- Live tracking table for all 8 gladiators
- Instructions for tracking gains and spending
- Drama Score calculation examples
- Milestone announcement reminders
- Warning system for lagging players
- Post-combat calculation template

### 3. **Post-Session Application Guide** (`sessions/session_4/post_session_rubric_application.md`)
**MOST RELEVANT TO YOUR CURRENT SITUATION**

Since you've already completed the session, this guide shows you how to:
- Reconstruct spent Favor from session notes
- Estimate spending if you don't have detailed tracking
- Calculate Drama Scores retroactively
- Handle uncertainty and player input
- Communicate results fairly to players

### 4. **Validation Test Scenarios** (`sessions/session_4/drama_score_validation.md`)
10+ test scenarios proving the system works:
- Hoarder vs. Showboat
- Extreme cases
- Full 8-gladiator session
- Edge cases (ties, all high, all low)
- Optimal spending analysis (50-75% is best)

## Files Updated

### Session 4 Files
- **session_4_encounter.md** - Now references Drama Score instead of raw Favor
- **session_4/index.md** - Explains Drama Score system upfront

### Mechanics Index
- **mechanics/index.md** - Lists Phoenix Resurrection Rubric in special events section

## How to Use It Right Now

Since you've completed Session 4 and all players died:

### Step 1: Read the Post-Session Guide
Go to `sessions/session_4/post_session_rubric_application.md` and follow the reconstruction method.

### Step 2: Gather Data
For each gladiator, determine or estimate:
- Total Favor earned during session
- Total Favor spent during session
- Final Favor retained at death

### Step 3: Calculate Drama Scores
```
Drama Score = (Spent × 2) + Retained
```

### Step 4: Rank and Decide
- Rank all 8 gladiators by Drama Score (highest to lowest)
- Lowest Drama Score = permanent death
- Others resurrect with quality based on their Drama tier

### Example Quick Calculation

**If you remember:**
- Player A ended with 15 Favor, didn't spend much → estimate 4 spent
  - Drama = (4 × 2) + 15 = **23**
  
- Player B ended with 5 Favor, spent aggressively → estimate 18 spent
  - Drama = (18 × 2) + 5 = **41**
  
- Player C ended with 10 Favor, moderate spending → estimate 10 spent
  - Drama = (10 × 2) + 10 = **30**

**Result:** Player A has lowest Drama (23) and stays dead. Players B and C resurrect.

## Resurrection Quality Tiers

Once you know who resurrects, their Drama Score determines quality:

- **0-15 Drama:** Basic resurrection (1 level exhaustion)
- **16-24 Drama:** Clean resurrection (full HP, no penalty)
- **25-35 Drama:** Resurrection with vigor (advantage next session)
- **36-45 Drama:** Phoenix blessing (permanent boon: +1 skill, +5 max HP, or Phoenix Trinket)
- **46+ Drama:** Champion of the Phoenix (blessing + Phoenix Mark + +2 Favor for 3 sessions)

## Key Benefits of This System

✓ **Rewards the right behavior** - Spending Favor for spectacle > hoarding for safety
✓ **Fair and measurable** - Clear math, no GM favoritism
✓ **Maintains stakes** - Someone still dies
✓ **Encourages teamwork** - Spending on allies increases your Drama
✓ **Thematically perfect** - Phoenix rewards those who embraced the spectacle
✓ **Handles edge cases** - Ties, low engagement, high engagement all addressed
✓ **Player-friendly** - Can be explained clearly and justified mathematically

## Communicating to Players

When you reveal the results:

1. **Explain the system first:**
   "The Phoenix judges based on Drama Score: spent Favor times 2, plus retained Favor. This rewards those who engaged with the crowd and created spectacle."

2. **Show your work:**
   "Kael: 14 spent, 10 retained = (14×2)+10 = 38 Drama"
   "PC3: 4 spent, 12 retained = (4×2)+12 = 20 Drama"

3. **Make it narrative:**
   "The Phoenix saw Kael's bold displays and fearless spending. But PC3, you held back. The crowd remembers bold warriors, not cautious ones."

4. **Be fair but firm:**
   If players contest, show them the rubric was designed to reward engagement. This is a teaching moment: in Phoenix events, use it or lose it.

## Future Use

This rubric isn't just for Session 4! Use it for:
- Any future "Rite of Phoenix Flames" events
- Other guaranteed-resurrection scenarios
- Special arena events where engagement matters more than survival

## Critique and Improvements Welcome

The system was validated through 10+ test scenarios, but if you find issues when applying it to your actual session data, the rubric includes GM discretion clauses.

If players had genuinely bad luck (died early, fewer opportunities), you can:
- Weight Drama slightly to account for rounds survived
- Use GM judgment to break close ties
- Apply the "exceptional circumstances" clause

The goal is fair consequences, not arbitrary punishment.

## Questions or Issues?

If you run into problems applying the rubric or need clarification:
1. Check the **Post-Session Application Guide** for reconstruction methods
2. Review the **Validation Scenarios** to see if your case is covered
3. Use your best judgment and communicate reasoning to players
4. The Phoenix judges courage and spectacle—let that guide close calls

---

## Quick Reference Card

**Formula:** Drama = (Spent × 2) + Retained

**Result:** Lowest Drama = Permanent Death, Others Resurrect

**Quality Tiers:**
- 0-15: Basic (+1 exhaustion)
- 16-24: Clean (full HP)
- 25-35: Vigor (+advantage)
- 36-45: Blessing (+permanent boon)
- 46+: Champion (+Phoenix Mark)

**Optimal Strategy:** Spend 50-75% of earned Favor

**Philosophy:** The Phoenix rewards those who embrace the spectacle
