# API Documentation

DevBoard REST API v1

**Base URL**: `https://api.devboard.com/api/v1`

## Authentication

All endpoints (except `/auth/*`) require JWT token in Authorization header:

```
Authorization: Bearer <token>
```

## Response Format

### Success Response

```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "name": "Example"
  },
  "message": "Optional success message"
}
```

### Error Response

```json
{
  "success": false,
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Human readable error message"
  }
}
```

## Endpoints

### Authentication

#### Sign Up
```
POST /auth/signup
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response**: 201 Created
```json
{
  "success": true,
  "data": {
    "user_id": "uuid",
    "email": "user@example.com",
    "access_token": "token"
  }
}
```

#### Login
```
POST /auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response**: 200 OK
```json
{
  "success": true,
  "data": {
    "user_id": "uuid",
    "email": "user@example.com",
    "access_token": "token"
  }
}
```

#### Logout
```
POST /auth/logout
Authorization: Bearer <token>
```

**Response**: 200 OK

#### Get Current User
```
GET /auth/me
Authorization: Bearer <token>
```

**Response**: 200 OK
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "email": "user@example.com",
    "full_name": "John Doe",
    "avatar_url": "https://..."
  }
}
```

#### Refresh Token
```
POST /auth/refresh
Authorization: Bearer <token>
```

**Response**: 200 OK
```json
{
  "success": true,
  "data": {
    "access_token": "new_token"
  }
}
```

---

### Projects

#### List Projects
```
GET /projects
Authorization: Bearer <token>
```

**Query Parameters**:
- `status`: Filter by status (active, archived)
- `priority`: Filter by priority (low, medium, high, critical)
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 10)

**Response**: 200 OK
```json
{
  "success": true,
  "data": [
    {
      "id": "uuid",
      "name": "Project Name",
      "description": "Description",
      "status": "active",
      "priority": "high",
      "created_at": "2024-01-01T00:00:00Z",
      "updated_at": "2024-01-01T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 5
  }
}
```

#### Get Project
```
GET /projects/{project_id}
Authorization: Bearer <token>
```

**Response**: 200 OK
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "name": "Project Name",
    "description": "Description",
    "status": "active",
    "priority": "high",
    "board_id": "uuid",
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2024-01-01T00:00:00Z"
  }
}
```

#### Create Project
```
POST /projects
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "New Project",
  "description": "Project description",
  "priority": "high"
}
```

**Response**: 201 Created

#### Update Project
```
PUT /projects/{project_id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "Updated Name",
  "description": "Updated description",
  "priority": "medium"
}
```

**Response**: 200 OK

#### Delete Project
```
DELETE /projects/{project_id}
Authorization: Bearer <token>
```

**Response**: 204 No Content

#### Archive Project
```
PATCH /projects/{project_id}/archive
Authorization: Bearer <token>
```

**Response**: 200 OK

---

### Kanban Board

#### Get Board
```
GET /projects/{project_id}/board
Authorization: Bearer <token>
```

**Response**: 200 OK
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "project_id": "uuid",
    "columns": [
      {
        "id": "uuid",
        "name": "Ideas",
        "order": 1,
        "tasks": [
          {
            "id": "uuid",
            "title": "Task Title",
            "description": "Task description",
            "priority": "high",
            "status": "todo",
            "due_date": "2024-12-31",
            "story_points": 5,
            "labels": ["bug", "urgent"]
          }
        ]
      }
    ]
  }
}
```

---

### Tasks

#### Create Task
```
POST /tasks
Authorization: Bearer <token>
Content-Type: application/json

{
  "project_id": "uuid",
  "column_id": "uuid",
  "title": "New Task",
  "description": "Task description",
  "priority": "high",
  "due_date": "2024-12-31",
  "story_points": 5
}
```

**Response**: 201 Created

#### Update Task
```
PUT /tasks/{task_id}
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Updated Title",
  "priority": "medium",
  "story_points": 3
}
```

**Response**: 200 OK

#### Delete Task
```
DELETE /tasks/{task_id}
Authorization: Bearer <token>
```

**Response**: 204 No Content

#### Move Task
```
PATCH /tasks/{task_id}/move
Authorization: Bearer <token>
Content-Type: application/json

{
  "column_id": "new_column_id",
  "order": 1
}
```

**Response**: 200 OK

---

### Labels

#### Create Label
```
POST /projects/{project_id}/labels
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "bug",
  "color": "#FF0000"
}
```

**Response**: 201 Created

#### Add Label to Task
```
POST /tasks/{task_id}/labels/{label_id}
Authorization: Bearer <token>
```

**Response**: 200 OK

#### Remove Label from Task
```
DELETE /tasks/{task_id}/labels/{label_id}
Authorization: Bearer <token>
```

**Response**: 204 No Content

---

### Activity

#### Get Activity Logs
```
GET /projects/{project_id}/activity
Authorization: Bearer <token>
```

**Query Parameters**:
- `limit`: Items per page (default: 20)
- `offset`: Skip N items (default: 0)

**Response**: 200 OK
```json
{
  "success": true,
  "data": [
    {
      "id": "uuid",
      "user_id": "uuid",
      "action": "task_created",
      "description": "Created task 'New Feature'",
      "task_id": "uuid",
      "metadata": {},
      "created_at": "2024-01-01T00:00:00Z"
    }
  ]
}
```

---

### Dashboard

#### Get Dashboard Metrics
```
GET /dashboard
Authorization: Bearer <token>
```

**Response**: 200 OK
```json
{
  "success": true,
  "data": {
    "total_projects": 5,
    "active_projects": 3,
    "completed_projects": 2,
    "total_tasks": 25,
    "completed_tasks": 10,
    "open_tasks": 15,
    "recent_activity": [
      {
        "id": "uuid",
        "action": "task_completed",
        "description": "Completed task 'Fix bug'",
        "created_at": "2024-01-01T00:00:00Z"
      }
    ]
  }
}
```

---

## Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `INVALID_REQUEST` | 400 | Invalid request format |
| `UNAUTHORIZED` | 401 | Missing or invalid token |
| `FORBIDDEN` | 403 | Access denied |
| `NOT_FOUND` | 404 | Resource not found |
| `CONFLICT` | 409 | Resource already exists |
| `VALIDATION_ERROR` | 422 | Validation failed |
| `INTERNAL_ERROR` | 500 | Server error |

---

## Rate Limiting

- **Limit**: 1000 requests per hour per user
- **Header**: `X-RateLimit-Remaining`

---

## Pagination

For list endpoints:

**Request**:
```
GET /projects?page=2&limit=20
```

**Response**:
```json
{
  "success": true,
  "data": [...],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 150,
    "pages": 8
  }
}
```

---

## Interactive Docs

Access interactive API documentation at:
- **Swagger UI**: `/docs`
- **ReDoc**: `/redoc`
- **OpenAPI Schema**: `/openapi.json`

---

## Examples

### Example: Create and Move Task

```bash
# 1. Create project
curl -X POST https://api.devboard.com/api/v1/projects \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name":"My Project"}'

# 2. Get board
curl https://api.devboard.com/api/v1/projects/$PROJECT_ID/board \
  -H "Authorization: Bearer $TOKEN"

# 3. Create task
curl -X POST https://api.devboard.com/api/v1/tasks \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "project_id":"$PROJECT_ID",
    "column_id":"$COLUMN_ID",
    "title":"New Task",
    "priority":"high"
  }'

# 4. Move task
curl -X PATCH https://api.devboard.com/api/v1/tasks/$TASK_ID/move \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"column_id":"$NEW_COLUMN_ID","order":1}'
```

