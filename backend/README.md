# Backend - DevBoard

FastAPI backend for DevBoard.

## Quick Start

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

## Folder Structure

See [FOLDER_STRUCTURE.md](../FOLDER_STRUCTURE.md#backend-structure) in root directory.

## Environment Variables

Copy `.env.example` to `.env` and update values:

```
DATABASE_URL=postgresql://user:password@localhost:5432/devboard
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SECRET_KEY=your-secret-key-change-in-production
```

## Dependencies

- FastAPI
- SQLAlchemy
- Pydantic
- Alembic
- PostgreSQL driver (psycopg2)

See `requirements.txt` for full dependencies.

## Available APIs

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /docs` - Swagger UI (interactive API docs)
- `GET /redoc` - ReDoc (alternative API docs)

## Database Migrations

```bash
# Create a new migration
alembic revision -m "description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```
