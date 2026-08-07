# FastAPI SQLite Task API

A simple CRUD API built with FastAPI and SQLite.

## Why SQLite?

SQLite uses a single database file, requires no separate setup, and keeps data after the server restarts.

The database is stored in `tasks.db` and is created automatically when the app starts. If the `tasks` table is empty, three example tasks are seeded automatically.

## Run

```powershell
py -m pip install -r requirements.txt
py -m uvicorn main:app --reload
```

Swagger docs:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

```text
GET     /tasks
GET     /tasks/{id}
POST    /tasks
PUT     /tasks/{id}
DELETE  /tasks/{id}
```

## Example SQL

```sql
SELECT * FROM tasks;
```

## Database Screenshots

[![Database screenshot 1](https://i.ibb.co/zWG3FG6Y/Untitled.jpg)](https://ibb.co/ZRWQSW2P)

[![Database screenshot 2](https://i.ibb.co/Nn3jF2PW/Untitled1.jpg)](https://ibb.co/93vTpHLy)

`tasks.db` can be added to `.gitignore` because the application recreates it automatically on a fresh start.
