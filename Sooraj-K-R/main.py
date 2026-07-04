from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
todos_db = []

class Priority(str, Enum):
    low = "low"
    med = "med"
    high = "high"

class ToDoItem(BaseModel):
    id: int
    title: str
    checked: bool 
    priority: Priority

@app.post('/todos')
def insert_item(item: ToDoItem):
    todos_db.append(item)
    return item 

@app.get('/todos')
def get_all(priority: Optional[Priority] = None, checked: Optional[bool] = None):
    filtered_todos = todos_db
    
    if priority:
        filtered_todos = [todo for todo in filtered_todos if todo.priority == priority]
    
    if checked is not None:
        filtered_todos = [todo for todo in filtered_todos if todo.checked == checked]
        
    return filtered_todos

@app.get('/todos/{id}')
def get_item(id: int):
    for i in todos_db:
        if i.id == id:
            return i
        
@app.put('/todos/{id}')
def update_item(id: int, item: ToDoItem):
    for index,i in enumerate(todos_db):
        if i.id == id:
            todos_db[index] = item
            return item 
    
@app.delete('/todos/{id}')
def delete_item(id: int):
    for i in todos_db:
        if i.id == id:
            todos_db.remove(i)
    return {"message": "Todo deleted"}

@app.patch('/todos/{id}/complete')
def mark_as_done(id: int):
    for i in todos_db:
        if i.id == id:
            i.checked = True
            return i 

