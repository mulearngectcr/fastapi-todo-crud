# ToDo API

A simple in-memory ToDo REST API built with FastAPI as part of the AI for Builders cohort (Month 1, Sprint B).

## Features

- Create, read, update, and partially update todos
- In-memory storage (data resets on server restart)
- Full CRUD-style operations following REST conventions

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn

## Setup

1. Clone the repo and navigate into the project folder.

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install "fastapi[standard]"
   ```

4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

5. Open the interactive docs at:
   ```
   http://127.0.0.1:8000/docs
   ```

## Endpoints

| Method | Endpoint         | Description                          |
|--------|------------------|---------------------------------------|
| GET    | `/`              | Health check / welcome message       |
| GET    | `/todos`         | Get all todos                        |
| GET    | `/todo/{id}`     | Get a single todo by ID              |
| POST   | `/todos`         | Create a new todo                    |
| PUT    | `/todos/{id}`    | Fully update an existing todo        |
| PATCH  | `/todos/{id}`    | Mark a todo as checked (`checked: true`) |

### Example todo object

```json
{
  "id": 1,
  "title": "Buy Bread",
  "checked": false,
  "priority": "low"
}
```

### Testing the endpoints

All endpoints can be tested directly through the interactive Swagger UI at `/docs`:

- **POST `/todos`** — expand the endpoint, click "Try it out", and paste a todo object (like the example above) into the request body.
- **GET `/todos`** — click "Try it out" then "Execute" to view all current todos.
- **GET `/todo/{id}`** — enter an existing todo's `id` and execute to fetch that single todo.
- **PUT `/todos/{id}`** — enter the `id` to update, and provide a full replacement object (`title`, `checked`, `priority`) in the request body.
- **PATCH `/todos/{id}`** — enter the `id` and execute; no request body needed, it simply marks that todo as `checked: true`.

## Notes

- Data is stored in a Python list in memory — it resets whenever the server restarts (including on auto-reload triggered by saving code changes).
- IDs and request bodies must be valid JSON (lowercase `true`/`false`, double-quoted keys/strings).
