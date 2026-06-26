# DevBoard Database Schema

## Entity Relationship Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                           │
│                          DATABASE SCHEMA                                 │
│                                                                           │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │ USERS                                                              │ │
│  ├────────────────────────────────────────────────────────────────────┤ │
│  │ id (UUID, PK)                                                      │ │
│  │ email (VARCHAR, UNIQUE)                                            │ │
│  │ full_name (VARCHAR, NULL)                                          │ │
│  │ avatar_url (VARCHAR, NULL)                                         │ │
│  │ created_at (TIMESTAMP)                                             │ │
│  │ updated_at (TIMESTAMP)                                             │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                              │                                            │
│                              │ 1:N                                        │
│                              ▼                                            │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │ PROJECTS                                                           │ │
│  ├────────────────────────────────────────────────────────────────────┤ │
│  │ id (UUID, PK)                                                      │ │
│  │ user_id (UUID, FK → users.id)                                      │ │
│  │ name (VARCHAR)                                                     │ │
│  │ description (TEXT, NULL)                                           │ │
│  │ status (ENUM: active, archived)                                    │ │
│  │ priority (ENUM: low, medium, high, critical)                       │ │
│  │ created_at (TIMESTAMP)                                             │ │
│  │ updated_at (TIMESTAMP)                                             │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                              │                                            │
│                              │ 1:1                                        │
│                              ▼                                            │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │ BOARDS                                                             │ │
│  ├────────────────────────────────────────────────────────────────────┤ │
│  │ id (UUID, PK)                                                      │ │
│  │ project_id (UUID, FK → projects.id)                                │ │
│  │ created_at (TIMESTAMP)                                             │ │
│  │ updated_at (TIMESTAMP)                                             │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                              │                                            │
│                              │ 1:N                                        │
│                              ▼                                            │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │ COLUMNS                                                            │ │
│  ├────────────────────────────────────────────────────────────────────┤ │
│  │ id (UUID, PK)                                                      │ │
│  │ board_id (UUID, FK → boards.id)                                    │ │
│  │ name (VARCHAR)                                                     │ │
│  │ order (INTEGER)                                                    │ │
│  │ created_at (TIMESTAMP)                                             │ │
│  │ updated_at (TIMESTAMP)                                             │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                              │                                            │
│                              │ 1:N                                        │
│                              ▼                                            │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │ TASKS                                                              │ │
│  ├────────────────────────────────────────────────────────────────────┤ │
│  │ id (UUID, PK)                                                      │ │
│  │ column_id (UUID, FK → columns.id)                                  │ │
│  │ project_id (UUID, FK → projects.id)                                │ │
│  │ title (VARCHAR)                                                    │ │
│  │ description (TEXT, NULL)                                           │ │
│  │ priority (ENUM: low, medium, high)                                 │ │
│  │ status (ENUM: todo, in_progress, done)                             │ │
│  │ due_date (DATE, NULL)                                              │ │
│  │ story_points (INTEGER, NULL)                                       │ │
│  │ order (INTEGER)                                                    │ │
│  │ created_at (TIMESTAMP)                                             │ │
│  │ updated_at (TIMESTAMP)                                             │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                  │                                                        │
│                  │ N:M (via TASK_LABELS)                                │
│                  ▼                                                        │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │ LABELS                                                             │ │
│  ├────────────────────────────────────────────────────────────────────┤ │
│  │ id (UUID, PK)                                                      │ │
│  │ project_id (UUID, FK → projects.id)                                │ │
│  │ name (VARCHAR)                                                     │ │
│  │ color (VARCHAR) [hex color code]                                   │ │
│  │ created_at (TIMESTAMP)                                             │ │
│  │ updated_at (TIMESTAMP)                                             │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                                                                           │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │ TASK_LABELS (Join Table)                                           │ │
│  ├────────────────────────────────────────────────────────────────────┤ │
│  │ task_id (UUID, FK → tasks.id, PK)                                  │ │
│  │ label_id (UUID, FK → labels.id, PK)                                │ │
│  │ created_at (TIMESTAMP)                                             │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                                                                           │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │ ACTIVITY_LOGS                                                      │ │
│  ├────────────────────────────────────────────────────────────────────┤ │
│  │ id (UUID, PK)                                                      │ │
│  │ user_id (UUID, FK → users.id)                                      │ │
│  │ project_id (UUID, FK → projects.id)                                │ │
│  │ task_id (UUID, FK → tasks.id, NULL)                                │ │
│  │ action (ENUM: task_created, task_updated, task_moved, task_completed│ │
│  │          project_created, project_updated, project_archived)       │ │
│  │ description (TEXT)                                                 │ │
│  │ metadata (JSONB, NULL) [stores additional context]                 │ │
│  │ created_at (TIMESTAMP)                                             │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                                                                           │
│  ┌────────────────────────────────────────────────────────────────────┐ │
│  │ GITHUB_CONNECTIONS (Phase 2)                                       │ │
│  ├────────────────────────────────────────────────────────────────────┤ │
│  │ id (UUID, PK)                                                      │ │
│  │ user_id (UUID, FK → users.id, UNIQUE)                              │ │
│  │ github_username (VARCHAR)                                          │ │
│  │ github_user_id (INTEGER)                                           │ │
│  │ access_token (VARCHAR) [encrypted]                                 │ │
│  │ refresh_token (VARCHAR, NULL) [encrypted]                          │ │
│  │ token_expires_at (TIMESTAMP, NULL)                                 │ │
│  │ connected_at (TIMESTAMP)                                           │ │
│  │ disconnected_at (TIMESTAMP, NULL)                                  │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Table Definitions

### USERS
Store user account information.

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) NOT NULL UNIQUE,
  full_name VARCHAR(255),
  avatar_url VARCHAR(512),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_created_at ON users(created_at);
```

**Constraints:**
- Email is unique (prevents duplicate accounts)
- All timestamps default to current time

**Notes:**
- Password handled by Supabase Auth (not stored in this table)
- User ID is UUID (provided by Supabase)

---

### PROJECTS
Store project metadata.

```sql
CREATE TABLE projects (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  status VARCHAR(50) NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'archived')),
  priority VARCHAR(50) NOT NULL DEFAULT 'medium' CHECK (priority IN ('low', 'medium', 'high', 'critical')),
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_projects_user_id ON projects(user_id);
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_projects_created_at ON projects(created_at);
```

**Constraints:**
- user_id is required (every project belongs to a user)
- status and priority are enums (enforced with CHECK)
- Cascading delete: removing user deletes all projects

**Notes:**
- Users can archive projects (soft delete alternative)
- Multiple projects per user allowed

---

### BOARDS
One Kanban board per project.

```sql
CREATE TABLE boards (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id UUID NOT NULL UNIQUE REFERENCES projects(id) ON DELETE CASCADE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_boards_project_id ON boards(project_id);
```

**Constraints:**
- Unique constraint on project_id (one board per project)
- Cascading delete: removing project deletes board

**Notes:**
- Simple table that links projects to columns
- Default columns created via migration/seeding

---

### COLUMNS
Board columns (Ideas, Planning, Backlog, In Progress, Testing, Completed).

```sql
CREATE TABLE columns (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  board_id UUID NOT NULL REFERENCES boards(id) ON DELETE CASCADE,
  name VARCHAR(255) NOT NULL,
  "order" INTEGER NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_columns_board_id ON columns(board_id);
CREATE UNIQUE INDEX idx_columns_board_order ON columns(board_id, "order");
```

**Constraints:**
- board_id is required
- order field maintains column sequence
- Unique constraint on (board_id, order) prevents duplicate positions

**Notes:**
- "order" is quoted because it's a reserved keyword in SQL
- Default 6 columns created automatically

---

### TASKS
Individual tasks/cards in columns.

```sql
CREATE TABLE tasks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  column_id UUID NOT NULL REFERENCES columns(id) ON DELETE CASCADE,
  project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  priority VARCHAR(50) NOT NULL DEFAULT 'medium' CHECK (priority IN ('low', 'medium', 'high')),
  status VARCHAR(50) NOT NULL DEFAULT 'todo' CHECK (status IN ('todo', 'in_progress', 'done')),
  due_date DATE,
  story_points INTEGER CHECK (story_points > 0),
  "order" INTEGER NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_tasks_column_id ON tasks(column_id);
CREATE INDEX idx_tasks_project_id ON tasks(project_id);
CREATE INDEX idx_tasks_status ON tasks(status);
CREATE INDEX idx_tasks_due_date ON tasks(due_date);
CREATE UNIQUE INDEX idx_tasks_column_order ON tasks(column_id, "order");
```

**Constraints:**
- column_id and project_id are required
- Cascading delete: removing column deletes tasks
- priority and status are enums
- story_points must be positive
- Unique constraint on (column_id, order)

**Notes:**
- project_id denormalized for faster queries
- Supports drag-and-drop with order field

---

### LABELS
Task labels/tags (e.g., "bug", "feature", "urgent").

```sql
CREATE TABLE labels (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
  name VARCHAR(100) NOT NULL,
  color VARCHAR(7) NOT NULL DEFAULT '#808080',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_labels_project_id ON labels(project_id);
CREATE UNIQUE INDEX idx_labels_project_name ON labels(project_id, name);
```

**Constraints:**
- project_id is required (labels are project-specific)
- Unique constraint on (project_id, name)
- color is hex color code (#RRGGBB format)

**Notes:**
- Scoped to projects (different projects can have same label names)
- Cascading delete with project

---

### TASK_LABELS
Junction table for N:M relationship between tasks and labels.

```sql
CREATE TABLE task_labels (
  task_id UUID NOT NULL REFERENCES tasks(id) ON DELETE CASCADE,
  label_id UUID NOT NULL REFERENCES labels(id) ON DELETE CASCADE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (task_id, label_id)
);

CREATE INDEX idx_task_labels_label_id ON task_labels(label_id);
```

**Constraints:**
- Composite primary key prevents duplicate assignments
- Cascading delete from both tables

**Notes:**
- Many-to-many relationship
- Track when label was added to task

---

### ACTIVITY_LOGS
Event log for audit trail and activity feed.

```sql
CREATE TABLE activity_logs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
  task_id UUID REFERENCES tasks(id) ON DELETE SET NULL,
  action VARCHAR(50) NOT NULL CHECK (action IN (
    'task_created', 'task_updated', 'task_moved', 'task_completed',
    'task_deleted', 'project_created', 'project_updated', 'project_archived',
    'project_deleted'
  )),
  description TEXT NOT NULL,
  metadata JSONB,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_activity_logs_user_id ON activity_logs(user_id);
CREATE INDEX idx_activity_logs_project_id ON activity_logs(project_id);
CREATE INDEX idx_activity_logs_task_id ON activity_logs(task_id);
CREATE INDEX idx_activity_logs_created_at ON activity_logs(created_at);
CREATE INDEX idx_activity_logs_action ON activity_logs(action);
```

**Constraints:**
- action is enum (limited set of events)
- task_id is nullable (project events don't have task_id)
- Cascading deletes on user/project, SET NULL on task (preserve log even if task deleted)

**Notes:**
- JSONB metadata stores additional context (e.g., old values, new values)
- Indexed on created_at for feed queries
- Primary data source for dashboard metrics

---

### GITHUB_CONNECTIONS (Phase 2)
Store GitHub OAuth connection per user.

```sql
CREATE TABLE github_connections (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE,
  github_username VARCHAR(255) NOT NULL,
  github_user_id INTEGER NOT NULL,
  access_token VARCHAR(512) NOT NULL,
  refresh_token VARCHAR(512),
  token_expires_at TIMESTAMP,
  connected_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  disconnected_at TIMESTAMP,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_github_connections_user_id ON github_connections(user_id);
CREATE INDEX idx_github_connections_github_user_id ON github_connections(github_user_id);
```

**Constraints:**
- Unique constraint on user_id (one GitHub connection per user)
- Cascading delete with user

**Notes:**
- Tokens should be encrypted at rest (handled by backend)
- disconnected_at allows tracking disconnection history
- Phase 2 feature - not required for MVP

---

## Database Design Principles

### Normalization (3NF)
- No data duplication
- Proper use of foreign keys
- Project_id denormalized in tasks for performance (acceptable deviation)

### Performance
- Indexes on frequently queried columns
- Foreign key columns indexed
- Composite indexes for common query patterns
- Order columns for drag-and-drop support

### Data Integrity
- Foreign key constraints enforce referential integrity
- Check constraints enforce valid enum values
- Unique constraints prevent duplicates
- Cascading deletes prevent orphaned records

### Timestamps
- created_at: Immutable record creation time
- updated_at: Mutable record modification time
- Both default to CURRENT_TIMESTAMP
- Used for sorting, filtering, and audit trails

### User Data Isolation
- All queries filtered by user_id
- Supabase RLS policies enforce at database level
- Users cannot access other users' data

---

## Migration Strategy

### Migration Files
Each schema change gets a timestamped migration file.

Example: `alembic/versions/2024_01_01_001_create_users_table.py`

### Rollback Safety
- Every migration includes both upgrade and downgrade paths
- Can rollback to any previous state
- Test rollbacks before production

### Production Deployment
1. Back up production database
2. Run migration on staging
3. Verify data integrity
4. Run migration on production
5. Monitor for issues

---

## Initial Data (Seeding)

### Default Board Columns
When a project is created, auto-create these columns:
```
1. Ideas (order: 1)
2. Planning (order: 2)
3. Backlog (order: 3)
4. In Progress (order: 4)
5. Testing (order: 5)
6. Completed (order: 6)
```

---

## Future Enhancements (Phase 2+)

### Additional Tables
- `project_members` - For team collaboration
- `task_comments` - For task discussions
- `task_attachments` - For file uploads
- `notifications` - For alert system
- `time_tracking` - For time logs

### Indexes to Add
- Composite indexes for common filter combinations
- Partial indexes for soft deletes
- Full-text search indexes for description/title

### Partitioning
- Partition activity_logs by date (if > 10M rows)
- Partition tasks by project (if > 50M rows)

