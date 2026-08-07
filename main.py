import db
from fastapi import FastAPI
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel

app = FastAPI()

class TaskCreate(BaseModel):
    title: str | None = None
    
class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None

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
    
@app.put("/tasks/{id}")
def update_task(id, task: TaskUpdate):
    
    if task.title is None:
        return JSONResponse(
            status_code=400,
            content={"error": "Title is required"}
        )
        
    if task.done is None:
        return JSONResponse(
            status_code=400,
            content={"error": "Done is required"}
        )
        
    updated_task = db.update_task(id, task.title, task.done)
    
    if updated_task is None:
        return JSONResponse(
            status_code=404,
            content={"error": "Task not found"}
        )
        
    return updated_task

@app.delete("/tasks/{id}")
def delete_task(id):
    deleted = db.delete_task(id)
    
    if not deleted:
        return JSONResponse(
            status_code=404,
            content={"error": "Task not found"}
        )
    return Response(status_code=204)