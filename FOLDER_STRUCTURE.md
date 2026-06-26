# DevBoard Folder Structure

This document outlines the complete folder structure for the DevBoard project.

---

## Root Structure

```
DevBoard/
├── .git/                          # Git repository (auto-generated)
├── .gitignore
├── .env.example                   # Example environment variables
├── LICENSE                        # MIT License
├── README.md                      # Main project documentation
├── ROADMAP.md                     # Development roadmap
├── ARCHITECTURE.md                # System architecture
├── DATABASE_SCHEMA.md             # Database design
├── FOLDER_STRUCTURE.md            # This file
├── MILESTONE_PLAN.md              # Phase-by-phase milestones
│
├── frontend/                      # React frontend application
├── backend/                       # FastAPI backend application
├── docker-compose.yml             # Local development stack
│
├── .github/
│   ├── workflows/                 # GitHub Actions CI/CD
│   │   ├── backend-test.yml
│   │   ├── frontend-test.yml
│   │   ├── deploy.yml
│   │   └── lint.yml
│   ├── CODEOWNERS
│   ├── pull_request_template.md
│   └── issue_template/
│       ├── bug_report.md
│       └── feature_request.md
│
├── docs/                          # Additional documentation
│   ├── API.md                     # API endpoint documentation
│   ├── DEPLOYMENT.md              # Deployment guide
│   ├── DEVELOPMENT.md             # Development guide
│   ├── CONTRIBUTING.md            # Contributing guidelines
│   ├── SECURITY.md                # Security policy
│   ├── setup/
│   │   ├── frontend-setup.md
│   │   ├── backend-setup.md
│   │   └── database-setup.md
│   └── images/                    # Screenshots, diagrams
│       ├── architecture.png
│       └── database-erd.png
│
└── scripts/                       # Utility scripts
    ├── setup-dev.sh               # Setup development environment
    ├── start-dev.sh               # Start development stack
    └── reset-db.sh                # Reset development database
```

---

## Frontend Structure

```
frontend/
├── public/
│   ├── favicon.ico
│   ├── manifest.json
│   └── index.html
│
├── src/
│   ├── main.tsx                   # Entry point
│   ├── App.tsx                    # Root component
│   ├── index.css                  # Global styles
│   │
│   ├── components/                # Reusable components
│   │   ├── common/
│   │   │   ├── Button.tsx
│   │   │   ├── Input.tsx
│   │   │   ├── Modal.tsx
│   │   │   ├── Card.tsx
│   │   │   ├── Spinner.tsx
│   │   │   ├── Toast.tsx
│   │   │   ├── Sidebar.tsx
│   │   │   ├── Navbar.tsx
│   │   │   └── index.ts
│   │   │
│   │   ├── kanban/
│   │   │   ├── KanbanBoard.tsx
│   │   │   ├── KanbanColumn.tsx
│   │   │   ├── KanbanCard.tsx
│   │   │   ├── TaskModal.tsx
│   │   │   └── index.ts
│   │   │
│   │   ├── dashboard/
│   │   │   ├── DashboardMetrics.tsx
│   │   │   ├── ActivityFeed.tsx
│   │   │   ├── ProjectStats.tsx
│   │   │   └── index.ts
│   │   │
│   │   ├── projects/
│   │   │   ├── ProjectList.tsx
│   │   │   ├── ProjectCard.tsx
│   │   │   ├── ProjectForm.tsx
│   │   │   └── index.ts
│   │   │
│   │   ├── auth/
│   │   │   ├── LoginForm.tsx
│   │   │   ├── SignupForm.tsx
│   │   │   └── index.ts
│   │   │
│   │   └── index.ts               # Export all components
│   │
│   ├── pages/                     # Page-level components
│   │   ├── AuthPage.tsx
│   │   ├── DashboardPage.tsx
│   │   ├── ProjectsPage.tsx
│   │   ├── BoardPage.tsx
│   │   ├── SettingsPage.tsx
│   │   ├── NotFoundPage.tsx
│   │   └── index.ts
│   │
│   ├── layouts/                   # Layout components
│   │   ├── MainLayout.tsx
│   │   ├── AuthLayout.tsx
│   │   └── index.ts
│   │
│   ├── hooks/                     # Custom React hooks
│   │   ├── useAuth.ts
│   │   ├── useProject.ts
│   │   ├── useTask.ts
│   │   ├── useApi.ts
│   │   ├── useDarkMode.ts
│   │   └── index.ts
│   │
│   ├── context/                   # React Context
│   │   ├── AuthContext.tsx
│   │   ├── AppContext.tsx
│   │   └── index.ts
│   │
│   ├── services/                  # API clients
│   │   ├── api.ts                 # Axios instance
│   │   ├── authService.ts
│   │   ├── projectService.ts
│   │   ├── taskService.ts
│   │   ├── activityService.ts
│   │   └── index.ts
│   │
│   ├── types/                     # TypeScript types
│   │   ├── api.ts
│   │   ├── models.ts
│   │   ├── errors.ts
│   │   ├── forms.ts
│   │   └── index.ts
│   │
│   ├── utils/                     # Utility functions
│   │   ├── formatting.ts
│   │   ├── validation.ts
│   │   ├── date.ts
│   │   ├── localStorage.ts
│   │   └── index.ts
│   │
│   ├── styles/
│   │   └── globals.css
│   │
│   └── constants/
│       ├── api.ts
│       ├── messages.ts
│       └── config.ts
│
├── tests/
│   ├── setup.ts
│   ├── components/
│   │   ├── Button.test.tsx
│   │   └── LoginForm.test.tsx
│   ├── hooks/
│   │   ├── useAuth.test.ts
│   │   └── useApi.test.ts
│   └── utils/
│       └── formatting.test.ts
│
├── .env.example                   # Example environment variables
├── .env.local (gitignored)        # Local environment variables
├── .eslintrc.json                 # ESLint configuration
├── .prettierrc                    # Prettier configuration
├── tsconfig.json                  # TypeScript configuration
├── vite.config.ts                 # Vite configuration
├── vitest.config.ts               # Vitest configuration
├── tailwind.config.js             # Tailwind CSS configuration
├── postcss.config.js              # PostCSS configuration
├── package.json
├── package-lock.json
├── README.md
└── .gitignore
```

---

## Backend Structure

```
backend/
├── app/
│   ├── main.py                    # FastAPI application entry
│   ├── __init__.py
│   │
│   ├── api/                       # API routes/endpoints
│   │   ├── v1/
│   │   │   ├── auth.py           # Authentication endpoints
│   │   │   ├── projects.py       # Project endpoints
│   │   │   ├── tasks.py          # Task endpoints
│   │   │   ├── boards.py         # Board endpoints
│   │   │   ├── activity.py       # Activity endpoints
│   │   │   ├── labels.py         # Label endpoints
│   │   │   └── __init__.py
│   │   └── __init__.py
│   │
│   ├── models/                    # SQLAlchemy ORM models
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── board.py
│   │   ├── column.py
│   │   ├── task.py
│   │   ├── label.py
│   │   ├── task_label.py
│   │   ├── activity.py
│   │   ├── github_connection.py   # Phase 2
│   │   ├── base.py                # Base model class
│   │   └── __init__.py
│   │
│   ├── schemas/                   # Pydantic request/response schemas
│   │   ├── user.py
│   │   ├── project.py
│   │   ├── task.py
│   │   ├── board.py
│   │   ├── activity.py
│   │   ├── label.py
│   │   └── __init__.py
│   │
│   ├── services/                  # Business logic layer
│   │   ├── auth_service.py
│   │   ├── project_service.py
│   │   ├── task_service.py
│   │   ├── board_service.py
│   │   ├── activity_service.py
│   │   ├── label_service.py
│   │   └── __init__.py
│   │
│   ├── repositories/              # Data access layer
│   │   ├── base_repo.py          # Base repository class
│   │   ├── user_repo.py
│   │   ├── project_repo.py
│   │   ├── task_repo.py
│   │   ├── board_repo.py
│   │   ├── activity_repo.py
│   │   ├── label_repo.py
│   │   └── __init__.py
│   │
│   ├── core/                      # Core configuration
│   │   ├── config.py             # Environment variables
│   │   ├── security.py           # Auth utilities
│   │   ├── dependencies.py       # FastAPI dependencies
│   │   ├── exceptions.py         # Custom exceptions
│   │   └── __init__.py
│   │
│   ├── middleware/                # ASGI middleware
│   │   ├── logging.py
│   │   ├── cors.py
│   │   └── __init__.py
│   │
│   ├── utils/                     # Utility functions
│   │   ├── date_utils.py
│   │   ├── validation.py
│   │   ├── formatting.py
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── migrations/                    # Alembic database migrations
│   ├── versions/
│   │   ├── 2024_01_01_001_create_users_table.py
│   │   ├── 2024_01_01_002_create_projects_table.py
│   │   └── ...
│   ├── env.py
│   ├── script.py.mako
│   ├── alembic.ini
│   └── README
│
├── tests/
│   ├── conftest.py               # pytest fixtures
│   │
│   ├── test_api/
│   │   ├── test_auth.py
│   │   ├── test_projects.py
│   │   ├── test_tasks.py
│   │   ├── test_boards.py
│   │   └── __init__.py
│   │
│   ├── test_services/
│   │   ├── test_auth_service.py
│   │   ├── test_project_service.py
│   │   ├── test_task_service.py
│   │   └── __init__.py
│   │
│   ├── test_repositories/
│   │   ├── test_project_repo.py
│   │   └── __init__.py
│   │
│   ├── test_integration/
│   │   ├── test_api_integration.py
│   │   └── __init__.py
│   │
│   └── __init__.py
│
├── .env.example
├── .env (gitignored)
├── .dockerignore
├── .gitignore
├── .eslintignore
├── Dockerfile
├── requirements.txt
├── pyproject.toml
├── setup.py
├── pytest.ini
├── README.md
└── docker-entrypoint.sh
```

---

## Database Structure

```
database/
├── scripts/
│   ├── init-db.sql               # Initial schema (if not using Alembic)
│   ├── seed-data.sql             # Development data
│   └── reset-db.sh               # Reset development database
│
└── backups/                       # Database backups (gitignored)
    └── .gitkeep
```

---

## GitHub Workflows

```
.github/
└── workflows/
    ├── lint-and-test.yml         # Lint, format, test on every push
    ├── backend-deploy.yml        # Deploy backend on push to main
    ├── frontend-deploy.yml       # Deploy frontend on push to main
    └── security-scan.yml         # Security scanning (future)
```

---

## Documentation Folder

```
docs/
├── README.md                      # Docs index
├── API.md                         # API documentation
├── DEPLOYMENT.md                  # Deployment guide
├── DEVELOPMENT.md                 # Development setup guide
├── CONTRIBUTING.md                # Contributing guidelines
├── SECURITY.md                    # Security policy
│
├── guides/
│   ├── frontend-setup.md
│   ├── backend-setup.md
│   ├── database-setup.md
│   ├── docker-guide.md
│   └── github-integration.md (Phase 2)
│
├── architecture/
│   ├── overview.md
│   ├── frontend-architecture.md
│   ├── backend-architecture.md
│   └── data-flow.md
│
├── images/
│   ├── architecture-diagram.png
│   ├── database-erd.png
│   ├── api-endpoints.png
│   └── screenshots/
│       ├── dashboard.png
│       ├── kanban-board.png
│       └── projects-list.png
│
├── api/
│   ├── auth.md
│   ├── projects.md
│   ├── tasks.md
│   ├── boards.md
│   ├── labels.md
│   └── activity.md
│
└── troubleshooting/
    ├── common-issues.md
    ├── docker-issues.md
    └── database-issues.md
```

---

## Key Design Decisions

### 1. Separation of Concerns
- **Frontend** and **Backend** are completely separate
- Can be developed independently
- Different deployment targets

### 2. Layered Architecture (Backend)
- **API Layer**: HTTP handling
- **Service Layer**: Business logic
- **Repository Layer**: Data access
- **Models Layer**: Database entities

### 3. Component Organization (Frontend)
- **components/**: Reusable UI components
- **pages/**: Route-level components
- **services/**: API communication
- **hooks/**: Stateful logic
- **context/**: Global state

### 4. Testing Structure
- Tests colocated with source code logic
- Test file naming: `*.test.ts` or `*.test.tsx`
- Shared fixtures in `conftest.py` / `setup.ts`

### 5. Configuration Management
- `.env.example` committed to repo
- `.env` files gitignored
- Environment variables validated at startup
- Different configs per environment

### 6. Documentation
- Main docs in root (README, ARCHITECTURE, etc.)
- Detailed guides in `docs/`
- API docs auto-generated from code

### 7. Version Control
- All code in Git
- GitHub Actions for CI/CD
- Branch protection on main
- Conventional commits

---

## Important Files to Create

**Priority 1 (Before any code):**
- ✅ README.md
- ✅ ROADMAP.md
- ✅ ARCHITECTURE.md
- ✅ DATABASE_SCHEMA.md
- ✅ FOLDER_STRUCTURE.md (this file)
- ✅ MILESTONE_PLAN.md

**Priority 2 (Project setup):**
- LICENSE
- .gitignore
- .env.example
- GitHub Actions workflows

**Priority 3 (Development):**
- Docker setup files
- Configuration files (tsconfig, vite, pytest.ini)

**Priority 4 (Implementation):**
- Source code files as per folder structure

