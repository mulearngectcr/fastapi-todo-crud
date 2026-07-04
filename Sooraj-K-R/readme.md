# FastAPI Todo CRUD API

A simple RESTful Todo API built with **FastAPI** and **Pydantic**.

## Features

- **Create** a todo item (`POST /todos`)
- **Read** all todos with optional filtering by priority and status (`GET /todos`)
- **Read** a single todo by ID (`GET /todos/{id}`)
- **Update** a todo item (`PUT /todos/{id}`)
- **Delete** a todo item (`DELETE /todos/{id}`)
- **Mark as complete** (`PATCH /todos/{id}/complete`)

## Tech Stack

- Python
- FastAPI
- Pydantic

## How to Run

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

API docs available at `http://127.0.0.1:8000/docs`.
