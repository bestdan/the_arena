# RAG Companion Web App - Documentation Suite

> **Complete architectural design and planning documentation for The Arena's RAG-powered web companion app.**

---

## 📋 Quick Navigation

**Start here:**
- 👉 **[Quick Summary](RAG_COMPANION_APP_SUMMARY.md)** - Executive overview and quick reference (10 min read)
- 📖 **[FAQ](RAG_COMPANION_APP_FAQ.md)** - Common questions and answers (15 min read)

**Deep dive:**
- 🏗️ **[Full Architecture Design](RAG_COMPANION_APP_DESIGN.md)** - Complete technical specification (45 min read)
- 📊 **[Visual Diagrams](RAG_COMPANION_APP_DIAGRAMS.md)** - Architecture diagrams and user flows (20 min read)
- 🏷️ **[Content Metadata Spec](CONTENT_METADATA_SPEC.md)** - Frontmatter and visibility system (25 min read)

---

## 🎯 What is This?

This documentation suite provides a **complete architectural design** for a React-based web companion app for The Arena D&D 5e campaign. The app uses RAG (Retrieval-Augmented Generation) technology to give players intelligent, conversational access to campaign content while preventing spoilers.

### Key Features
- 💬 **AI-powered chat interface** for querying sessions, mechanics, and characters
- 🔒 **Spoiler prevention** with 3-tier content visibility system
- 🎭 **Theatrical Arena-themed UI** with announcer-style responses
- 📱 **Mobile-responsive** React SPA with modern tech stack
- 🔄 **Automated sync** from GitHub repository to searchable content
- 💰 **Affordable hosting** (~$15-70/month for MVP)

---

## 📚 Document Guide

### 1. [RAG_COMPANION_APP_SUMMARY.md](RAG_COMPANION_APP_SUMMARY.md)
**Purpose:** Quick reference and executive summary  
**Audience:** Everyone (stakeholders, developers, players)  
**Contains:**
- Documentation index
- Project goals and architecture overview
- Tech stack summary
- Content visibility system
- Implementation roadmap
- Cost estimates
- Next steps

**Read this first** if you want a high-level understanding without diving into details.

---

### 2. [RAG_COMPANION_APP_FAQ.md](RAG_COMPANION_APP_FAQ.md)
**Purpose:** Answer common questions  
**Audience:** GMs, developers, stakeholders  
**Contains:**
- General questions (What is RAG? Why not just use ChatGPT?)
- Content & visibility (How to reveal sessions, prevent spoilers)
- Technical questions (Why React? Why Pinecone? Self-hosting?)
- Features & functionality (Mobile support, integrations)
- Cost & scaling (Free tier limits, bandwidth usage)
- Development & maintenance (Build time, backups)
- User experience (Wrong answers, accessibility)
- Troubleshooting

**Read this** if you have specific questions about any aspect of the design.

---

### 3. [RAG_COMPANION_APP_DESIGN.md](RAG_COMPANION_APP_DESIGN.md)
**Purpose:** Complete architectural specification  
**Audience:** Developers, technical stakeholders  
**Contains:**
- Executive summary
- System architecture overview (diagrams + explanations)
- Content visibility & access control strategy
- RAG implementation architecture (vector DB, embeddings, query pipeline)
- React frontend architecture (components, state, UI)
- Backend API design (endpoints, database schema, query logic)
- Data ingestion & synchronization pipeline
- Deployment architecture
- Security & privacy considerations
- Feature specifications (MVP, Phase 2, Phase 3)
- Technical stack summary
- Implementation roadmap (6-week timeline)
- Cost estimates (monthly, scaling)
- Success metrics
- Open questions for GM review
- Example user flows

**Read this** if you're building the app or need full technical details.

---

### 4. [RAG_COMPANION_APP_DIAGRAMS.md](RAG_COMPANION_APP_DIAGRAMS.md)
**Purpose:** Visual architecture diagrams and flows  
**Audience:** Developers, visual learners  
**Contains:**
- System component diagram (ASCII art)
- RAG query flow (step-by-step with examples)
- Content visibility access matrix
- User journey diagrams (player onboarding, mechanics exploration, strategic planning)
- Content synchronization flow (GitHub → Vector DB)
- Tech stack component map

**Read this** if you prefer visual explanations or need to understand data flows.

---

### 5. [CONTENT_METADATA_SPEC.md](CONTENT_METADATA_SPEC.md)
**Purpose:** Metadata system specification for content visibility  
**Audience:** GMs, content creators, developers  
**Contains:**
- Frontmatter schema (YAML format)
- Visibility levels explained (public, player-specific, private)
- Content type specifications (session, mechanic, NPC, character, etc.)
- Migration strategy for existing files
- Validation scripts
- Tag taxonomy
- Example annotated files
- Automated frontmatter generation
- RAG ingestion behavior by visibility
- Future enhancements

**Read this** if you're managing campaign content or setting up the ingestion pipeline.

---

## 🚀 Getting Started

### For Stakeholders & GMs

1. **Read:** [Quick Summary](RAG_COMPANION_APP_SUMMARY.md) (10 min)
2. **Review:** Open questions at end of [Full Design](RAG_COMPANION_APP_DESIGN.md)
3. **Decide:** Feature priorities and access model preferences
4. **Approve:** Move forward with Phase 1 development

### For Developers

1. **Read:** [Quick Summary](RAG_COMPANION_APP_SUMMARY.md) for context
2. **Study:** [Full Architecture Design](RAG_COMPANION_APP_DESIGN.md) for technical details
3. **Review:** [Visual Diagrams](RAG_COMPANION_APP_DIAGRAMS.md) for data flows
4. **Understand:** [Content Metadata Spec](CONTENT_METADATA_SPEC.md) for ingestion pipeline
5. **Reference:** [FAQ](RAG_COMPANION_APP_FAQ.md) for implementation questions
6. **Build:** Follow Phase 1 roadmap in design document

### For Content Creators

1. **Read:** [Content Metadata Spec](CONTENT_METADATA_SPEC.md)
2. **Learn:** How to add frontmatter to markdown files
3. **Understand:** Visibility levels (public, player-specific, private)
4. **Practice:** Add metadata to one session file
5. **Validate:** Use provided validation scripts
6. **Apply:** Add frontmatter to all campaign content

---

## 📊 Project Status

**Current Phase:** ✅ Design Complete  
**Next Phase:** ⏳ Awaiting stakeholder review  
**Timeline:** 6 weeks to MVP (Phase 1-3)  
**Estimated Cost:** $15-70/month for MVP

---

## 🎯 Design Goals Achieved

- ✅ React-based web app architecture
- ✅ RAG system for intelligent content queries
- ✅ 3-tier content visibility system (prevents spoilers)
- ✅ Automated GitHub sync pipeline
- ✅ Mobile-responsive UI design
- ✅ Theatrical Arena-themed UX
- ✅ Scalable architecture (6 to 100+ players)
- ✅ Affordable hosting strategy
- ✅ No code written (design-only per issue request)

---

## 🔑 Key Technologies

**Frontend:**
- React 18+ with TypeScript
- Vite, Tailwind CSS, shadcn/ui
- TanStack Query, Zustand

**Backend:**
- Node.js 20+ with Fastify/Express
- PostgreSQL + Prisma ORM
- Redis (Upstash)

**AI/ML:**
- Pinecone vector database
- OpenAI embeddings + GPT-4
- RAG query pipeline

**Hosting:**
- Vercel (frontend)
- Railway/Render (backend)
- GitHub Actions (CI/CD)

---

## 💡 Core Concepts

### RAG (Retrieval-Augmented Generation)
Instead of the AI making things up, it:
1. Searches your campaign content for relevant information
2. Uses that content to inform its response
3. Cites sources so you can verify accuracy

### Content Visibility System
Three tiers protect against spoilers:
- **Public:** Revealed sessions, published mechanics (all players)
- **Player-Specific:** Character notes, private moments (owner only)
- **Private:** Future sessions, GM notes (GM only)

### Automated Sync
When you push to GitHub:
1. GitHub Actions detects changed files
2. Parses frontmatter for visibility settings
3. Chunks and embeds content
4. Upserts to vector database
5. Updates searchable in ~30 seconds

---

## 📞 Questions & Feedback

### Have Questions?
- Check the [FAQ](RAG_COMPANION_APP_FAQ.md) first
- Review the [Full Design](RAG_COMPANION_APP_DESIGN.md) for technical details
- Consult [Content Metadata Spec](CONTENT_METADATA_SPEC.md) for frontmatter questions

### Provide Feedback
- Answer open questions in [Full Design](RAG_COMPANION_APP_DESIGN.md)
- Suggest feature priorities
- Review cost estimates and timeline
- Approve or request changes to architecture

### Ready to Build?
- Follow "Developer Quick Start" in [Summary](RAG_COMPANION_APP_SUMMARY.md)
- Set up hosting accounts (Vercel, Railway, Pinecone)
- Generate API keys (OpenAI, GitHub)
- Begin Phase 1 implementation

---

## 📖 Additional Context

For campaign-specific context and guidelines:
- **[AGENTS.md](AGENTS.md)** - Main campaign instructions for AI agents
- **[README.md](README.md)** - The Arena campaign overview
- **[environment/the_empire.md](environment/the_empire.md)** - World lore
- **[mechanics/](mechanics/)** - Custom game mechanics

---

## 🎭 About The Arena

The Arena is a D&D 5e gladiatorial campaign where:
- Players are gladiators fighting for fame and freedom
- Showmanship matters as much as combat skill
- Custom mechanics reward dramatic moments
- Real consequences (injuries, death) drive the narrative
- Theatrical announcer-style narration creates immersive atmosphere

This companion app extends that theatrical experience to help players explore the campaign world intelligently without spoiling future content.

---

## ✅ Checklist for Stakeholders

Before approving development:

- [ ] Review [Quick Summary](RAG_COMPANION_APP_SUMMARY.md)
- [ ] Understand [Content Metadata Spec](CONTENT_METADATA_SPEC.md)
- [ ] Check [FAQ](RAG_COMPANION_APP_FAQ.md) for questions
- [ ] Review cost estimates in [Full Design](RAG_COMPANION_APP_DESIGN.md)
- [ ] Answer open questions (access models, feature priorities)
- [ ] Approve architecture and tech stack
- [ ] Confirm budget and timeline
- [ ] Decide on hosting providers
- [ ] Generate necessary API keys
- [ ] Greenlight Phase 1 development

---

## 🔄 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-23 | Initial design complete - all 5 documents |

---

## 📄 License

This documentation is part of The Arena campaign repository and follows the same license as the main project.

---

**Ready to build the future of campaign companions?** Start with the [Quick Summary](RAG_COMPANION_APP_SUMMARY.md)!

---

*Generated by GitHub Copilot for @bestdan | The Arena Campaign*
