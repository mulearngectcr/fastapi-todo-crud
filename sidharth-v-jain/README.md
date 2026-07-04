# Todo CRUD API

A simple in-memory Todo Management API built with FastAPI. In this implementation, I went with the recommended Pydantic classes approach for better testability. 
I implemented the required features, and the bonus challenge for the PATCH request.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn main:app --reload
```

## Usage

Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive API docs.

| Method | Endpoint              | Description          |
|--------|-----------------------|-----------------------|
| GET    | /todos                | List all todos       |
| GET    | /todos/{id}           | Get a single todo    |
| POST   | /todos                | Create a todo        |
| PUT    | /todos/{id}           | Update a todo        |
| DELETE | /todos/{id}           | Delete a todo        |
| PATCH  | /todos/{id}/complete  | Mark a todo as done  |

Data is stored in memory and resets whenever the server restarts.
