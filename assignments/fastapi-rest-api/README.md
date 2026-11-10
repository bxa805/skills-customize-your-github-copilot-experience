# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small task-list REST API with FastAPI. Practice defining routes, validating JSON request bodies, and implementing create, read, update, and delete operations.

## 📝 Tasks

### 🛠️ Create and Run the API

#### Description
Use the provided starter code to create a FastAPI application with a health-check endpoint. Install FastAPI and its standard tools, then run the application.

```bash
python -m pip install "fastapi[standard]"
python starter-code.py
```

#### Requirements
Completed program should:

- Define a FastAPI application
- Add a `GET /health` endpoint that returns `{"status": "ok"}`
- Start locally and show the interactive API documentation at `/docs`


### 🛠️ Create and List Tasks

#### Description
Add endpoints to create tasks and retrieve the task list. Each task should have an integer ID, a title, and a completion status. Keep tasks in memory; a database is not required.

#### Requirements
Completed program should:

- Use the provided Pydantic model to validate task request data
- Add a `POST /tasks` endpoint that creates a task and assigns it a unique ID
- Default a new task's `done` value to `false` when it is not provided
- Add a `GET /tasks` endpoint that returns all tasks as JSON


### 🛠️ Read, Update, and Delete Tasks

#### Description
Complete the task API by adding endpoints to retrieve, update, and delete a task by its ID.

#### Requirements
Completed program should:

- Add `GET /tasks/{task_id}` to return one task
- Add `PUT /tasks/{task_id}` to update a task's title and completion status
- Add `DELETE /tasks/{task_id}` to remove a task
- Return an HTTP 404 response when an endpoint refers to an ID that does not exist
- Verify the endpoints and their JSON responses using `/docs`