---
tags: [arena, meta, history, recommendations]
content_type: recommendations
created: 2025-11-23
updated: 2025-11-23
audience: gm
aliases: [best-practices, ai-campaign-guide]
---

# Recommendations: Building an AI-Assisted TTRPG Campaign Manager

## Core Learnings from The Arena Repository

### 1. Initialize Git BEFORE AI Collaboration

**Problem**: The Arena's early development with ChatGPT/Claude was lost—months of iteration unrecorded.

**Recommendation**: Create your repository on day one, even for exploratory work. Commit early, commit often. Future you (and your AI collaborators) will thank you for the history.

### 2. Design Framework First, Generate Content Second

**Pattern Observed**: PR #1 (optimization) came *hours* after initialization, before major content generation began. This wasn't accident—it was necessary.

**Recommendation**:
- **Week 1**: Build scaffolding (directory structure, instruction files, templates, core mechanics)
- **Week 2+**: Generate content at scale using those frameworks
- Resist the urge to have AI generate content before the architecture is solid

### 3. Distributed Instructions Over Monolithic Documentation

**Key Innovation**: Multiple directory-scoped `AGENTS.md` files rather than one giant instruction file.

**Why This Works**:
- **Token efficiency**: AI loads only relevant context for the task
- **Maintainability**: Changes to NPC guidance don't affect session instructions
- **Clarity**: Focused, specific instructions outperform general guidelines

**Implementation**:
```
repo/
├── AGENTS.md              # Overview, map, general rules
├── sessions/AGENTS.md     # Session-specific instructions
├── mechanics/AGENTS.md    # Homebrew system guidelines
├── npcs/AGENTS.md         # NPC creation standards
└── ideas/AGENTS.md        # Brainstorming format
```

### 4. Rigid Templates Enable Creative Variety

**Paradox**: The more structured your templates, the more creative freedom AI has within them.

**Every Arena Encounter Follows Identical Structure**:
1. Hook/Theme
2. Arena Layout
3. Enemy Roster (with Flex scaling)
4. Tactical Phases
5. Crowd Favor Hooks
6. Announcer Beats
7. GM Tips
8. Aftermath Seeds

**Result**: 60+ unique encounters, all immediately usable at table, consistent quality, diverse tactical spaces.

**Recommendation**: Create strict templates for repeatable content types. Include:
- Required sections (enforce completeness)
- Formatting standards (enable consistency)
- Mechanical requirements (stat blocks, CR, saves)
- Tone guidelines (maintain voice)

### 5. Establish Cross-Reference Systems Early

**Pattern**: Liberal `[[wiki links]]` throughout content enable:
- Mechanics referenced from encounters
- NPCs connected to sessions
- Related encounters linked
- Thematic threads discoverable

**Recommendation**: Choose a linking system (wiki links, tags, whatever) and enforce it from day one. AI is excellent at maintaining cross-reference discipline if you establish the pattern.

### 6. Clear Division of Labor: Human Strategy, AI Execution

**What Humans Do Better**:
- Strategic architecture
- Quality oversight (PR review)
- Framework design
- Tone-setting
- Continuity tracking across sessions

**What AI Does Better**:
- Systematic content generation at scale
- Maintaining consistency within constraints
- Mechanical calculations (CR, stat blocks)
- Following templates precisely
- Cross-referencing exhaustively

**Recommendation**: Don't ask AI to design your campaign. Ask AI to generate 20 encounters following your campaign's design.

### 7. PR-Based Workflow Maintains Quality at Scale

**Pattern**: 24 AI commits, all through PRs with human review before merge.

**Why This Works**:
- Human oversight catches drift from campaign tone
- Review confirms mechanical accuracy
- Merge decisions maintain repo coherence
- Branch names document intent (`copilot/create-bbeg-battles`)

**Recommendation**:
- Never give AI direct commit access to main
- Review every PR, even if you trust the AI
- Use meaningful branch names
- Don't batch—review and merge incrementally

### 8. Optimize for Table Use, Not Reading

**Key Insight**: Every AI-generated document includes immediately usable game content:
- Specific stat blocks, not vague descriptions
- Exact DCs and damage values
- Flex scaling for party size variations
- GM tips for improvisation moments

**Recommendation**: Your quality bar should be "can I run this at table tonight?" not "is this interesting to read?" Generate session notes format, not fiction.

### 9. Meta-Documentation Preserves Learning

**Pattern**: The repository documented its own development process, creating institutional memory.

**Recommendation**: Periodically generate:
- Repository history/narrative
- "What worked" retrospectives
- Template evolution notes
- Failed experiment documentation

This creates feedback loops: analyze what works → refine instructions → generate better content.

## Concrete Starting Template

If starting fresh, follow this sequence:

### Phase 1: Foundation (Before AI Content Generation)
1. Initialize git repository
2. Create core directory structure
3. Write distributed AGENTS.md files
4. Document 3-5 session templates you actually used
5. Create one example of each content type manually
6. Establish cross-reference system
7. **Commit everything**

### Phase 2: Template Refinement
1. Have AI generate ONE piece of content per type
2. Review for usability, tone, completeness
3. Refine your AGENTS.md instructions
4. Iterate until quality is table-ready
5. **Don't scale until templates work**

### Phase 3: Scaled Generation
1. Generate content in batches (5-10 pieces)
2. Use PR workflow with meaningful names
3. Review each batch before merging
4. Track what works (and doesn't)
5. Refine instructions based on drift

### Phase 4: Maintenance
1. Update AGENTS.md as campaign evolves
2. Document actual play results
3. Generate retrospective analyses
4. Prune or archive unused content
5. Keep templates synchronized with reality

## Anti-Patterns to Avoid

1. **Asking AI to design your campaign framework** → You design, AI fills
2. **Monolithic instruction files** → Distribute by scope
3. **Vague quality standards** → Specific, table-ready requirements
4. **Batch generating before template refinement** → Iterate first, scale second
5. **No version control** → Git from day one
6. **Direct commits to main** → PR workflow with review
7. **Content without structure** → Templates before creativity
8. **Ignoring actual play feedback** → Living documentation that evolves

## Success Metrics

You'll know your system works when:
- You can generate 10 quality sessions in an hour
- Every document is immediately usable at table
- New content maintains consistent tone/quality
- Cross-references stay coherent
- You spend more time playing than preparing
- AI suggestions feel like your campaign voice

## Final Principle

**Structure is not the enemy of creativity—it's the enabler of creative scalability.**

Rigid frameworks don't constrain imagination; they free you from reinventing wheels so you can focus on what makes your campaign unique. The Arena works because every encounter follows identical structure while exploring entirely different tactical, narrative, and thematic spaces.

Design the machine. Let AI run it. Play the campaign that emerges.
