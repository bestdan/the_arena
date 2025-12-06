---
tags: [arena, test, validation, session-4]
content_type: test-scenarios
visibility: private
created: 2025-12-06
updated: 2025-12-06
---

# Drama Score Rubric - Test Scenarios

Validation scenarios to ensure the [[phoenix_resurrection_rubric|Phoenix Resurrection Rubric]] produces fair and thematically appropriate outcomes.

## Formula Reference
```
Drama Score = (Spent Favor × 2) + Retained Favor
```

---

## Scenario 1: The Hoarder vs. The Showboat

### Setup
Two gladiators earn the same total Favor (20) but use different strategies.

**Gladiator A (The Hoarder):**
- Earned: 20 Favor
- Spent: 3 Favor
- Retained: 17 Favor
- Drama: (3 × 2) + 17 = **23**

**Gladiator B (The Showboat):**
- Earned: 20 Favor
- Spent: 15 Favor
- Retained: 5 Favor
- Drama: (15 × 2) + 5 = **35**

### Result
✓ **PASS:** Showboat scores higher (35 vs 23) despite having less retained Favor
✓ System correctly rewards engagement over hoarding

---

## Scenario 2: Extreme Spending vs. Extreme Hoarding

**Gladiator A (All-In):**
- Earned: 25 Favor
- Spent: 24 Favor
- Retained: 1 Favor
- Drama: (24 × 2) + 1 = **49**

**Gladiator B (Pure Hoarder):**
- Earned: 25 Favor
- Spent: 0 Favor
- Retained: 25 Favor
- Drama: (0 × 2) + 25 = **25**

### Result
✓ **PASS:** All-in gladiator scores nearly 2× higher (49 vs 25)
✓ Demonstrates 2× multiplier working as intended
✓ Pure hoarding is mathematically inferior

---

## Scenario 3: Low Earner with Good Spending

**Gladiator A (High Earner, Low Spender):**
- Earned: 30 Favor
- Spent: 5 Favor
- Retained: 25 Favor
- Drama: (5 × 2) + 25 = **35**

**Gladiator B (Low Earner, High Spender):**
- Earned: 18 Favor
- Spent: 12 Favor
- Retained: 6 Favor
- Drama: (12 × 2) + 6 = **30**

### Result
✓ **PASS:** High earner still wins, but the gap is small (35 vs 30)
✓ Good spending partially compensates for lower total earning
✓ Both strategies are viable

---

## Scenario 4: The Unlucky Player

Player had bad luck, died early, earned less total Favor.

**Gladiator A (Average, Full Session):**
- Earned: 22 Favor
- Spent: 12 Favor
- Retained: 10 Favor
- Drama: (12 × 2) + 10 = **34**

**Gladiator B (Unlucky, Died Round 5):**
- Earned: 12 Favor (fewer rounds)
- Spent: 8 Favor (aggressive to compensate)
- Retained: 4 Favor
- Drama: (8 × 2) + 4 = **20**

### Result
⚠️ **ISSUE:** Unlucky player significantly behind (20 vs 34)
✓ **ACCEPTABLE:** System doesn't compensate for bad luck
✓ GM can account for this in "exceptional circumstances" clause
✓ Early death might generate sympathy—could influence tie-breaker

---

## Scenario 5: Eight Gladiators - Full Session

Realistic distribution from a complete session:

| Gladiator | Earned | Spent | Retained | Drama | Tier |
|-----------|--------|-------|----------|-------|------|
| Zara      | 28     | 22    | 6        | 50    | Champion (46+) |
| Kael      | 24     | 14    | 10       | 38    | Blessing (36-45) |
| PC1       | 22     | 12    | 10       | 34    | Vigor (25-35) |
| Rohm      | 20     | 10    | 10       | 30    | Vigor (25-35) |
| PC2       | 18     | 8     | 10       | 26    | Vigor (25-35) |
| Fennec    | 16     | 6     | 10       | 22    | Clean (16-24) |
| Merryn    | 15     | 5     | 10       | 20    | Clean (16-24) |
| PC3       | 14     | 3     | 11       | 17    | **DEAD** |

### Analysis
✓ **PASS:** Clear separation between ranks
✓ Zara (aggressive spender) gets Champion tier
✓ PC3 (conservative hoarder) dies despite decent retained Favor
✓ Middle pack shows viable strategies (30-38 Drama)
✓ All Drama scores in expected range (17-50)

---

## Scenario 6: Tie for Lowest

**Gladiator A:**
- Drama: 18

**Gladiator B:**
- Drama: 18

**Gladiator C:**
- Drama: 22

### Result
✓ **PASS:** Rubric provides tie-breaker options:
- Dramatic choice (GM/patron selects)
- Random (dice)
- Both die (harsh but memorable)
✓ System doesn't fail on edge case

---

## Scenario 7: Everyone Spends Heavily

All gladiators engage well with the mechanic:

| Gladiator | Earned | Spent | Retained | Drama |
|-----------|--------|-------|----------|-------|
| PC1       | 25     | 18    | 7        | 43    |
| PC2       | 24     | 17    | 7        | 41    |
| PC3       | 23     | 16    | 7        | 39    |
| PC4       | 22     | 15    | 7        | 37    |
| PC5       | 21     | 14    | 7        | 35    |
| PC6       | 20     | 13    | 7        | 33    |
| PC7       | 19     | 12    | 7        | 31    |
| PC8       | 18     | 11    | 7        | 29    |

### Result
✓ **PASS:** PC8 still dies (lowest Drama 29)
✓ All scores are good (29-43), showing strong engagement
⚠️ **GM OPTION:** Could allow all to resurrect since lowest is 29 (above "Adequate" threshold)
✓ Rubric acknowledges this edge case in guidelines
✓ Default: lowest still dies (maintains stakes)

---

## Scenario 8: Everyone Hoards

No one engages with spending:

| Gladiator | Earned | Spent | Retained | Drama |
|-----------|--------|-------|----------|-------|
| PC1       | 18     | 2     | 16       | 20    |
| PC2       | 16     | 1     | 15       | 17    |
| PC3       | 15     | 2     | 13       | 17    |
| PC4       | 14     | 1     | 13       | 15    |
| PC5       | 13     | 0     | 13       | 13    |
| PC6       | 12     | 1     | 11       | 13    |
| PC7       | 11     | 0     | 11       | 11    |
| PC8       | 10     | 1     | 9        | 11    |

### Result
⚠️ **PROBLEM:** Very low Drama across the board (11-20)
✓ **ADDRESSED:** Rubric includes "Suspiciously Low Drama" clause
✓ GM can apply consequences:
  - Most dramatic death still resurrects
  - Others resurrect with penalties
  - Snak and patrons express disappointment
✓ System identifies failure to engage with mechanic

---

## Scenario 9: Optimal Balance

What's the "sweet spot" for spending?

**Testing different spend rates with 20 Favor earned:**

| Spent % | Spent | Retained | Drama | Assessment |
|---------|-------|----------|-------|------------|
| 0%      | 0     | 20       | 20    | Too conservative |
| 25%     | 5     | 15       | 25    | Conservative |
| 40%     | 8     | 12       | 28    | Balanced |
| 50%     | 10    | 10       | 30    | **OPTIMAL** |
| 60%     | 12    | 8        | 32    | Aggressive (good) |
| 75%     | 15    | 5        | 35    | Very aggressive |
| 90%     | 18    | 2        | 38    | All-in |
| 100%    | 20    | 0        | 40    | Maximum Drama |

### Result
✓ **PASS:** 50-60% spending is optimal balance
✓ More spending is ALWAYS better for Drama Score
✓ The 2× multiplier incentivizes spending without making hoarding worthless
✓ System correctly implements design goal

---

## Scenario 10: Player Critique - "Retained Favor Doesn't Matter Enough"

**Concern:** "If I spend everything, retained is 0—isn't that bad?"

**Test:**
- Gladiator A: Earned 20, Spent 20, Retained 0 → Drama = (20×2)+0 = **40**
- Gladiator B: Earned 20, Spent 10, Retained 10 → Drama = (10×2)+10 = **30**
- Gladiator C: Earned 20, Spent 0, Retained 20 → Drama = (0×2)+20 = **20**

**Analysis:**
✓ Retained DOES matter—it adds directly to Drama
✓ But spending matters MORE (worth 2×)
✓ Balanced approach (B) is viable but not optimal
✓ **WORKING AS INTENDED:** Encourages spending without making retention worthless

---

## Scenario 11: Edge Case - Negative Favor?

Can Favor go negative? What if someone spent more than earned?

**Impossible in RAW:** You can't spend Favor you don't have.

**If GM allowed "Favor debt" (homebrew):**
- Spent 15, Retained -3 (in debt)
- Drama: (15 × 2) + (-3) = 30 - 3 = **27**

✓ System would still work mathematically
✓ Debt penalizes but doesn't eliminate Drama
✓ Not relevant to standard rules

---

## Validation Summary

### ✓ Passes All Core Tests
1. Spending is rewarded over hoarding (2× multiplier works)
2. System produces clear rankings
3. Edge cases are handled
4. Optimal strategy is 50-75% spending
5. Total engagement matters more than final retention
6. Stakes are maintained (someone dies)
7. Quality tiers create meaningful differentiation

### ⚠️ Known Limitations
1. Doesn't compensate for bad luck/early death
2. Requires tracking during session (or reconstruction)
3. GM discretion needed for extreme edge cases

### ✓ Thematic Alignment
1. Rewards showmanship and risk-taking
2. Punishes passive hoarding
3. Maintains consequences (permanent death)
4. Creates meaningful resurrection quality differences
5. Encourages teamwork (spending on allies increases Drama)

---

## Recommendation

**The Phoenix Resurrection Rubric is VALIDATED for use.**

It achieves the design goals:
- Values engagement over passivity
- Rewards spending without eliminating value of earning
- Maintains dramatic stakes
- Produces fair and thematically appropriate outcomes
- Handles edge cases gracefully

The system is ready for implementation in Session 4 and future Phoenix Rite events.
