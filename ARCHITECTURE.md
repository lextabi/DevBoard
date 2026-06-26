# DevBoard Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      User Browser                           │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTPS
          ┌──────────────┴──────────────┐
          │                             │
    ┌─────▼─────┐              ┌──────▼──────┐
    │   Vercel  │              │  Supabase   │
    │  Frontend │              │    Auth     │
    │  (React)  │              │  & Storage  │
    └─────┬─────┘              └──────┬──────┘
          │                           │
          └──────────────┬────────────┘
                         │ REST API
          ┌──────────────▼──────────────┐
          │      Render Backend         │
          │    (FastAPI + Python)       │
          └──────────────┬──────────────┘
                         │ SQL
          ┌──────────────▼──────────────┐
          │   Supabase PostgreSQL       │
          │      (Database)             │
          └─────────────────────────────┘
```

---

## Frontend Architecture

### Technology Stack
- **Framework:** React 18+ with TypeScript
- **Build Tool:** Vite
- **Styling:** Tailwind CSS + shadcn/ui
- **Routing:** React Router v6
- **State Management:** React Context API + Custom Hooks
- **HTTP Client:** Axios
- **Drag & Drop:** @dnd-kit
- **Charts:** Recharts
- **Authentication:** Supabase Auth

### Directory Structure
```
frontend/
├── public/
│   ├── favicon.ico
│   └── index.html
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── common/         # Button, Input, Modal, etc.
│   │   ├── kanban/         # Kanban board components
│   │   ├── dashboard/      # Dashboard components
│   │   └── projects/       # Project list components
│   ├── pages/              # Page components (route level)
│   │   ├── Auth/
│   │   ├── Dashboard/
│   │   ├── Projects/
│   │   └── NotFound/
│   ├── layouts/            # Layout wrappers
│   │   ├── MainLayout
│   │   └── AuthLayout
│   ├── hooks/              # Custom React hooks
│   │   ├── useAuth
│   │   ├── useProject
│   │   └── useTask
│   ├── services/           # API client logic
│   │   ├── api.ts         # Axios instance
│   │   ├── authService.ts
│   │   ├── projectService.ts
│   │   └── taskService.ts
│   ├── types/              # TypeScript type definitions
│   │   ├── api.ts
│   │   ├── models.ts
│   │   └── errors.ts
│   ├── context/            # React Context
│   │   ├── AuthContext
│   │   └── AppContext
│   ├── utils/              # Helper functions
│   │   ├── formatting.ts
│   │   ├── validation.ts
│   │   └── date.ts
│   ├── styles/             # Global styles
│   │   └── globals.css
│   ├── App.tsx
│   └── main.tsx
├── .env.example
├── .env.local (gitignored)
├── vite.config.ts
├── tsconfig.json
├── tailwind.config.js
├── postcss.config.js
├── package.json
├── package-lock.json
└── .gitignore
```

### Key Components

#### AuthContext
- User authentication state
- Token management
- Login/logout/signup actions
- Protected route wrapper

#### AppContext
- Global application state
- Current project context
- UI state (modals, notifications)

#### Custom Hooks
- `useAuth()` - Authentication state and actions
- `useProject()` - Current project state
- `useTask()` - Task management
- `useApi()` - API call wrapper with loading/error states

### Data Flow

1. User logs in via Supabase Auth
2. Frontend stores auth token in secure storage
3. Token included in all API requests
4. Backend validates token
5. API returns data
6. React state updated
7. UI re-renders

---

## Backend Architecture

### Technology Stack
- **Framework:** FastAPI (Python 3.12+)
- **ORM:** SQLAlchemy
- **Database:** PostgreSQL (Supabase)
- **Migrations:** Alembic
- **Authentication:** Supabase Auth (JWT tokens)
- **Testing:** pytest
- **HTTP Client:** httpx
- **Data Validation:** Pydantic

### Directory Structure
```
backend/
├── app/
│   ├── api/                # API routes
│   │   ├── v1/
│   │   │   ├── auth.py
│   │   │   ├── projects.py
│   │   │   ├── tasks.py
│   │   │   ├── boards.py
│   │   │   └── activity.py
│   │   └── __init__.py
│   ├── models/             # SQLAlchemy models
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── board.py
│   │   ├── column.py
│   │   ├── task.py
│   │   ├── label.py
│   │   ├── task_label.py
│   │   ├── activity.py
│   │   └── __init__.py
│   ├── schemas/            # Pydantic schemas (requests/responses)
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── task.py
│   │   ├── activity.py
│   │   └── __init__.py
│   ├── services/           # Business logic
│   │   ├── auth_service.py
│   │   ├── project_service.py
│   │   ├── task_service.py
│   │   ├── activity_service.py
│   │   └── __init__.py
│   ├── repositories/       # Data access layer
│   │   ├── user_repo.py
│   │   ├── project_repo.py
│   │   ├── task_repo.py
│   │   ├── activity_repo.py
│   │   └── __init__.py
│   ├── core/               # Core configuration
│   │   ├── config.py      # Environment variables
│   │   ├── security.py    # Auth helpers
│   │   ├── dependencies.py # FastAPI dependencies
│   │   └── exceptions.py  # Custom exceptions
│   ├── middleware/         # CORS, logging, etc.
│   │   └── __init__.py
│   ├── utils/              # Helper functions
│   │   ├── date_utils.py
│   │   ├── validation.py
│   │   └── __init__.py
│   ├── main.py            # FastAPI app initialization
│   └── __init__.py
├── migrations/            # Alembic migrations
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│   └── alembic.ini
├── tests/
│   ├── conftest.py       # pytest fixtures
│   ├── test_api/
│   │   ├── test_auth.py
│   │   ├── test_projects.py
│   │   └── test_tasks.py
│   ├── test_services/
│   │   ├── test_auth_service.py
│   │   └── test_project_service.py
│   └── test_integration/
│       └── test_api_integration.py
├── .env.example
├── .env (gitignored)
├── requirements.txt
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
└── README.md
```

### Clean Architecture Layers

#### 1. API Layer (FastAPI Routes)
- HTTP request/response handling
- Input validation (Pydantic)
- Authentication/authorization
- Returns consistent JSON responses

#### 2. Service Layer
- Business logic
- Validation rules
- Service-to-service communication
- Transaction management

#### 3. Repository Layer
- Data access abstraction
- Database queries
- Query optimization
- Returns model instances

#### 4. Models Layer
- SQLAlchemy ORM models
- Table definitions
- Relationships
- Database constraints

#### 5. Core Layer
- Configuration
- Security utilities
- Custom exceptions
- Dependency injection

### API Design

#### Base URL
```
https://api.devboard.app/api/v1
```

#### Authentication
- All endpoints except `/auth/*` require JWT token
- Token passed in `Authorization: Bearer <token>` header
- Token validated via Supabase

#### Response Format
```json
{
  "success": true,
  "data": { ... },
  "message": "Optional message"
}
```

#### Error Response Format
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message"
  }
}
```

---

## Database Architecture

### Database: PostgreSQL (Supabase)

#### Core Tables
1. **users** - User accounts and profiles
2. **projects** - User projects
3. **boards** - Kanban boards (one per project)
4. **columns** - Board columns
5. **tasks** - Individual tasks
6. **labels** - Task labels
7. **task_labels** - M2M relationship
8. **activity_logs** - Event tracking
9. **github_connections** - GitHub OAuth data (Phase 2)

#### Key Design Principles
- Normalized schema (3NF)
- Proper foreign key relationships
- Timestamps on all entities (created_at, updated_at)
- Soft deletes where applicable
- Indexes on frequently queried columns
- User data isolation (RLS policies in Supabase)

#### Migrations
- Version-controlled with Alembic
- Each change is a separate migration file
- Can rollback to any previous state
- Tested before production deployment

---

## Deployment Architecture

### Environment Strategy

#### Development
- Local Docker Compose
- Local PostgreSQL
- Hot reload enabled
- Debug logging enabled

#### Staging
- Same infrastructure as production
- Separate database
- Pre-deployment verification

#### Production
- Frontend: Vercel CDN + Serverless Functions
- Backend: Render Web Services
- Database: Supabase Managed PostgreSQL
- Domain: Custom domain with HTTPS

### CI/CD Pipeline (GitHub Actions)

```
Push to GitHub
    ↓
Run Tests (Backend)
    ↓
Run Linting & Type Checking
    ↓
Build Frontend
    ↓
Deploy Frontend to Vercel (if main)
    ↓
Deploy Backend to Render (if main)
```

---

## Security Architecture

### Authentication Flow
1. User signs up with email/password via Supabase
2. Supabase issues JWT token
3. Frontend stores token securely
4. Token sent with each API request
5. Backend validates token signature
6. Backend checks token expiration
7. Token includes user ID claim

### Authorization
- User can only access their own projects
- User can only modify/delete their own tasks
- Backend verifies ownership on every request

### Data Protection
- HTTPS everywhere
- Passwords hashed by Supabase (bcrypt)
- API tokens short-lived
- Refresh token rotation
- SQL injection prevention (SQLAlchemy parameterization)
- CORS properly configured

### Environment Secrets
- Database credentials
- API keys (never in code)
- Supabase keys
- JWT secret (via Supabase)
- Stored in environment variables
- Different values per environment

---

## Performance Considerations

### Frontend
- Code splitting with React Router
- Lazy loading components
- Image optimization
- Caching strategies
- Minification via Vite

### Backend
- Database query optimization
- Connection pooling
- Caching layer (future)
- Pagination for large datasets
- Async operations where possible

### Database
- Indexes on foreign keys
- Indexes on frequently filtered columns
- Query optimization
- Connection limits

---

## Monitoring & Logging

### Frontend
- Client-side error tracking (Sentry - future)
- Performance monitoring
- User session tracking

### Backend
- Structured logging (JSON format)
- Request/response logging
- Error logging with stack traces
- Performance metrics

### Database
- Query performance monitoring
- Connection monitoring
- Backup verification

---

## Technology Rationale

### Why These Choices?

| Component | Choice | Reason |
|-----------|--------|--------|
| Frontend | React + Vite | Modern, fast, large ecosystem |
| Backend | FastAPI | High performance, auto docs, type hints |
| Database | PostgreSQL | Robust, relational, Supabase managed |
| Auth | Supabase | Managed, secure, easy integration |
| Deployment | Vercel/Render | Serverless, auto-scaling, free tier |
| ORM | SQLAlchemy | Powerful, type-safe, migrations |

