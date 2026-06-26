# DevBoard

A production-quality personal developer workspace combining Kanban project management, GitHub integration, and productivity analytics.

**Status:** MVP in development  
**GitHub:** https://github.com/yourusername/DevBoard  
**Live Demo:** (coming soon)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Architecture](#architecture)
- [Database Schema](#database-schema)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Development Guide](#development-guide)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

DevBoard is a full-stack SaaS application designed for solo developers and small teams to:

- **Manage Projects**: Create, organize, and track software projects
- **Track Tasks**: Use Kanban boards with customizable columns
- **Monitor Progress**: Dashboard with metrics and activity tracking
- **Integrate GitHub**: View repositories, commits, and pull requests (Phase 2)
- **Analyze Productivity**: Track task completion and productivity trends (Phase 2)

This is a **portfolio project** demonstrating:
- Full-stack development capabilities
- Clean architecture and best practices
- Professional deployment strategies
- Production-ready code quality

### Target Users
- Solo developers managing multiple projects
- Small teams with lightweight project management needs
- Developers looking for a personal developer workspace

---

## Features

### MVP (Phase 1-5)

#### ✅ User Authentication
- Sign up with email/password
- Secure login/logout
- Protected routes
- User profile management
- Session persistence

#### ✅ Project Management
- Create/edit/delete projects
- Archive projects
- Project priorities and status
- User-specific project isolation

#### ✅ Kanban Board
- One board per project
- 6 default columns (Ideas → Completed)
- Create/edit/delete tasks
- Drag-and-drop task movement
- Reorder tasks within columns
- Task priorities and due dates
- Story points estimation
- Task labels/tags
- Task descriptions

#### ✅ Dashboard
- Key metrics (total projects, active tasks, etc.)
- Task statistics
- Activity feed
- Recent activity tracking

#### ✅ Activity Tracking
- Log all task and project events
- Activity feed display
- Audit trail

### Phase 2 (GitHub Integration)
- Connect GitHub account
- Display repositories
- Show recent commits
- Display pull requests and issues
- GitHub activity dashboard

### Phase 3 (AI-Assisted Features)
- OpenAI integration for project planning
- Claude integration for task suggestions
- GitHub Models integration

---

## Tech Stack

### Frontend
- **React 18+** with TypeScript
- **Vite** for fast builds
- **Tailwind CSS** for styling
- **shadcn/ui** for components
- **React Router v6** for navigation
- **Axios** for API calls
- **@dnd-kit** for drag-and-drop
- **Recharts** for visualizations

### Backend
- **FastAPI** (Python 3.12+)
- **SQLAlchemy** for ORM
- **Pydantic** for validation
- **Alembic** for migrations
- **pytest** for testing

### Database & Auth
- **PostgreSQL** (via Supabase)
- **Supabase Auth** for authentication

### Deployment
- **Vercel** - Frontend hosting
- **Render** - Backend hosting
- **Supabase** - Database hosting
- **GitHub Actions** - CI/CD

### Development
- **Docker** & **Docker Compose** - Local development
- **Git** - Version control
- **GitHub** - Repository hosting

---

## Project Structure

```
DevBoard/
├── frontend/                    # React SPA
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── types/
│   │   └── styles/
│   └── package.json
│
├── backend/                     # FastAPI REST API
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── repositories/
│   │   ├── core/
│   │   └── utils/
│   ├── migrations/
│   ├── tests/
│   └── requirements.txt
│
├── docker-compose.yml           # Local development stack
├── README.md                    # This file
├── ARCHITECTURE.md              # System architecture
├── DATABASE_SCHEMA.md           # Database design
├── ROADMAP.md                   # Development roadmap
├── FOLDER_STRUCTURE.md          # Detailed folder layout
├── MILESTONE_PLAN.md            # Phase-by-phase milestones
└── docs/                        # Additional documentation
```

See [FOLDER_STRUCTURE.md](FOLDER_STRUCTURE.md) for detailed breakdown.

---

## Getting Started

### Prerequisites
- Node.js 18+ (for frontend)
- Python 3.12+ (for backend)
- PostgreSQL (or Docker for local dev)
- Git
- Supabase account (free tier available)

### Quick Start with Docker

1. **Clone repository:**
   ```bash
   git clone https://github.com/yourusername/DevBoard.git
   cd DevBoard
   ```

2. **Set up environment:**
   ```bash
   cp .env.example .env.local
   # Edit .env.local with your Supabase credentials
   ```

3. **Start development stack:**
   ```bash
   docker-compose up
   ```

4. **Access application:**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Manual Setup

See individual setup guides:
- [Frontend Setup](docs/guides/frontend-setup.md)
- [Backend Setup](docs/guides/backend-setup.md)
- [Database Setup](docs/guides/database-setup.md)

---

## 🧪 Testing & Approval Workflow

This project follows a structured testing workflow for quality assurance:

1. **Development**: Features implemented per phase requirements
2. **Manual Testing**: You personally test all functionality
3. **Approval**: Once satisfied, request proceed to next phase
4. **Deployment**: Code deployed to production

Each phase includes:
- Unit/integration tests in CI/CD
- Manual testing checklist
- Approval gate before next phase
- Documentation for testing procedures

See [docs/TESTING.md](docs/TESTING.md) for detailed testing checklists and procedures.

---

## Architecture

DevBoard follows a **three-tier architecture**:

```
┌─────────────────────────────────┐
│   React Frontend (Vite)         │
│   - User Interface              │
│   - State Management            │
│   - API Communication           │
└────────────┬────────────────────┘
             │ HTTP(S)
             ▼
┌─────────────────────────────────┐
│   FastAPI Backend               │
│   - REST API                    │
│   - Business Logic              │
│   - Request Validation          │
└────────────┬────────────────────┘
             │ SQL
             ▼
┌─────────────────────────────────┐
│   PostgreSQL Database           │
│   - Data Persistence            │
│   - Relationships               │
│   - Constraints                 │
└─────────────────────────────────┘
```

### Key Design Principles

1. **Separation of Concerns**: Frontend and backend are independent
2. **Clean Architecture**: Layered architecture in backend (API → Service → Repository)
3. **Type Safety**: TypeScript (frontend) and Pydantic (backend)
4. **Data Integrity**: Foreign keys, constraints, migrations
5. **Security**: JWT auth, CORS, HTTPS, input validation
6. **Testing**: Unit, integration, and E2E tests
7. **Documentation**: Auto-generated API docs, guides, architecture docs

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed architecture documentation.

---

## Database Schema

DevBoard uses **PostgreSQL** with the following core entities:

- **Users** - User accounts and profiles
- **Projects** - User projects with metadata
- **Boards** - Kanban board per project
- **Columns** - Board columns (Ideas → Completed)
- **Tasks** - Individual cards/tasks
- **Labels** - Tags for tasks
- **ActivityLogs** - Event audit trail

All relationships are properly normalized with foreign keys, indexes, and constraints.

### ER Diagram

```
Users (1) ──→ (N) Projects
         ──→ (N) ActivityLogs
         ──→ (1) GitHubConnections

Projects (1) ──→ (1) Boards
         ──→ (N) Tasks
         ──→ (N) Labels
         ──→ (N) ActivityLogs

Boards (1) ──→ (N) Columns

Columns (1) ──→ (N) Tasks

Tasks (N) ──→ (N) Labels [via TaskLabels]
     (1) ──→ (1) Column

Labels (1) ──→ (N) Tasks [via TaskLabels]
```

See [DATABASE_SCHEMA.md](DATABASE_SCHEMA.md) for complete schema documentation.

---

## API Documentation

DevBoard provides a **REST API** with OpenAPI documentation.

### Base URL
```
https://api.devboard.app/api/v1
```

### Key Endpoints

#### Authentication
- `POST /auth/signup` - Register new user
- `POST /auth/login` - Login user
- `POST /auth/logout` - Logout user
- `GET /auth/me` - Get current user
- `POST /auth/refresh` - Refresh token

#### Projects
- `GET /projects` - List user projects
- `POST /projects` - Create project
- `GET /projects/{id}` - Get project details
- `PUT /projects/{id}` - Update project
- `DELETE /projects/{id}` - Delete project
- `PATCH /projects/{id}/archive` - Archive project

#### Tasks
- `POST /tasks` - Create task
- `PUT /tasks/{id}` - Update task
- `DELETE /tasks/{id}` - Delete task
- `PATCH /tasks/{id}/move` - Move task to column

#### Boards
- `GET /projects/{id}/board` - Get project board
- `PATCH /columns/{id}/reorder` - Reorder tasks in column

#### Labels
- `POST /projects/{id}/labels` - Create label
- `POST /tasks/{id}/labels/{label_id}` - Add label to task
- `DELETE /tasks/{id}/labels/{label_id}` - Remove label from task

#### Activity
- `GET /projects/{id}/activity` - Get project activity logs
- `GET /dashboard` - Get user dashboard metrics

**Full API documentation:** See [docs/API.md](docs/API.md)

**Interactive Docs:** Visit http://localhost:8000/docs (Swagger UI)

---

## Deployment

### Frontend Deployment (Vercel)

1. Push code to GitHub
2. Connect GitHub repo to Vercel
3. Vercel automatically builds and deploys on every push
4. Frontend available at custom domain

### Backend Deployment (Render)

1. Push code to GitHub
2. Connect GitHub repo to Render
3. Render automatically builds and deploys on every push
4. Backend API available at custom domain

### Database (Supabase)

1. Create Supabase project
2. PostgreSQL database automatically provisioned
3. Connection string in environment variables
4. Backups and monitoring included

See [DEPLOYMENT.md](docs/guides/deployment.md) for detailed deployment guide.

---

## Development Guide

### Prerequisites
- Node.js 18+
- Python 3.12+
- PostgreSQL (local or via Docker)
- Git

### Setup

```bash
# Clone repository
git clone https://github.com/yourusername/DevBoard.git
cd DevBoard

# Setup with Docker (recommended)
docker-compose up

# Or setup manually - see docs/guides/
```

### Development Workflow

```bash
# Start development server
npm run dev          # Frontend (http://localhost:5173)
python -m uvicorn app.main:app --reload  # Backend (http://localhost:8000)

# Run tests
npm run test         # Frontend
pytest               # Backend

# Lint and format
npm run lint         # Frontend
python -m black app/  # Backend

# Create database migration
alembic revision -m "description"
alembic upgrade head
```

### Commit Standards

Use conventional commits:
```
feat: add task drag-and-drop
fix: resolve database connection issue
docs: update API documentation
test: add tests for project service
chore: update dependencies
```

See [DEVELOPMENT.md](docs/guides/development.md) for complete development guide.

---

## Roadmap

### Phase 1 (MVP) - 4-6 weeks
- ✅ Authentication system
- ✅ Project management (CRUD)
- ✅ Kanban board with drag-and-drop
- ✅ Dashboard with metrics
- ✅ Activity tracking

### Phase 2 - GitHub Integration
- GitHub OAuth connection
- Repository display
- Commit history
- Pull requests and issues
- GitHub activity dashboard

### Phase 3 - AI-Assisted Features
- OpenAI integration for project planning
- Claude integration for task suggestions
- Automated task generation from issues

### Phase 4 - Advanced Features
- Team collaboration
- Time tracking
- Advanced filtering
- Custom board templates
- Notifications system

See [ROADMAP.md](ROADMAP.md) and [MILESTONE_PLAN.md](MILESTONE_PLAN.md) for detailed timelines.

---

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

---

## Project Stats

- **Lines of Code**: ~5,000+ (target for MVP)
- **Test Coverage**: >80% (frontend), >85% (backend)
- **Number of API Endpoints**: 20+
- **Database Tables**: 9
- **React Components**: 30+
- **Documentation Pages**: 8+

---

## Learning Outcomes

This project demonstrates:

✅ **Full-Stack Development**
- Modern React patterns (hooks, context, components)
- FastAPI and Python async programming
- PostgreSQL and SQL optimization

✅ **Software Engineering**
- Clean architecture and design patterns
- Test-driven development
- API design and documentation
- Database design and migrations

✅ **DevOps & Deployment**
- Docker containerization
- GitHub Actions CI/CD
- Cloud deployment (Vercel, Render, Supabase)
- Environment management

✅ **Best Practices**
- Git workflow and commit standards
- Code review readiness
- Security implementation
- Performance optimization

---

## Performance Targets

| Metric | Target |
|--------|--------|
| Dashboard Load | < 2s |
| Task Creation | < 500ms |
| Drag-and-Drop | 60 FPS |
| API Response | < 200ms |
| Test Coverage | > 80% |
| Lighthouse Score | > 90 |

---

## Security

- **Authentication**: Supabase Auth (JWT tokens)
- **HTTPS**: Enforced on all connections
- **CORS**: Properly configured
- **Input Validation**: Pydantic schemas
- **Database**: RLS policies, parameterized queries
- **Secrets**: Never committed, environment variables only

See [SECURITY.md](docs/SECURITY.md) for detailed security documentation.

---

## Troubleshooting

### Common Issues

1. **Docker issues** → See [Docker Troubleshooting](docs/troubleshooting/docker-issues.md)
2. **Database issues** → See [Database Troubleshooting](docs/troubleshooting/database-issues.md)
3. **API errors** → See [API Troubleshooting](docs/troubleshooting/common-issues.md)

---

## License

MIT License - see [LICENSE](LICENSE) file for details

---

## Contact & Links

- **GitHub**: https://github.com/yourusername/DevBoard
- **LinkedIn**: [Your LinkedIn Profile]
- **Email**: your.email@example.com
- **Portfolio**: [Your Portfolio Website]

---

## Acknowledgments

- Built with [React](https://react.dev) and [FastAPI](https://fastapi.tiangolo.com)
- UI components from [shadcn/ui](https://ui.shadcn.com)
- Styling with [Tailwind CSS](https://tailwindcss.com)
- Drag-and-drop with [@dnd-kit](https://docs.dnd-kit.com)
- Charts with [Recharts](https://recharts.org)

---

## Next Steps

1. Review the [ARCHITECTURE.md](ARCHITECTURE.md) for system design
2. Check [DATABASE_SCHEMA.md](DATABASE_SCHEMA.md) for data model
3. Read [MILESTONE_PLAN.md](MILESTONE_PLAN.md) for implementation phases
4. Start Phase 0 setup (see [MILESTONE_PLAN.md](MILESTONE_PLAN.md#phase-0-project-setup-week-1))

---

**Last Updated:** June 26, 2024  
**Status:** Planning Phase  
**Version:** 0.1.0 (Planning)

