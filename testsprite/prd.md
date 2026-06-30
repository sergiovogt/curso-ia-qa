# PRD — Gestor de Tareas (curso-ia-qa)

## Product overview

Web-based task manager that lets a logged-in user view a list of tasks and update their status. Single-user demo app; authentication is hardcoded (user: `demo` / password: `demo`). Runs at http://localhost:5000.

## Users

| Role | Description |
|------|-------------|
| Authenticated user | The only user type. Logs in with demo credentials, views and manages tasks. |

Unauthenticated requests are redirected to `/login`.

## Features

### 1. Authentication

- **Login page** (`GET /login`): form with `user` and `password` fields and a submit button.
- **Valid credentials** (`demo` / `demo`): redirects to the task list.
- **Invalid credentials**: stays on `/login` and shows an error message.
- **Logout** (`GET /logout`): clears the session and redirects to `/login`.

### 2. Task list

- **Route:** `GET /` (requires authentication).
- Displays all tasks in a table with at least two columns: **Title** and **Status**.
- Tasks are ordered by ID (ascending).
- Initial seed data (4 tasks):

| Title | Initial status |
|-------|----------------|
| Validar login con credenciales válidas | pendiente |
| Validar mensaje de error con clave incorrecta | pendiente |
| Revisar carga de la lista de tareas | en progreso |
| Probar cambio de estado de una tarea | pendiente |

### 3. Change task status

- Each task row has a control (dropdown or button) that sends `PATCH /tasks/:id` with `{ "estado": "<new_status>" }`.
- **Valid statuses:** `pendiente`, `en progreso`, `completada`.
- **Backend:** responds `200 { "id": <id>, "estado": "<new_status>" }` when the update succeeds.
- **Expected frontend behavior:** after a successful `PATCH`, the task's status cell in the list updates immediately — **without requiring a page reload**.
- **Error — invalid status:** backend responds `400 { "error": "estado inválido" }`.
- **Error — task not found:** backend responds `404 { "error": "tarea no encontrada" }`.

## Known bug — TASK-142

> **"El estado de la tarea no se actualiza en pantalla al cambiarlo"**

After `PATCH /tasks/:id` returns `200`, the frontend does **not** re-render the status cell in the list. The new status only becomes visible after a manual page reload. The backend stored the change correctly; the defect is exclusively in the frontend (missing DOM update after the API response).

**Expected:** status cell updates immediately after the change.  
**Actual:** status cell keeps showing the old value until the page is reloaded.

## API summary

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/login` | No | Login form |
| POST | `/login` | No | Submit credentials |
| GET | `/logout` | Yes | Clear session and redirect to login |
| GET | `/` | Yes | Task list |
| PATCH | `/tasks/:id` | Yes | Update task status |

## Out of scope

- Creating, deleting, or reordering tasks.
- Multiple users or roles.
- Pagination or search.
- Password change or registration.
