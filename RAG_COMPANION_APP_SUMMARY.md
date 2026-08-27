# RAG Companion App - Quick Reference & Summary

> **Purpose:** This document provides a high-level summary of the RAG companion web app design for The Arena campaign. For full details, see the related design documents.

---

## 📚 Documentation Index

| Document | Purpose | Size |
|----------|---------|------|
| **RAG_COMPANION_APP_DESIGN.md** | Main architectural design, tech stack, implementation roadmap | 33KB |
| **CONTENT_METADATA_SPEC.md** | Metadata frontmatter specification for content visibility | 15KB |
| **RAG_COMPANION_APP_DIAGRAMS.md** | Visual architecture diagrams and user flows | 49KB |
| **RAG_COMPANION_APP_SUMMARY.md** (this file) | Quick reference and executive summary | - |

---

## 🎯 Project Goals

Build a React-based web companion app that allows players to:
1. **Query campaign content** via conversational AI (RAG-powered)
2. **Browse session summaries** and character histories
3. **Look up game mechanics** (Panache, Crowd's Favor, etc.)
4. **Ask strategic questions** ("How can I earn patron interest?")

**Critical Requirement:** Prevent spoilers by hiding unrevealed sessions and future plot arcs.

---

## 🏗️ Architecture at a Glance

```
Players → React SPA → Node.js API → Vector DB (Pinecone)
                                  → PostgreSQL
                                  → OpenAI GPT-4
```

### Tech Stack Summary

**Frontend:**
- React 18+ with TypeScript
- Vite for build tooling
- Tailwind CSS + shadcn/ui
- TanStack Query for server state

**Backend:**
- Node.js 20+ with Fastify/Express
- PostgreSQL + Prisma ORM
- Redis for caching
- JWT authentication

**AI/ML:**
- Pinecone vector database
- OpenAI embeddings (text-embedding-3-small)
- GPT-4 Turbo for responses

**Hosting:**
- Vercel (frontend)
- Railway/Render (backend)
- GitHub Actions (content sync)

---

## 🔒 Content Visibility System

Three-tier access control via YAML frontmatter:

### 1. **Public Content** (`visibility: public`)
- Revealed sessions (completed and debriefed)
- Published mechanics (Panache, Crowd's Favor, Last Stand)
- Active character sheets
- World lore

**Access:** All authenticated players

### 2. **Player-Specific** (`visibility: player-specific`)
- Character private notes
- Session content with character secrets
- Patron relationships

**Access:** Only character owner + GM

### 3. **Private Content** (`visibility: private`)
- Future session ideas (`ideas/` folder)
- Unrevealed plot arcs
- GM-only notes

**Access:** GM only (never indexed for players)

---

## 📝 Example Frontmatter

Every markdown file needs this at the top:

```yaml
---
visibility: public | player-specific | private
revealed: true | false
content_type: session | mechanic | npc | character | environment | idea
session_number: 3
title: "Session 3: Thunder Above, Blood Below"
participants: [imwe, torgana, orion]
tags: [combat, aerial, crowd-favor]
---
```

**Key Rule:** Content is `private` by default until explicitly revealed.

---

## 🔍 How RAG Queries Work

### User asks: "What happened to Torgana in session 3?"

**Step 1:** Classify intent (session summary for specific character)  
**Step 2:** Filter by user permissions (only public + revealed content)  
**Step 3:** Generate query embedding (OpenAI)  
**Step 4:** Search vector database (Pinecone, top-10 chunks)  
**Step 5:** Assemble context from relevant chunks  
**Step 6:** Generate dramatic response (GPT-4 with Arena system prompt)  
**Step 7:** Format with citations and wiki-links  

**Response time:** ~2-3 seconds

---

## 🎨 UI Features

### 1. Conversational Chat Interface
- Theatrical Arena-themed design
- Announcer-style AI responses
- Typewriter effect animations
- Contextual query suggestions
- Multi-turn conversations

### 2. Session Browser
- Grid view of revealed sessions
- Filter by character, date, tags
- Full markdown rendering
- Character spotlight moments

### 3. Character Dashboard
- View character stats and history
- Session participation log
- Patron relationships
- Fame/injury tracking

### 4. Mechanics Reference
- Searchable mechanics index
- Interactive examples
- Usage history from sessions

---

## 🚀 Implementation Roadmap

### Phase 1: Foundation (Weeks 1-3)
- [ ] Set up React + TypeScript project
- [ ] Build Node.js backend with API
- [ ] Configure PostgreSQL + Prisma
- [ ] Set up Pinecone vector database
- [ ] Implement content ingestion pipeline
- [ ] Create basic chat interface

### Phase 2: MVP Features (Weeks 4-5)
- [ ] Add authentication system
- [ ] Implement visibility filtering
- [ ] Build session browser UI
- [ ] Create character dashboard
- [ ] Add mechanics reference
- [ ] Polish Arena-themed design

### Phase 3: Launch (Week 6+)
- [ ] Deploy to Vercel + Railway
- [ ] Set up GitHub Actions for content sync
- [ ] User testing with players
- [ ] Monitor and iterate

---

## 💰 Cost Estimates

### MVP (Monthly)
- Vercel (frontend): **$0** (hobby tier)
- Railway (backend + DB): **$5-20**
- Pinecone (vector DB): **$0** (free tier, 100k vectors)
- Upstash Redis: **$0** (free tier)
- OpenAI API: **$10-50** (query-dependent)

**Total MVP: $15-70/month**

### Production Scale (100 users)
- Vercel: **$0**
- Railway: **$30-50**
- Pinecone: **$70** (standard tier)
- Redis: **$10**
- OpenAI: **$100-200**

**Total Production: $210-330/month**

---

## 🔐 Security & Privacy

**Authentication:**
- JWT tokens with bcrypt password hashing
- Role-based access (player, GM, admin)

**Content Security:**
- Backend enforces visibility filtering
- Separate vector DB namespaces by visibility
- Query audit logging
- No spoiler leaks via RAG responses

**API Security:**
- Rate limiting (100 queries/hour per user)
- CORS whitelisting
- Helmet.js security headers
- Input sanitization

---

## 📊 Success Metrics

**User Engagement:**
- Daily active users (DAU)
- Queries per user per session
- Average session duration

**RAG Quality:**
- Response accuracy (user ratings 1-5)
- Query resolution rate (% answered vs "I don't know")
- Average response time (target: <3 seconds)

**Content Coverage:**
- % of sessions indexed
- Time from GitHub update to RAG availability

---

## 🔄 Content Sync Workflow

```
GM updates markdown → Git push → GitHub Actions workflow
    ↓
Parse frontmatter → Chunk content → Generate embeddings
    ↓
Upsert to Pinecone → Update PostgreSQL → Invalidate cache
    ↓
Content now searchable in app (within ~30 seconds)
```

**Automation:** Fully automated via GitHub Actions on push to main branch.

---

## ❓ Open Questions for GM

1. **Character Access Model**
   - Should players see all active characters or only their own?
   - Should retired/dead characters remain accessible?

2. **Session Reveal Workflow**
   - Manual GM approval per session, or auto-reveal after date?
   - Partial reveals possible (show aftermath, hide future hooks)?

3. **Voice & Tone**
   - Always strict announcer voice, or allow neutral mode?
   - Character-perspective responses?

4. **Mobile Priority**
   - Mobile-responsive web app sufficient, or native app needed?

5. **Integrations**
   - Interest in Discord bot for quick queries?
   - VTT integration for real-time lookups?

---

## 📋 Next Steps

### Before Development:
1. ✅ Review design documents with stakeholders
2. [ ] Answer open questions about access models
3. [ ] Decide on feature priorities
4. [ ] Set up hosting accounts (Vercel, Railway, Pinecone)
5. [ ] Generate API keys (OpenAI, GitHub)

### To Start Development:
1. [ ] Initialize React project with Vite + TypeScript
2. [ ] Set up Node.js backend repository
3. [ ] Create PostgreSQL database schema
4. [ ] Configure Pinecone index
5. [ ] Begin Phase 1 implementation

---

## 🎭 Example User Queries

The app should answer questions like:

- "Summarize session 3 for me"
- "What happened to Torgana last session?"
- "How does Crowd's Favor work?"
- "What are my options for using Panache in aerial combat?"
- "Which patrons have shown interest in my character?"
- "Who died in the last session?"
- "What injuries does Imwe currently have?"
- "How can I earn more fame?"

All with dramatic, announcer-style responses and source citations!

---

## 📖 Key Design Principles

1. **Spoiler Prevention First:** Never index or reveal unrevealed content
2. **Theatrical Experience:** Match The Arena's dramatic tone in all UI/UX
3. **Accessibility:** Ensure all players can easily find information
4. **Performance:** Sub-3-second query responses
5. **Scalability:** Design for growth from 6 players to 100+
6. **Maintainability:** Automated sync, minimal manual GM intervention
7. **Mobile-Friendly:** Responsive design for on-the-go access

---

## 🛠️ Developer Quick Start (Future)

When ready to implement:

```bash
# Frontend
npm create vite@latest arena-companion -- --template react-ts
cd arena-companion
npm install @tanstack/react-query zustand tailwindcss ...

# Backend
npm init -y
npm install fastify @prisma/client @pinecone-database/pinecone openai ...
npx prisma init

# Environment
cp .env.example .env
# Add API keys: OPENAI_API_KEY, PINECONE_API_KEY, DATABASE_URL

# Run
npm run dev  # Frontend on :5173
npm run start  # Backend on :3000
```

---

## 📞 Support & Questions

For questions about this design:
- Review full design docs in this repository
- Check `AGENTS.md` for campaign context
- Consult `CONTENT_METADATA_SPEC.md` for frontmatter rules

---

**Document Version:** 1.0  
**Last Updated:** 2025-11-23  
**Status:** Design Complete, Awaiting Review  
**Next Milestone:** Stakeholder approval → Phase 1 development
