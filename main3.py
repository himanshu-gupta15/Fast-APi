from fastapi import FastAPI 
from pydantic import BaseModel 

app=FastAPI()

todos=[]

class Todo(BaseModel):
    id:int
    title:str 
    complete:bool 

@app.post("/todo")
def create_todo(todo:Todo):
    todos.append(todo)
    return {
        "message":"Todo created successfully",
        "data":todo
    }

@app.get("/todo")
def get_todos():
    return todos

@app.get("/todo/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return todo
    return {"message":"Todo not found"}

@app.put("/todo/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[index]=updated_todo
            return {
                "message":"Data updated",
                "data":updated_todo
    
            }
    return {"message":"Todo not found"}
        

@app.delete("/todo/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos.pop(index)
            return {"message":"Todo deleted successfully"}
    return {"message":"Todo not found"}