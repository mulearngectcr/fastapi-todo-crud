from enum import Enum
from memory import load_memory, save_memory
from fastapi import FastAPI
from pydantic import BaseModel


class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Todo(BaseModel):
    id: int
    title: str
    checked: bool
    priority: Priority

    
app = FastAPI()

@app.get("/todos")
def read():
    return load_memory()

@app.get("/todos/{id}")
def read_todo(id: int):
    memory=load_memory()
    for todo in memory:
        if todo['id']==id:
            return todo
    return {"error": "Todo not found"}

@app.post("/todos")
def create_todo(todo: Todo):
    memory=load_memory()
    memory.append(todo.dict())
    save_memory(memory)
    return todo

@app.put("/todos/{id}")
def update_todo(id: int, todo: Todo):
    memory=load_memory()
    for todos in memory:
        if todos['id']==id:
            todos.update(todo.dict())
            save_memory(memory)
            return todo
    return {'error': 'Todo not found'}

@app.delete("/todos/{id}")
def delete_todo(id: int):
    memory=load_memory()
    for item in memory:
        if item['id']==id:
            memory.remove(item)
            save_memory(memory)
            return {'message': 'Todo deleted successfully'}
    return {'error': 'Todo not found'}
          
