from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Task List API")


class TaskInput(BaseModel):
    title: str
    done: bool = False


tasks = []
next_task_id = 1


@app.get("/health")
def health_check():
    pass


@app.get("/tasks")
def list_tasks():
    pass


@app.post("/tasks")
def create_task(task: TaskInput):
    global next_task_id
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskInput):
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)