# Development Guide

This guide covers setting up your development environment for DevBoard.

## Prerequisites

- Node.js 18+ (for frontend)
- Python 3.12+ (for backend)
- PostgreSQL 13+ (or Docker)
- Git
- A code editor (VS Code recommended)

## Quick Start with Docker (Recommended)

The easiest way to start development is using Docker Compose:

```bash
# Clone the repository
git clone https://github.com/lextabi/DevBoard.git
cd DevBoard

# Start development stack
docker-compose up

# In a new terminal, install dependencies (if needed)
docker-compose exec backend pip install -r requirements.txt
docker-compose exec frontend npm install
```

Then access:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Database: localhost:5432

## Manual Setup

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create environment file
cp .env.example .env.local

# Update .env.local with your values
VITE_API_URL=http://localhost:8000/api/v1
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_ANON_KEY=your_supabase_key

# Start development server
npm run dev
```

Frontend runs on: http://localhost:5173

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Update .env with your values
DATABASE_URL=postgresql://user:password@localhost:5432/devboard
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key

# Run migrations
alembic upgrade head

# Start development server
python -m uvicorn app.main:app --reload
```

Backend runs on: http://localhost:8000

### Database Setup

PostgreSQL needs to be running. Either:

1. **Use Docker** (recommended):
   ```bash
   docker run -d \
     --name devboard-postgres \
     -e POSTGRES_USER=devboard \
     -e POSTGRES_PASSWORD=password \
     -e POSTGRES_DB=devboard \
     -p 5432:5432 \
     postgres:16-alpine
   ```

2. **Use local PostgreSQL** (if installed)

## Development Workflow

### 1. Create a feature branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make changes

Edit code in `frontend/src/` or `backend/app/`

### 3. Test your changes

**Frontend:**
```bash
cd frontend
npm run test          # Run tests
npm run test:coverage # Check coverage
npm run lint          # Check linting
```

**Backend:**
```bash
cd backend
pytest                # Run tests
pytest --cov=app     # Check coverage
flake8 .             # Check linting
```

### 4. Commit with conventional commits

```bash
git add .
git commit -m "feat: add new feature"
git commit -m "fix: resolve bug"
git commit -m "docs: update documentation"
git commit -m "test: add test cases"
git commit -m "chore: update dependencies"
```

### 5. Push and create PR

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Environment Variables

### Frontend (.env.local)

```
VITE_API_URL=http://localhost:8000/api/v1
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=your_anon_key
```

### Backend (.env)

```
DATABASE_URL=postgresql://devboard:password@localhost:5432/devboard
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_key
SECRET_KEY=dev-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Useful Commands

### Frontend

```bash
npm run dev           # Start dev server
npm run build         # Production build
npm run lint          # Lint code
npm run test          # Run tests
npm run test:ui       # Test UI
npm run test:coverage # Coverage report
npm run preview       # Preview build
```

### Backend

```bash
uvicorn app.main:app --reload        # Start dev server
pytest                               # Run tests
pytest -v                            # Verbose output
pytest --cov=app                     # Coverage
black app/                           # Format code
isort app/                           # Sort imports
flake8 app/                          # Lint code
alembic revision -m "description"    # Create migration
alembic upgrade head                 # Apply migrations
alembic downgrade -1                 # Rollback migration
```

### Docker

```bash
docker-compose up                    # Start all services
docker-compose up -d                 # Start in background
docker-compose down                  # Stop all services
docker-compose logs -f               # View logs
docker-compose logs -f backend       # Backend logs
docker-compose logs -f frontend      # Frontend logs
docker-compose exec backend bash     # Shell in backend
docker-compose exec frontend sh      # Shell in frontend
```

## Code Style

### Frontend

- Use TypeScript for type safety
- Use React hooks for state management
- Format with Prettier
- Lint with ESLint

```bash
cd frontend
npm run lint          # Run linter
npm run lint -- --fix # Auto-fix issues
```

### Backend

- Follow PEP 8
- Use type hints
- Format with Black
- Lint with flake8

```bash
cd backend
black app/            # Format code
isort app/            # Sort imports
flake8 app/           # Check style
```

## Testing

### Frontend Testing

```bash
cd frontend
npm run test          # Run all tests
npm run test:ui       # Interactive test UI
npm run test:coverage # Coverage report
```

### Backend Testing

```bash
cd backend
pytest                # Run all tests
pytest tests/test_api/ # Specific directory
pytest -v             # Verbose
pytest --cov=app      # Coverage
pytest -k test_name   # Specific test
```

## Database Migrations

```bash
# Create new migration
alembic revision -m "add users table"

# Edit migration file in backend/migrations/versions/

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1

# View current revision
alembic current
```

## Debugging

### Frontend Debugging

1. **Browser DevTools**: Press F12 in your browser
2. **React DevTools**: Install React DevTools extension
3. **Console**: Check browser console for errors
4. **VSCode Debugger**: Use VSCode's built-in debugger

### Backend Debugging

1. **VSCode Python Extension**: Install Python extension
2. **Set breakpoints**: Click on line number
3. **Debug with pytest**: `pytest --pdb` (interactive debugger)
4. **Print debugging**: Use `print()` or logging

## Common Issues

### Port Already in Use

```bash
# Find process using port 5173 (frontend)
lsof -i :5173
kill -9 <PID>

# Find process using port 8000 (backend)
lsof -i :8000
kill -9 <PID>
```

### Database Connection Error

Check `.env` has correct `DATABASE_URL`:
```
DATABASE_URL=postgresql://user:password@localhost:5432/devboard
```

### Module Not Found

**Frontend:**
```bash
cd frontend
npm install
rm -rf node_modules package-lock.json
npm install
```

**Backend:**
```bash
cd backend
pip install --upgrade pip
pip install -r requirements.txt
```

### Docker Issues

```bash
# Clean up Docker
docker-compose down -v
docker system prune
docker-compose up --build
```

## Need Help?

1. Check existing [issues](https://github.com/lextabi/DevBoard/issues)
2. Review [Architecture](../ARCHITECTURE.md)
3. Check [Database Schema](../DATABASE_SCHEMA.md)
4. Ask in GitHub Discussions

