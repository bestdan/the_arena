# RAG Companion Web App - Architecture & Design

## Executive Summary

This document outlines the architectural design for a React-based web companion app for The Arena D&D 5e gladiatorial campaign. The app provides players with intelligent, context-aware access to campaign materials through a conversational RAG (Retrieval-Augmented Generation) interface while maintaining strict content visibility controls to prevent spoilers.

**Key Goals:**
- Provide players with an AI-powered interface to query session summaries, character notes, and game mechanics
- Enable discovery of strategic options (e.g., "How can I use Crowd's Favor to make an ally?")
- Maintain strict separation between public content (revealed sessions/mechanics) and private content (future plot arcs)
- Deliver a modern, theatrical user experience matching The Arena's dramatic tone

---

## System Architecture Overview

### High-Level Components

```
┌─────────────────────────────────────────────────────────────┐
│                      React Frontend (SPA)                    │
│  - Conversational UI                                         │
│  - Session browsing interface                                │
│  - Character sheets viewer                                   │
│  - Mechanics reference                                       │
└────────────────┬────────────────────────────────────────────┘
                 │
                 │ REST API / WebSocket
                 │
┌────────────────▼────────────────────────────────────────────┐
│                    Backend API Server                        │
│  - Express.js/Fastify Node.js server                        │
│  - Authentication & session management                       │
│  - Content visibility control layer                          │
│  - Query processing & orchestration                          │
└────────────────┬────────────────────────────────────────────┘
                 │
      ┌──────────┴──────────┬──────────────────┐
      │                     │                  │
┌─────▼─────┐      ┌────────▼──────┐   ┌──────▼────────┐
│  Vector   │      │   LLM Service  │   │  GitHub Sync  │
│  Database │      │   (OpenAI/     │   │   Service     │
│ (Pinecone/│      │   Anthropic)   │   │               │
│  Weaviate)│      └────────────────┘   └───────────────┘
└───────────┘
```

---

## Content Visibility & Access Control Strategy

### Content Classification System

All repository content is classified into three visibility tiers:

#### 1. **Public Content** (Always Accessible)
- Completed session notes (`sessions/session_*.md` marked as "revealed")
- Published mechanics (`mechanics/*.md`)
- Revealed NPC profiles
- Active player characters (`player_characters/*.md`)
- World/environment lore (`environment/*.md`)

#### 2. **Player-Specific Content** (Conditional Access)
- Individual character sheets (only owner can see private notes)
- Session summaries for sessions the character participated in
- Patron interactions specific to that character

#### 3. **Private Content** (GM-Only, Never Indexed)
- Future session plans in `ideas/` folder
- Unrevealed sessions (flagged in metadata)
- GM notes and secret NPC motivations
- Upcoming plot arcs and twists

### Implementation Approach

**Metadata-Driven Visibility:**
Add frontmatter to each markdown file:

```yaml
---
visibility: public | player-specific | private
revealed: true | false
session_number: 3
participants: ["imwe", "torgana", "orion"]
date_revealed: 2025-11-15
tags: ["combat", "crowd-favor", "patron-interaction"]
---
```

**Access Control Layer:**
- Backend middleware filters content before RAG indexing
- Separate vector databases/namespaces for different visibility tiers
- Query-time filtering based on user authentication/permissions
- Automatic content promotion (private → public) via GitHub Actions when GM marks session as revealed

---

## RAG Implementation Architecture

### Vector Database Strategy

**Recommended: Pinecone or Weaviate**
- Cloud-hosted, scalable vector storage
- Built-in filtering on metadata
- Support for hybrid search (semantic + keyword)

**Data Structure:**

```javascript
{
  id: "session_3_setup_chunk_5",
  vector: [0.234, -0.567, ...],  // OpenAI embedding
  metadata: {
    source_file: "sessions/session_3_setup.md",
    visibility: "public",
    revealed: true,
    content_type: "session",
    session_number: 3,
    tags: ["combat", "announcer-dialogue"],
    participants: ["imwe", "torgana"],
    chunk_index: 5,
    total_chunks: 12
  },
  text: "The announcer's voice booms..."
}
```

### Chunking Strategy

**Smart Semantic Chunking:**
- Split on markdown headings (H2/H3 boundaries)
- Preserve announcer dialogue blocks as complete units
- Keep stat blocks and mechanic descriptions intact
- Max chunk size: ~500 tokens with 50-token overlap
- Include metadata about surrounding context in each chunk

### Embedding Generation

**Recommended: OpenAI text-embedding-3-small**
- Cost-effective ($0.02/1M tokens)
- 1536 dimensions, high quality
- Fast inference

**Alternative: Cohere embed-english-v3.0**
- Competitive pricing
- Built-in compression options

### RAG Query Pipeline

```
User Query
    ↓
1. Query Classification
   - Intent detection (summary request, mechanics question, strategy query)
   - Entity extraction (character names, session numbers, mechanics)
    ↓
2. Query Embedding + Metadata Filtering
   - Generate query embedding
   - Apply visibility filters (user's access level)
   - Add semantic filters (e.g., only "mechanics" content)
    ↓
3. Vector Similarity Search
   - Top-k retrieval (k=5-10 chunks)
   - Hybrid search: vector similarity + keyword matching
   - Re-ranking based on recency/relevance
    ↓
4. Context Assembly
   - Retrieve full surrounding context for top chunks
   - Assemble chronologically/thematically
   - Inject relevant mechanics definitions
    ↓
5. LLM Response Generation
   - Use GPT-4 or Claude with campaign-aware system prompt
   - Include retrieved chunks as context
   - Format response in theatrical Arena tone
   - Add citations to source documents
    ↓
6. Response Post-Processing
   - Convert wiki-links to clickable UI elements
   - Highlight key mechanics terms
   - Add "Learn More" links to full source documents
```

---

## React Frontend Architecture

### Technology Stack

**Core Framework:**
- **React 18+** with TypeScript
- **Vite** for build tooling (fast HMR, optimized builds)
- **React Router v6** for navigation

**State Management:**
- **Zustand** or **Jotai** (lightweight, modern)
- Server state: **TanStack Query (React Query)**

**UI Framework:**
- **Tailwind CSS** for styling
- **shadcn/ui** component library (accessible, customizable)
- **Framer Motion** for theatrical animations

**Additional Libraries:**
- **react-markdown** + **remark/rehype** for rendering markdown
- **react-syntax-highlighter** for stat blocks
- **socket.io-client** for real-time updates

### Component Structure

```
src/
├── components/
│   ├── chat/
│   │   ├── ChatInterface.tsx          # Main conversational UI
│   │   ├── MessageList.tsx            # Message history
│   │   ├── MessageBubble.tsx          # Individual message
│   │   ├── QueryInput.tsx             # User input with suggestions
│   │   └── SourceCitation.tsx         # Links to source documents
│   ├── browser/
│   │   ├── SessionBrowser.tsx         # Browse completed sessions
│   │   ├── SessionCard.tsx            # Session preview card
│   │   ├── CharacterViewer.tsx        # View character sheets
│   │   └── MechanicsReference.tsx     # Browse mechanics docs
│   ├── layout/
│   │   ├── AppShell.tsx               # Main app layout
│   │   ├── Sidebar.tsx                # Navigation sidebar
│   │   └── AnnouncerHeader.tsx        # Theatrical header component
│   └── shared/
│       ├── MarkdownRenderer.tsx       # Render campaign markdown
│       ├── WikiLink.tsx               # Handle [[wiki]] links
│       └── LoadingSpinner.tsx         # Arena-themed loading
├── features/
│   ├── auth/                          # Authentication logic
│   ├── chat/                          # Chat feature state
│   └── content/                       # Content browsing state
├── hooks/
│   ├── useChat.ts                     # Chat interaction hook
│   ├── useSessionData.ts              # Fetch session data
│   └── useCharacter.ts                # Character data hook
├── services/
│   ├── api.ts                         # API client
│   ├── websocket.ts                   # WebSocket connection
│   └── markdown.ts                    # Markdown processing
├── stores/
│   ├── authStore.ts                   # Auth state
│   └── appStore.ts                    # App-level state
├── types/
│   └── index.ts                       # TypeScript definitions
└── utils/
    ├── formatting.ts                  # Text formatting
    └── constants.ts                   # App constants
```

### Key UI Features

#### 1. Conversational Chat Interface

**Primary interaction mode:**
- Theatrical, Arena-themed design with announcer-style flourishes
- Animated message delivery (typewriter effect for drama)
- Contextual suggestions: "Ask about..." based on recent content
- Multi-turn conversations with memory
- Voice of the announcer for AI responses

**Example Queries:**
- "Summarize session 3 for me"
- "What happened to Torgana last session?"
- "How does Crowd's Favor work?"
- "What are my options for using Panache in an aerial combat?"
- "Which patrons have shown interest in my character?"

**Response Format:**
```
[Dramatic announcer-style opening]

[Core answer with citations]

[Related mechanics or suggestions]

📜 Sources:
  - Session 3: Thunder and Blood
  - Crowd's Favor Mechanic
```

#### 2. Session Browser

- Grid/list view of revealed sessions
- Filter by: participant, date, session number, tags
- Preview cards with announcer excerpt + outcome summary
- Full session view with rendered markdown
- Character spotlight: highlight moments for specific characters

#### 3. Character Dashboard

- View your character sheet with latest stats
- Session history participation log
- Patron relationships tracker
- Injury/status tracking
- Fame and reputation meter

#### 4. Mechanics Reference

- Searchable index of custom mechanics
- Interactive examples
- "How would this work if..." simulator suggestions
- Cross-references to sessions where mechanic was used

### Theatrical UI Design Elements

**Color Palette (Arena-themed):**
- Primary: Deep crimson (#8B0000) and gold (#FFD700)
- Background: Dark stone gray (#2C2C2C)
- Accents: Arena sand (#D4A76A), blood red (#CC0000)
- Text: Parchment white (#F5F5DC)

**Typography:**
- Headers: Cinzel or Crimson Text (theatrical serif)
- Body: Inter or Open Sans (readable sans-serif)
- Announcer dialogue: Spectral or Playfair Display (dramatic)

**Animations:**
- Announcer text: Fade-in with slight scale
- Message delivery: Slide up from bottom
- Page transitions: Curtain wipe effect
- Loading states: Arena gates opening animation

---

## Backend API Design

### Technology Stack

**Runtime & Framework:**
- **Node.js 20+** with TypeScript
- **Fastify** (high performance) or **Express.js** (ecosystem maturity)
- **Prisma** ORM for database interactions

**Additional Services:**
- **Bull** or **BullMQ** for background job processing
- **Redis** for caching and session storage
- **Winston** for logging
- **Helmet** for security headers

### API Endpoints

#### Authentication & User Management

```typescript
POST   /api/auth/login              // Player login
POST   /api/auth/logout             // Logout
GET    /api/auth/me                 // Current user info
GET    /api/auth/characters         // User's characters
```

#### Chat & Query Interface

```typescript
POST   /api/chat/query              // Submit RAG query
GET    /api/chat/history            // Conversation history
POST   /api/chat/feedback           // Rate response quality
WS     /api/chat/stream             // Streaming responses
```

#### Content Browsing

```typescript
GET    /api/sessions                // List revealed sessions
GET    /api/sessions/:id            // Get session details
GET    /api/characters/:id          // Get character data
GET    /api/mechanics               // List mechanics
GET    /api/mechanics/:slug         // Get mechanic details
GET    /api/npcs                    // List revealed NPCs
```

#### Admin Endpoints (GM Only)

```typescript
POST   /api/admin/reveal-session   // Mark session as public
POST   /api/admin/sync-content     // Trigger GitHub sync
GET    /api/admin/analytics        // Usage analytics
```

### Database Schema

**Primary Database: PostgreSQL**

```sql
-- Users (players)
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role VARCHAR(20) DEFAULT 'player', -- player, gm, admin
  created_at TIMESTAMP DEFAULT NOW()
);

-- Characters (links users to their PCs)
CREATE TABLE characters (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  name VARCHAR(100) NOT NULL,
  class VARCHAR(50),
  level INTEGER DEFAULT 1,
  status VARCHAR(20) DEFAULT 'active', -- active, injured, dead
  fame_level INTEGER DEFAULT 0,
  metadata JSONB, -- flexible storage for stats, notes
  created_at TIMESTAMP DEFAULT NOW()
);

-- Sessions (tracking revealed content)
CREATE TABLE sessions (
  id SERIAL PRIMARY KEY,
  session_number INTEGER UNIQUE NOT NULL,
  title VARCHAR(255),
  file_path VARCHAR(500),
  visibility VARCHAR(20) DEFAULT 'private', -- public, private
  revealed_at TIMESTAMP,
  participants JSONB, -- array of character IDs
  tags JSONB, -- array of tag strings
  summary TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Chat history
CREATE TABLE chat_messages (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  character_id INTEGER REFERENCES characters(id),
  query TEXT NOT NULL,
  response TEXT NOT NULL,
  sources JSONB, -- array of source document references
  feedback INTEGER, -- 1-5 rating
  created_at TIMESTAMP DEFAULT NOW()
);

-- Content metadata (tracks all indexed content)
CREATE TABLE content_metadata (
  id SERIAL PRIMARY KEY,
  file_path VARCHAR(500) UNIQUE NOT NULL,
  content_type VARCHAR(50), -- session, mechanic, npc, character
  visibility VARCHAR(20) DEFAULT 'private',
  title VARCHAR(255),
  tags JSONB,
  last_synced_at TIMESTAMP,
  github_sha VARCHAR(40), -- track changes
  created_at TIMESTAMP DEFAULT NOW()
);
```

### RAG Query Processing Logic

```typescript
interface RAGQueryRequest {
  query: string;
  character_id?: number;
  max_results?: number;
  content_types?: string[]; // filter by type
}

interface RAGQueryResponse {
  answer: string;
  sources: SourceReference[];
  suggestions: string[];
  processing_time_ms: number;
}

async function processRAGQuery(
  req: RAGQueryRequest,
  user: User
): Promise<RAGQueryResponse> {
  
  // 1. Classify query intent
  const intent = await classifyQuery(req.query);
  
  // 2. Build metadata filters based on user permissions
  const filters = {
    visibility: ['public'],
    // Add character-specific content if querying about own character
    ...(req.character_id && {
      OR: [
        { visibility: 'public' },
        { 
          visibility: 'player-specific',
          participants: { contains: req.character_id }
        }
      ]
    })
  };
  
  // 3. Generate embedding for query
  const queryEmbedding = await generateEmbedding(req.query);
  
  // 4. Vector search with metadata filtering
  const chunks = await vectorDB.query({
    vector: queryEmbedding,
    filter: filters,
    topK: 10,
    includeMetadata: true
  });
  
  // 5. Re-rank results
  const rerankedChunks = await rerankByRelevance(chunks, req.query);
  
  // 6. Assemble context
  const context = await assembleContext(rerankedChunks.slice(0, 5));
  
  // 7. Generate response with LLM
  const systemPrompt = buildArenaSystemPrompt(user, intent);
  const response = await generateLLMResponse({
    systemPrompt,
    context,
    query: req.query,
    streamCallback: // ... for streaming responses
  });
  
  // 8. Extract citations and format
  const sources = extractSources(rerankedChunks);
  const suggestions = generateSuggestions(intent, sources);
  
  return {
    answer: response,
    sources,
    suggestions,
    processing_time_ms: performance.now() - startTime
  };
}
```

### System Prompts for Arena Tone

```typescript
const ARENA_SYSTEM_PROMPT = `
You are the Arena Chronicler, an AI assistant for "The Arena" D&D 5e gladiatorial campaign.

VOICE & TONE:
- Write with theatrical flair, matching the announcer's dramatic style
- Use present tense for describing past events to maintain immediacy
- Reference the crowd, the sand, and the spectacle when relevant
- Show consequences: injuries matter, deaths are permanent, reputation shifts

CONSTRAINTS:
- Only use information from the provided context documents
- If information isn't in the context, say so clearly
- Never speculate about future sessions or unrevealed plot points
- Cite specific sessions or mechanics documents when answering

FORMAT:
- Lead with a dramatic hook or announcer-style opening
- Provide the core answer clearly
- Include relevant mechanics or cross-references
- End with related suggestions or questions the player might ask next
- Add source citations in a "Sources" section

Remember: You're helping players understand what HAS happened and what mechanics ARE available, not predicting what WILL happen.
`;
```

---

## Data Ingestion & Synchronization Pipeline

### GitHub Integration Strategy

**Automated Sync via GitHub Actions:**

```yaml
# .github/workflows/sync-content.yml
name: Sync Content to RAG Database

on:
  push:
    branches: [main]
    paths:
      - 'sessions/**'
      - 'mechanics/**'
      - 'npcs/**'
      - 'player_characters/**'
      - 'environment/**'
  workflow_dispatch: # Manual trigger

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Detect changed files
        id: changes
        run: |
          # Get list of changed markdown files
          
      - name: Process changed files
        run: |
          # Extract metadata from frontmatter
          # Split into chunks
          # Generate embeddings
          
      - name: Update vector database
        env:
          PINECONE_API_KEY: ${{ secrets.PINECONE_API_KEY }}
        run: |
          # Upsert vectors to Pinecone
          # Update PostgreSQL metadata
          
      - name: Notify webhook
        run: |
          # Trigger backend to refresh content cache
```

### Content Processing Pipeline

```typescript
// Ingestion workflow
async function ingestMarkdownFile(filePath: string) {
  
  // 1. Read file and parse frontmatter
  const { content, metadata } = await parseMarkdownWithFrontmatter(filePath);
  
  // 2. Validate visibility settings
  if (!metadata.visibility) {
    metadata.visibility = 'private'; // default to private
  }
  
  // 3. Skip if marked as private
  if (metadata.visibility === 'private' && metadata.revealed !== true) {
    console.log(`Skipping private content: ${filePath}`);
    return;
  }
  
  // 4. Smart chunking
  const chunks = await chunkMarkdown(content, {
    preserveAnnouncerBlocks: true,
    preserveStatBlocks: true,
    maxTokens: 500,
    overlap: 50
  });
  
  // 5. Generate embeddings for each chunk
  const embeddings = await generateEmbeddings(
    chunks.map(c => c.text)
  );
  
  // 6. Prepare vector records
  const vectors = chunks.map((chunk, idx) => ({
    id: `${filePath}_chunk_${idx}`,
    values: embeddings[idx],
    metadata: {
      source_file: filePath,
      visibility: metadata.visibility,
      revealed: metadata.revealed,
      content_type: detectContentType(filePath),
      session_number: metadata.session_number,
      participants: metadata.participants,
      tags: metadata.tags,
      chunk_index: idx,
      total_chunks: chunks.length,
      text: chunk.text
    }
  }));
  
  // 7. Upsert to vector database
  await vectorDB.upsert({ vectors });
  
  // 8. Update content metadata in PostgreSQL
  await db.content_metadata.upsert({
    where: { file_path: filePath },
    update: {
      visibility: metadata.visibility,
      title: metadata.title || extractTitle(content),
      tags: metadata.tags,
      last_synced_at: new Date(),
      github_sha: await getGitSHA(filePath)
    },
    create: { /* ... */ }
  });
}
```

### Incremental Updates

- Track GitHub commit SHA for each file
- Only re-process files that have changed
- Delete old vectors and insert new ones (upsert)
- Maintain version history for rollback capability

---

## Deployment Architecture

### Recommended Hosting Strategy

**Frontend (React SPA):**
- **Vercel** or **Netlify** for static hosting
  - Automatic deployments from Git
  - Edge caching and CDN
  - Preview deployments for PRs
  - Custom domain support

**Backend API:**
- **Railway** or **Render** for containerized backend
  - Automatic scaling
  - Managed PostgreSQL instances
  - Simple environment variable management
  - Affordable for hobby/small projects

**Alternative: All-in-one on Vercel:**
- Use Vercel serverless functions for backend
- Simpler deployment but less control
- Good for MVP, may need migration later for scale

**Vector Database:**
- **Pinecone** free tier (100k vectors, 1 pod)
- Upgrade to paid tier as content grows

**Redis Cache:**
- **Upstash** serverless Redis (free tier available)
- Or included with Railway/Render hosting

### Environment Configuration

```env
# Frontend (.env)
VITE_API_BASE_URL=https://api.arena-companion.com
VITE_WS_URL=wss://api.arena-companion.com
VITE_ENVIRONMENT=production

# Backend (.env)
NODE_ENV=production
PORT=3000

# Database
DATABASE_URL=postgresql://user:pass@host:5432/arena_companion
REDIS_URL=redis://user:pass@host:6379

# Vector DB
PINECONE_API_KEY=xxxxx
PINECONE_ENVIRONMENT=us-east-1-aws
PINECONE_INDEX=arena-companion

# LLM Service
OPENAI_API_KEY=sk-xxxxx
# or
ANTHROPIC_API_KEY=sk-ant-xxxxx

# GitHub Integration
GITHUB_TOKEN=ghp_xxxxx
GITHUB_REPO=bestdan/the_arena
GITHUB_BRANCH=main

# Auth
JWT_SECRET=xxxxx
SESSION_SECRET=xxxxx

# Admin
ADMIN_EMAIL=gm@arena.com
```

### Deployment Pipeline

```
Git Push (main branch)
    ↓
GitHub Actions Workflow
    ├─> Build Frontend (Vite)
    │   └─> Deploy to Vercel
    │
    ├─> Build Backend (TypeScript)
    │   └─> Deploy to Railway
    │
    └─> Sync Content Pipeline
        ├─> Process changed markdown files
        ├─> Update vector database
        └─> Invalidate frontend cache
```

---

## Security & Privacy Considerations

### Authentication & Authorization

**Player Authentication:**
- JWT-based authentication
- Secure password hashing (bcrypt, cost factor 12+)
- Optional: OAuth integration (Google, Discord)
- Session expiration and refresh tokens

**Role-Based Access Control (RBAC):**
- **Player:** Access to public content + own character's content
- **GM:** Full access to all content + admin functions
- **Guest:** Read-only access to public content only (optional)

### Content Security

**Preventing Spoiler Leaks:**
- All RAG queries filtered by user's access level at query time
- Separate vector database namespaces for visibility tiers
- Backend validation: never trust frontend visibility filtering
- Audit logging of all queries for suspicious access attempts

**Data Privacy:**
- Player queries are logged but can be optionally anonymized
- Character-specific notes remain private
- GDPR compliance: user data export and deletion capabilities
- No sharing of query data across users

### API Security

- Rate limiting (100 queries/hour per user)
- CORS configuration (whitelist frontend domain)
- Helmet.js security headers
- Input sanitization and validation
- SQL injection prevention (Prisma parameterized queries)
- XSS protection in markdown rendering

---

## Feature Specifications

### MVP Features (Phase 1)

**Must-Have for Launch:**

1. **Conversational RAG Interface**
   - Text-based query input
   - AI-generated responses with citations
   - Session summaries on demand
   - Mechanics explanations

2. **Session Browser**
   - List of revealed sessions
   - Full session content rendering
   - Search and filter

3. **Character Dashboard**
   - View basic character stats
   - Session participation history

4. **Mechanics Reference**
   - Browse Panache, Crowd's Favor, Last Stand
   - Search mechanics by keyword

5. **Authentication**
   - Login/logout
   - Character association

### Enhanced Features (Phase 2)

**After MVP Validation:**

6. **Advanced Query Features**
   - Multi-turn conversations with memory
   - "What if" scenario exploration
   - Strategic suggestions ("Best ways to earn patron interest")

7. **Character Progression Tracking**
   - Fame meter visualization
   - Injury/death timeline
   - Patron relationship network graph

8. **Social Features**
   - Share interesting moments from sessions
   - Collaborative session notes/highlights
   - Player-to-player character connections

9. **GM Dashboard**
   - Content visibility management UI
   - Analytics on player engagement
   - Quick reveal/hide session controls

### Future Enhancements (Phase 3)

10. **Voice Interface**
    - Voice query input
    - Text-to-speech responses in announcer voice

11. **Mobile App**
    - React Native companion app
    - Offline mode with cached content

12. **Enhanced Visualizations**
    - Arena battle map viewer
    - Character stat progression charts
    - Crowd favor heat maps

13. **Integration Features**
    - Discord bot integration
    - Roll20/Foundry VTT hooks
    - Automated session note generation

---

## Technical Stack Summary

### Frontend
- **Framework:** React 18+ with TypeScript
- **Build Tool:** Vite
- **Routing:** React Router v6
- **State Management:** Zustand + TanStack Query
- **UI Library:** Tailwind CSS + shadcn/ui
- **Animations:** Framer Motion
- **Markdown:** react-markdown + remark/rehype

### Backend
- **Runtime:** Node.js 20+ with TypeScript
- **Framework:** Fastify or Express.js
- **Database:** PostgreSQL 15+
- **ORM:** Prisma
- **Cache:** Redis (Upstash)
- **Background Jobs:** BullMQ
- **Authentication:** JWT + bcrypt

### AI/ML Services
- **Vector Database:** Pinecone (or Weaviate)
- **Embeddings:** OpenAI text-embedding-3-small
- **LLM:** GPT-4 or Claude 3.5 Sonnet
- **Alternative:** Local embeddings with sentence-transformers

### DevOps
- **Frontend Hosting:** Vercel or Netlify
- **Backend Hosting:** Railway or Render
- **CI/CD:** GitHub Actions
- **Monitoring:** Sentry (errors) + Vercel Analytics
- **Logging:** Winston + cloud provider logs

---

## Implementation Roadmap

### Phase 1: Foundation (Weeks 1-3)

**Week 1: Setup & Infrastructure**
- [ ] Initialize React project with Vite + TypeScript
- [ ] Set up Fastify backend with TypeScript
- [ ] Configure PostgreSQL database with Prisma
- [ ] Set up Pinecone vector database
- [ ] Establish GitHub repository structure

**Week 2: Core RAG Pipeline**
- [ ] Implement markdown parsing with frontmatter
- [ ] Build content ingestion pipeline
- [ ] Create chunking and embedding generation
- [ ] Set up vector upsert workflow
- [ ] Test RAG retrieval accuracy

**Week 3: Basic UI + Backend API**
- [ ] Build chat interface component
- [ ] Implement query processing endpoint
- [ ] Create authentication system
- [ ] Build session browser UI
- [ ] Connect frontend to backend

### Phase 2: MVP Features (Weeks 4-5)

**Week 4: Content & Features**
- [ ] Ingest all public sessions and mechanics
- [ ] Implement visibility filtering
- [ ] Build character dashboard
- [ ] Add mechanics reference browser
- [ ] Create source citation system

**Week 5: Polish & Testing**
- [ ] Refine Arena-themed UI design
- [ ] Add announcer-style response formatting
- [ ] Implement rate limiting and security
- [ ] User testing with players
- [ ] Bug fixes and performance optimization

### Phase 3: Launch & Iteration (Week 6+)

**Week 6: Deployment**
- [ ] Deploy frontend to Vercel
- [ ] Deploy backend to Railway
- [ ] Configure custom domain
- [ ] Set up monitoring and logging
- [ ] Document user guide

**Ongoing: Enhancements**
- [ ] Gather user feedback
- [ ] Iterate on response quality
- [ ] Add Phase 2 features based on usage
- [ ] Expand content coverage
- [ ] Optimize costs and performance

---

## Cost Estimates (Monthly)

### MVP Hosting
- **Vercel** (Frontend): $0 (hobby tier sufficient)
- **Railway** (Backend + DB): $5-20 (scales with usage)
- **Pinecone** (Vector DB): $0 (free tier, 100k vectors)
- **Upstash Redis**: $0 (free tier)
- **OpenAI API**: $10-50 (depends on query volume)
  - Embeddings: ~$0.02/1M tokens
  - GPT-4 responses: ~$0.03/1k tokens input + $0.06/1k output

**Total MVP: $15-70/month**

### Production Scale (100 active users)
- **Vercel**: $0 (still within hobby limits)
- **Railway**: $30-50 (larger DB instance)
- **Pinecone**: $70 (standard tier, better performance)
- **Redis**: $10 (Upstash paid tier)
- **OpenAI API**: $100-200 (higher query volume)

**Total Production: $210-330/month**

### Cost Optimization Strategies
- Cache frequent queries to reduce LLM calls
- Use smaller embedding models (OpenAI small vs large)
- Implement query deduplication
- Consider self-hosted vector DB for scale (Qdrant, Milvus)

---

## Success Metrics

### User Engagement
- **Daily Active Users (DAU)**
- **Queries per user per session**
- **Session browser page views**
- **Average session duration**

### RAG Quality
- **Response accuracy** (user feedback ratings)
- **Source citation relevance** (manual review)
- **Query resolution rate** (% of queries answered vs "I don't know")
- **Average response time** (target: <3 seconds)

### Content Coverage
- **% of sessions indexed and searchable**
- **% of mechanics covered in RAG responses**
- **Freshness**: Time from GitHub update to available in RAG

### Player Satisfaction
- **User feedback scores** (1-5 stars)
- **Feature requests and bug reports**
- **Retention rate** (% returning users week-over-week)

---

## Open Questions for GM Review

1. **Character Access Model:**
   - Should players only access data about their own characters, or see all active characters?
   - Should retired/dead character data remain accessible to their original players?

2. **Session Reveal Workflow:**
   - Manual GM approval per session, or automatic reveal after session date?
   - Should partial reveals be possible (e.g., show aftermath but hide future hooks)?

3. **Social Features Priority:**
   - Interest in player-to-player sharing/discussion features?
   - Value of collaborative session note-taking?

4. **Voice & Tone Customization:**
   - Strict announcer voice always, or allow players to request "neutral" explanations?
   - Should responses adapt based on player's character perspective?

5. **Mobile Access:**
   - Priority on mobile-responsive web app vs native mobile app?
   - Offline access needs for sessions?

6. **Integration Preferences:**
   - Interest in Discord bot for quick queries?
   - VTT integration for real-time mechanics lookup during games?

---

## Appendix: Example User Flows

### Flow 1: New Player Onboarding

1. Player receives invitation link from GM
2. Creates account, sets password
3. GM assigns character (Imwe) to player's account
4. Player lands on character dashboard
   - Sees Imwe's current stats, fame level, injury status
   - Views session participation history (Sessions 1, 2, 3)
5. Player clicks "Ask the Chronicler" button
6. Types: "What happened in my last session?"
7. Receives dramatic summary of Session 3 with citations
8. Clicks citation to read full session notes

### Flow 2: Mechanics Exploration

1. Player preparing for next session
2. Opens app, navigates to chat
3. Asks: "How can I use Crowd's Favor to make the crowd love me?"
4. Receives explanation of Crowd's Favor mechanic
5. Sees examples from past sessions where it was used successfully
6. Gets suggestions: "Ask about Panache for even more crowd appeal"
7. Clicks "Panache" suggestion
8. Receives full Panache mechanics explanation
9. Bookmarks mechanics page for quick reference during game

### Flow 3: Strategic Planning

1. Player wants to earn patron interest
2. Asks: "Which patrons have sponsored gladiators in the past?"
3. Receives list of NPCs from revealed sessions who acted as patrons
4. Asks follow-up: "What impressed Patron Aurelius?"
5. Gets summary of what Aurelius valued in Session 2
6. Player notes to focus on dramatic finishers next session

---

## Conclusion

This architecture provides a scalable, secure, and theatrical web companion for The Arena campaign. By leveraging modern RAG technology with careful content access controls, players can explore the rich campaign history while preserving narrative surprises. The React-based frontend delivers an immersive experience that matches the dramatic tone of the campaign, while the robust backend ensures performance and reliability.

The phased implementation approach allows for rapid MVP delivery and iterative enhancement based on player feedback, keeping development focused and costs manageable.

**Next Steps:**
1. Review this design document with stakeholders
2. Address open questions on access models and feature priorities
3. Set up initial infrastructure (repos, hosting accounts, API keys)
4. Begin Phase 1 development

---

**Document Version:** 1.0  
**Last Updated:** 2025-11-23  
**Author:** GitHub Copilot (with @bestdan)
