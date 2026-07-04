from enum import Enum
from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Todo CRUD API")

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Todo(BaseModel):
    id: int
    title: str
    checked: bool = False
    priority: Priority = Priority.medium


class TodoCreate(BaseModel):
    title: str
    checked: bool = False
    priority: Priority = Priority.medium


class TodoUpdate(BaseModel):
    title: str
    checked: bool = False
    priority: Priority = Priority.medium


todos: List[Todo] = []


def find_todo(todo_id: int) -> Optional[Todo]:
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return None


@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    todo = find_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(todo_in: TodoCreate):
    new_id = max((todo.id for todo in todos), default=0) + 1
    new_todo = Todo(id=new_id, **todo_in.dict())
    todos.append(new_todo)
    return new_todo


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_in: TodoUpdate):
    todo = find_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.title = todo_in.title
    todo.checked = todo_in.checked
    todo.priority = todo_in.priority
    return todo


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    todo = find_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos.remove(todo)
    return None


@app.patch("/todos/{todo_id}/complete", response_model=Todo)
def complete_todo(todo_id: int):
    todo = find_todo(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.checked = True
    return todo
