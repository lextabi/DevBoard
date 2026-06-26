# Deployment Guide

This guide covers deploying DevBoard to production.

## Architecture

```
GitHub Repository
    ↓
GitHub Actions (CI/CD)
    ├→ Frontend → Vercel
    ├→ Backend → Render
    └→ Database → Supabase
```

## Deployment Services

- **Frontend**: [Vercel](https://vercel.com/) - Next-gen frontend platform
- **Backend**: [Render](https://render.com/) - Cloud application platform
- **Database**: [Supabase](https://supabase.com/) - Open source Firebase alternative

## Prerequisites

1. GitHub account and repository
2. Vercel account (free tier available)
3. Render account (free tier available)
4. Supabase account (free tier available)
5. Custom domain (optional)

## Step 1: Database Setup (Supabase)

### Create Supabase Project

1. Go to [supabase.com](https://supabase.com)
2. Sign in or create account
3. Click "New Project"
4. Fill in project details:
   - Name: `devboard`
   - Password: Choose strong password
   - Region: Select closest to you
5. Click "Create new project"

### Get Connection Details

1. Go to Settings → Database
2. Copy connection string
3. Add to GitHub Secrets as `DATABASE_URL`

### Run Migrations

```bash
# Install Alembic
pip install alembic

# Create migration
alembic revision -m "initial schema"

# Apply to production
alembic upgrade head --sql-mode
```

## Step 2: Backend Deployment (Render)

### Create Render Service

1. Go to [render.com](https://render.com)
2. Sign in with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Fill in settings:
   - Name: `devboard-api`
   - Environment: `Python 3`
   - Build Command: `pip install -r backend/requirements.txt`
   - Start Command: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port 10000`
6. Add environment variables:
   - `DATABASE_URL`: From Supabase
   - `SUPABASE_URL`: From Supabase
   - `SUPABASE_KEY`: From Supabase
   - `SECRET_KEY`: Generate strong key
   - `PYTHON_VERSION`: 3.12.1

### Configure Auto-Deployment

1. Go to Settings
2. Enable "Auto-deploy" from main branch
3. Save settings

## Step 3: Frontend Deployment (Vercel)

### Create Vercel Project

1. Go to [vercel.com](https://vercel.com)
2. Sign in with GitHub
3. Click "Add New..." → "Project"
4. Select your DevBoard repository
5. Configure project:
   - Framework Preset: `Vite`
   - Root Directory: `./frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`

### Add Environment Variables

1. Go to Settings → Environment Variables
2. Add:
   - `VITE_API_URL`: Your backend URL (from Render)
   - `VITE_SUPABASE_URL`: From Supabase
   - `VITE_SUPABASE_ANON_KEY`: From Supabase

### Deploy

Click "Deploy" to start deployment.

## Step 4: GitHub Secrets

Add these secrets for CI/CD:

### For Frontend Deployment

Go to Settings → Secrets and Variables → Actions

```
VERCEL_TOKEN=<token>
VERCEL_ORG_ID=<id>
VERCEL_PROJECT_ID=<id>
```

Get from Vercel Settings → Tokens

### For Backend Deployment

```
RENDER_SERVICE_ID=<id>
RENDER_API_KEY=<key>
```

Get from Render Settings

## Step 5: Custom Domain (Optional)

### Add Domain to Vercel

1. Go to Vercel Project Settings
2. Domains → Add Domain
3. Update DNS records at your registrar
4. Wait for verification

### Add Domain to Render

1. Go to Render Service Settings
2. Custom Domains → Add Domain
3. Update DNS records
4. Wait for verification

## Step 6: DNS Configuration

For custom domain (e.g., devboard.com):

```
# For Vercel (frontend)
CNAME   www    cname.vercel-dns.com
A             76.76.19.0

# For Render (backend)
CNAME   api    [render-url]
```

## Step 7: Environment Configuration

### Production Environment Variables

**Backend (.env)**:
```
DATABASE_URL=postgresql://user:pass@db.supabase.co:5432/postgres
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_KEY=xxxx
SECRET_KEY=<generate-strong-key>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**Frontend (.env.production)**:
```
VITE_API_URL=https://api.devboard.com/api/v1
VITE_SUPABASE_URL=https://xxxx.supabase.co
VITE_SUPABASE_ANON_KEY=xxxx
```

## Step 8: SSL/HTTPS

Both Vercel and Render provide free SSL certificates automatically.

Verify in browser:
- Frontend: https://your-domain.com (lock icon)
- Backend: https://api.your-domain.com/docs (lock icon)

## Monitoring & Logs

### Vercel Logs

1. Go to Project → Deployments
2. Click on deployment
3. View Logs tab

### Render Logs

1. Go to Service
2. View logs in dashboard
3. Monitor for errors

### Database Logs

1. Go to Supabase project
2. SQL Editor → View query logs
3. Monitor performance

## Database Backups

### Supabase Backups

1. Go to Settings → Backups
2. View automatic daily backups
3. Download backups if needed

### Manual Backup

```bash
# Export database
pg_dump -h db.supabase.co -U postgres -d postgres > backup.sql

# Import backup
psql -h db.supabase.co -U postgres -d postgres < backup.sql
```

## CI/CD Pipeline

Automatic deployments trigger on:

1. **Push to main branch**
   - Runs tests
   - Builds application
   - Deploys to production

2. **Pull requests**
   - Runs tests
   - Checks linting
   - Reports results

## Health Checks

### Frontend Health

Visit: https://your-domain.com
- Should load homepage
- Check console for errors

### Backend Health

Visit: https://api.your-domain.com/health
- Should return: `{"status": "ok"}`
- Check https://api.your-domain.com/docs for API docs

### Database Health

From backend server:
```bash
# Test connection
psql -h db.supabase.co -U postgres -d postgres -c "SELECT version();"
```

## Troubleshooting

### Build Failures

Check logs:
```bash
# Vercel
vercel logs

# Render
# Check Render dashboard logs
```

### Environment Variable Issues

Ensure all variables are set:
- Frontend: VITE_ prefix required
- Backend: DATABASE_URL format is correct

### Database Connection Errors

Test connection:
```bash
psql -c "SELECT version();"
```

### CORS Errors

Check CORS config in `backend/app/main.py`:
```python
allow_origins=["https://your-domain.com"]
```

## Production Checklist

Before going live:

- [ ] Database migrations tested
- [ ] Environment variables configured
- [ ] CORS properly configured
- [ ] HTTPS enabled
- [ ] Domain DNS configured
- [ ] Backups enabled
- [ ] Monitoring configured
- [ ] Error tracking enabled
- [ ] CDN/caching configured
- [ ] Rate limiting set up
- [ ] Security headers added
- [ ] CSRF protection enabled

## Rollback Procedure

If something goes wrong:

**Frontend (Vercel)**:
1. Go to Deployments
2. Find previous working deployment
3. Click "Promote to Production"

**Backend (Render)**:
1. Go to Deploys
2. Find previous working deploy
3. Click "Deploy"

## Further Reading

- [Vercel Deployment Guide](https://vercel.com/docs)
- [Render Deployment Guide](https://render.com/docs)
- [Supabase Guide](https://supabase.com/docs)
- [DevBoard Architecture](../ARCHITECTURE.md)

