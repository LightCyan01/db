import db
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class TaskCreate(BaseModel):
    title: str | None = None

db.create_table()
db.seed_tasks()

@app.get("/tasks")
def get_tasks():
    tasks = db.get_tasks()
    return tasks

@app.get("/tasks/{id}")
def get_tasks_id(id: int):
    task = db.get_task(id)
    
    if task is None:
        return JSONResponse(
            status_code=404,
            content={"error": "Task not found"}
        )
    return task

@app.post("/tasks")
def create_task(task: TaskCreate):
    if task.title is None:
        return JSONResponse(
            status_code=400,
            content={"error": "Title is required"}
        )
    
    new_task = db.create_task(task.title)
    
    return JSONResponse(
        status_code=201,
        content=new_task
    )
        