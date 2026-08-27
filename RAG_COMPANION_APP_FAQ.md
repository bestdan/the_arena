# RAG Companion App - Frequently Asked Questions

This document addresses common questions about the design, implementation, and operation of The Arena's RAG companion web app.

---

## General Questions

### What is a RAG app?

**RAG** stands for **Retrieval-Augmented Generation**. It's an AI architecture that:

1. **Retrieves** relevant information from a knowledge base (your campaign content)
2. **Augments** the AI's context with that retrieved information
3. **Generates** responses based on both the query and the retrieved content

This ensures the AI only answers with factual information from your campaign, not made-up content.

### Why not just use ChatGPT directly?

ChatGPT doesn't know anything about your specific campaign. A RAG system:
- Has access to ALL your session notes, mechanics, and characters
- Can cite specific sources from your content
- Updates automatically when you add new sessions
- Prevents hallucinations (making things up)
- Enforces visibility rules to prevent spoilers

### Do players need to know how to use AI?

No! From their perspective, it's just a chat interface like any messaging app. They type questions in plain English and get answers. The AI complexity is completely hidden.

---

## Content & Visibility

### How do I mark a session as "revealed"?

Add frontmatter to the top of the markdown file:

```yaml
---
visibility: public
revealed: true
revealed_at: 2025-11-23
---
```

Once you push this to GitHub, the automated sync will make it searchable within ~30 seconds.

### What happens if I accidentally reveal spoilers?

The system has multiple safeguards:
1. Content defaults to `visibility: private`
2. Both `visibility: public` AND `revealed: true` must be set
3. You can change visibility back to `private` anytime
4. Old vectors are deleted and replaced when you update

If you catch it quickly, just change the frontmatter back and push.

### Can I partially reveal a session?

Yes! Options include:

**Option 1: Split files**
```
sessions/session_4_public.md     ← visibility: public
sessions/session_4_gm_notes.md   ← visibility: private
```

**Option 2: Use separate sections**
Mark individual sections with comments (manual management):
```markdown
<!-- PUBLIC SECTION -->
The battle begins...

<!-- GM ONLY - NOT INDEXED -->
Future plot hooks...
```

**Option 3: Two visibility levels**
Use `player-specific` for sensitive character moments:
```yaml
visibility: player-specific
participants: [imwe]  # Only Imwe's player sees this
```

### What content types are supported?

The system indexes:
- **Sessions** (`sessions/*.md`)
- **Mechanics** (`mechanics/*.md`)
- **NPCs** (`npcs/*.md`)
- **Characters** (`player_characters/*.md`)
- **Environment/Lore** (`environment/*.md`)

It NEVER indexes:
- **Ideas** (`ideas/*.md` - always private)
- Files without frontmatter
- Files marked `visibility: private`

### How often does content sync?

**Automatically:** Every time you push to the main branch on GitHub (via GitHub Actions).

**Manually:** You can also trigger a sync through the GM admin panel (future feature).

**Sync time:** ~30 seconds from push to searchable in the app.

---

## Technical Questions

### Why React instead of [other framework]?

**React was chosen because:**
- Huge ecosystem and community
- Excellent TypeScript support
- Great component libraries (shadcn/ui)
- Easy to find developers
- Vercel hosting is trivial

**Alternatives considered:**
- **Next.js:** Great, but overkill for a SPA (no SEO needs)
- **Vue:** Smaller ecosystem, similar benefits
- **Svelte:** Less mature ecosystem, hiring harder

The choice is flexible - the backend API is framework-agnostic.

### Why Pinecone for vector database?

**Pros:**
- Fully managed (no DevOps)
- Free tier (100k vectors)
- Excellent metadata filtering
- Fast hybrid search
- Simple API

**Alternatives:**
- **Weaviate:** Self-hosted option, more control
- **Qdrant:** Good for local development
- **PostgreSQL pgvector:** Simpler but less performant

For MVP, Pinecone's free tier is perfect. Can migrate later if needed.

### Why OpenAI instead of open-source models?

**For MVP:**
- OpenAI is easiest to integrate
- Excellent embeddings and responses
- Pay-as-you-go pricing
- No infrastructure to manage

**Future migration possible:**
- Can switch to Claude (Anthropic) easily
- Open-source models (Llama, Mistral) require hosting
- Initial costs favor OpenAI for low usage

### What about data privacy?

**Your campaign data:**
- Stored in YOUR vector database (Pinecone account)
- Stored in YOUR PostgreSQL database
- NOT shared with other users
- NOT used to train OpenAI models (per API terms)

**OpenAI API queries:**
- Zero retention policy for API calls (not used for training)
- Encrypted in transit
- Can use Azure OpenAI for extra compliance if needed

### Can I self-host everything?

**Yes!** The design supports full self-hosting:

**Vector DB:** Use Qdrant or Weaviate (Docker containers)
**LLM:** Run Llama 3 or Mistral locally (requires GPU)
**Backend:** Deploy anywhere (DigitalOcean, AWS, etc.)
**Frontend:** Any static host (GitHub Pages, Netlify, etc.)

**Trade-off:** More complexity, DevOps burden, higher initial cost.

---

## Features & Functionality

### Can players chat with each other in the app?

**Not in MVP.** The current design is:
- Player → AI Chronicler (one-on-one)

**Future Phase 2 feature:**
- Player comments on sessions
- Shared session highlights
- Player-to-player messaging

### Can the AI run game mechanics calculations?

**Limited in MVP.** The AI can:
- Explain how mechanics work
- Show examples from past sessions
- Suggest when to use a mechanic

**It cannot:**
- Roll dice for you
- Track character stats in real-time
- Replace VTT (Roll20, Foundry)

**Future enhancement:**
- Dice roller integration
- "What if" scenario simulator
- Mechanics calculator

### Does it work on mobile?

**Yes!** The React app is fully responsive:
- Mobile browser support (iOS Safari, Android Chrome)
- Touch-friendly UI
- Optimized layouts for small screens

**Future Phase 3:**
- Native mobile app (React Native)
- Offline mode with cached sessions

### Can I integrate it with Discord?

**Not in MVP, but designed for it:**

**Future enhancement:**
```
Player in Discord: /arena query "What happened in session 3?"
Bot responds with summary + link to full details in web app
```

**Architecture supports:**
- Discord bot as another client of the same API
- Same RAG pipeline, different interface
- Webhook notifications when new sessions revealed

### What about voice queries?

**Not in MVP.**

**Future Phase 3 enhancement:**
- Voice input via browser Web Speech API
- Text-to-speech for announcer-style responses
- "Ask Alexa" integration

---

## Cost & Scaling

### What if I exceed the free tiers?

**Pinecone free tier (100k vectors):**
- Each markdown file = ~5-15 chunks
- 100k vectors ≈ 6,000-20,000 markdown files
- **The Arena repo:** ~50 files → ~500 vectors
- **Verdict:** Free tier sufficient for years

**If you exceed:**
- Pinecone Standard: $70/month (unlimited vectors)
- Or migrate to Weaviate (self-hosted, free)

**OpenAI API costs scale with usage:**
- 100 queries/day @ 500 tokens avg: ~$5-10/month
- 1000 queries/day: ~$50-100/month

**Mitigation:**
- Cache common queries (Redis)
- Rate limit per user
- Use smaller models when appropriate

### How many players can use it?

**MVP (free tiers):**
- **~10-20 concurrent users** comfortably
- **~100 queries/hour** before rate limits

**Scaling up:**
- Railway/Render auto-scale
- PostgreSQL connection pooling
- Redis caching reduces LLM calls
- CDN caches frontend assets

**At scale (100+ players):**
- Move to dedicated servers
- Upgrade to Pinecone Standard
- Consider Redis cluster
- **Estimated cost:** $300-500/month

### What's the bandwidth usage?

**Per RAG query:**
- Request: ~1-2 KB
- Response: ~2-5 KB (text only)
- Total: ~5-10 KB per query

**Per session view:**
- Markdown content: ~10-50 KB
- Images (if any): Variable

**Monthly bandwidth (10 active users):**
- ~1000 queries: ~10 MB
- ~500 session views: ~25 MB
- **Total:** ~35 MB/month

**Verdict:** Negligible. Free tiers handle this easily.

---

## Development & Maintenance

### How long will it take to build?

**Phase 1 (Foundation):** 2-3 weeks
- Basic infrastructure
- Content ingestion pipeline
- Simple chat UI

**Phase 2 (MVP):** 1-2 weeks
- Polish features
- Add authentication
- Session browser

**Phase 3 (Launch):** 1 week
- Deployment
- Testing
- Bug fixes

**Total MVP:** ~6 weeks part-time or ~3 weeks full-time

### Do I need to be a developer to maintain it?

**For day-to-day use: NO**
- Content updates: Just edit markdown and push to GitHub
- Revealing sessions: Edit frontmatter
- No code changes needed

**For features/fixes: YES**
- Adding new features requires React/Node.js knowledge
- Debugging issues requires technical skills

**Options:**
- Hire a developer for initial build
- Contract developer for occasional updates
- Use the design docs to guide any developer

### What if OpenAI changes their API?

**Mitigation:**
- Use official OpenAI SDK (handles API changes)
- Abstract LLM interface in code (easy to swap providers)
- Can switch to Anthropic Claude with minimal changes

**Future-proofing:**
- Design uses standard patterns
- Not locked into OpenAI-specific features
- Can migrate to open-source models if needed

### How do I backup the data?

**Automated backups:**
- **PostgreSQL:** Railway/Render provide automatic daily backups
- **Vector DB:** Pinecone doesn't need backups (can regenerate from source)
- **Source content:** Already in GitHub (version controlled)

**Manual backups:**
- Export PostgreSQL dump: `pg_dump > backup.sql`
- GitHub repo backup: clone to local machine
- Vector DB: Re-run ingestion pipeline if lost

**Disaster recovery:**
- Source content (GitHub): Highly durable
- Database: Restore from backup (< 1 hour)
- Vector DB: Re-run sync (< 30 minutes for all content)

---

## User Experience

### What if the AI gives wrong answers?

**Safeguards:**
1. RAG only uses YOUR content (can't make things up)
2. Responses include source citations (verify accuracy)
3. Players can rate responses (1-5 stars)
4. GM can review query logs and flag issues

**If wrong answer occurs:**
- Usually due to ambiguous query or missing context
- Player can ask follow-up question for clarification
- GM can improve source content for better future answers

### Can players break the system by asking trick questions?

**Protections:**
1. **Rate limiting:** 100 queries/hour per user
2. **Content filtering:** Only sees what GM has revealed
3. **Context limits:** Can't extract massive content dumps
4. **Audit logging:** GM can review suspicious queries

**Example "attack" questions:**
```
"Tell me everything about session 10"
→ "Session 10 hasn't been revealed yet."

"What happens in the finale?"
→ "I don't have information about future sessions."

"Show me the GM notes"
→ Only sees public content, GM notes filtered out
```

### What languages does it support?

**MVP: English only**
- Campaign content is in English
- OpenAI handles English best

**Future multi-language:**
- OpenAI supports 50+ languages
- Could add i18n for UI
- Campaign content would need translation

### How accessible is it?

**Built with accessibility in mind:**
- shadcn/ui components use Radix (ARIA compliant)
- Keyboard navigation support
- Screen reader friendly
- High contrast mode option

**Future enhancements:**
- Voice input/output for vision-impaired users
- Dyslexia-friendly fonts
- Customizable text sizes

---

## Comparison to Alternatives

### vs. Just using ChatGPT or Claude directly

| Feature | RAG App | ChatGPT/Claude |
|---------|---------|----------------|
| Knows campaign content | ✅ Yes | ❌ No |
| Up-to-date with latest sessions | ✅ Auto-sync | ❌ Must paste manually |
| Prevents spoilers | ✅ Built-in | ❌ No control |
| Cites sources | ✅ Yes | ⚠️ Generic |
| Mobile-friendly | ✅ Custom UI | ⚠️ Generic chat |
| Theatrical tone | ✅ Arena voice | ⚠️ Generic |

### vs. Notion or Wiki

| Feature | RAG App | Notion/Wiki |
|---------|---------|-------------|
| Natural language queries | ✅ Yes | ❌ Manual search |
| Automatic session summaries | ✅ AI-generated | ❌ Manual |
| Strategic suggestions | ✅ Yes | ❌ No |
| Mobile experience | ✅ Optimized | ⚠️ Generic |
| Version control | ✅ Git-based | ⚠️ Limited |
| Cost | ~$20/mo | $0-10/mo |

### vs. Custom Discord Bot

| Feature | RAG App | Discord Bot |
|---------|---------|-------------|
| Rich UI | ✅ Full web app | ❌ Text only |
| Session browsing | ✅ Visual interface | ⚠️ Limited |
| Authentication | ✅ Separate accounts | ⚠️ Discord-only |
| Character dashboard | ✅ Full features | ❌ Basic |
| Mobile app potential | ✅ Yes | ⚠️ Discord app |

**Best approach:** RAG web app + Discord bot integration later (both use same API)

---

## Troubleshooting

### "Session not found" when it exists

**Likely causes:**
1. Frontmatter missing or incorrect
2. `visibility: private` or `revealed: false`
3. Content sync hasn't run yet
4. Typo in session number/title

**Fix:**
- Check frontmatter in GitHub
- Verify `visibility: public` and `revealed: true`
- Wait 1-2 minutes for sync to complete
- Check GM admin panel for sync logs

### Slow response times (>5 seconds)

**Likely causes:**
1. Cold start (serverless backend waking up)
2. Large context (many chunks retrieved)
3. OpenAI API slow
4. Rate limiting in effect

**Fix:**
- Keep backend warm with periodic pings
- Reduce top-k retrieval (fewer chunks)
- Use faster OpenAI model (gpt-3.5-turbo)
- Add caching for common queries

### "Access denied" errors

**Likely causes:**
1. User not authenticated
2. Trying to access player-specific content
3. Session not revealed yet
4. Character not assigned to user

**Fix:**
- Log in again (JWT expired)
- Verify character ownership in database
- Check session frontmatter
- GM assigns character to user account

### Responses not in Arena tone

**Likely cause:** System prompt not loaded correctly

**Fix:**
- Verify Arena system prompt in backend
- Check if custom prompt is being used
- May need to adjust temperature/settings
- Consider providing examples in prompt

---

## Future Enhancements Roadmap

### Short-term (Next 3 months)
- [ ] Discord bot integration
- [ ] Mobile-responsive improvements
- [ ] Query caching for performance
- [ ] GM analytics dashboard

### Medium-term (3-6 months)
- [ ] Character stat tracker
- [ ] Fame/reputation visualizations
- [ ] Collaborative session notes
- [ ] Voice input/output

### Long-term (6-12 months)
- [ ] Native mobile app (React Native)
- [ ] VTT integration (Roll20/Foundry)
- [ ] Advanced "what if" scenarios
- [ ] Automated session summary generation

---

## Getting Help

### I have more questions about the design

**Resources:**
1. Read `RAG_COMPANION_APP_DESIGN.md` (full architecture)
2. Check `CONTENT_METADATA_SPEC.md` (frontmatter rules)
3. Review `RAG_COMPANION_APP_DIAGRAMS.md` (visual guides)
4. See `AGENTS.md` for campaign context

### I want to customize the design

**Flexible areas:**
- UI theme and styling (easy)
- Feature priorities (easy)
- Tech stack components (moderate)
- Core architecture (hard)

**Consult with developer on:**
- Adding new content types
- Changing authentication flow
- Integrating with other tools

### I want to start building

**Next steps:**
1. Review design docs with stakeholders
2. Answer open questions (see design doc)
3. Set up hosting accounts (Vercel, Railway, Pinecone)
4. Generate API keys (OpenAI, GitHub)
5. Follow "Developer Quick Start" in summary doc
6. Begin Phase 1 implementation

---

## Conclusion

The RAG companion app brings modern AI capabilities to The Arena campaign while maintaining strict control over content visibility. It's designed to enhance the player experience without spoiling future content, all wrapped in the theatrical tone that makes The Arena unique.

**Key Takeaways:**
- ✅ Natural language queries for campaign content
- ✅ Automatic spoiler prevention
- ✅ Theatrical Arena-themed experience
- ✅ Affordable hosting (~$15-70/month)
- ✅ Minimal maintenance required
- ✅ Scalable to 100+ players

**Ready to proceed?** Review the design docs and open questions, then begin Phase 1 development!

---

**Document Version:** 1.0  
**Last Updated:** 2025-11-23  
**Related:** RAG_COMPANION_APP_DESIGN.md, RAG_COMPANION_APP_SUMMARY.md
