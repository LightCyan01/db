# FastAPI PostgreSQL Task API

A simple CRUD API built with FastAPI, PostgreSQL, and Docker.

PostgreSQL runs in a Docker container and stores task data in a persistent Docker volume.

## Setup

Copy the example environment file:

```powershell
Copy-Item .env.example .env
```

Start the entire stack:

```powershell
docker compose up
```

Swagger docs:

```text
http://localhost:3000/docs
```

## Environment

See `.env.example` for the required environment variables.

```env
DATABASE_URL=postgres://postgres:dev@db:5432/tasks
```

## Endpoints

| Method | Endpoint |
|---|---|
| GET | `/tasks` |
| GET | `/tasks/{id}` |
| POST | `/tasks` |
| PUT | `/tasks/{id}` |
| DELETE | `/tasks/{id}` |

## Example Request

```powershell
curl.exe -i http://localhost:3000/tasks
```

## Database Screenshot

<a href="https://ibb.co/0p8qFN7t"><img src="https://i.ibb.co/fVBMnRgv/image-2026-08-11-082509146.png" alt="PostgreSQL tasks database screenshot" border="0"></a>

The database is created automatically and three example tasks are seeded when the table is empty. Data persists across `docker compose down` and `docker compose up` because PostgreSQL uses a Docker volume.
