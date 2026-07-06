from fastapi import FastAPI

app = FastAPI()

todos = []

@app.get("/")
def home():
    return {
        "message" : "ToDo API is running"
    }

@app.get("/todos")
def getall():
    return todos

@app.get("/todo/{id}")
def get_todo(id: int):
    for todo in todos:
        if todo["id"] == id:
            return todo
    
    return {
        "message" : "ToDo not found"
    }
        
@app.post("/todos")
def create_todo(todo: dict):
    todos.append(todo)
    return {
        "message" : "ToDo added successfully"
    }

@app.put("/todos/{id}")
def update_todo(id: int, new_todo: dict):
    for todo in todos:
        if todo["id"] == id:
            todo["title"] = new_todo["title"]
            todo["checked"] = new_todo["checked"]
            todo["priority"] = new_todo["priority"]

            return {
                "message" : "ToDo updated successfully"
            }
    return {
        "message" : "ToDo not found"
    }
        
@app.patch("/todos/{id}")
def update_checked(id: int):
    for todo in todos:
        if todo["id"] == id:
            todo["checked"] = True
            return {
                "message" : "ToDo checked successfully"
            }
    
    return {
        "message" : "ToDo not found"
    }