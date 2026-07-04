from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    id: int
    title: str
    checked: bool
    priority: str

all_todos = []

app = FastAPI()

#GET, POST, PUT, DELETE

@app.get("/todos")
def get_todos(priority: Optional[str] = None, checked: Optional[bool] = None):
    todos = all_todos
    if priority is not None:
        todos = [todo for todo in todos if todo.priority == priority]
    if checked is not None:
        todos = [todo for todo in todos if todo.checked == checked]
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.id == todo_id:
            return todo
    return {"error": "Todo not found"}

#the allowed priority values are "low", "medium", and "high"

@app.post("/todos")
def create_todo(todo: Todo):
    all_todos.append(todo)
    return todo

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    for index, existing_todo in enumerate(all_todos):
        if existing_todo.id == todo_id:
            all_todos[index] = todo
            return todo
    return {"error": "Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, existing_todo in enumerate(all_todos):
        if existing_todo.id == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    return {"error": "Todo not found"}

@app.patch("/todos/{todo_id}")
def patch_todo(todo_id: int, todo: Todo):
    for index, existing_todo in enumerate(all_todos):
        if existing_todo.id == todo_id:
            all_todos[index] = todo
            return todo
    return {"error": "Todo not found"}

