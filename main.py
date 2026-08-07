import db   
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

db.create_table()
db.seed_tasks()

@app.get("/tasks")
def get_tasks():
    tasks = db.get_tasks()
    return tasks

@app.get("/tasks/{id}")
def get_tasks_id(id: int):
    task = db.get_tasks(id)
    
    if task is None:
        return JSONResponse(
            status_code=404,
            content={"error": "Task not found"}
        )
    return task
