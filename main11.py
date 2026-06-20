#slq alchemy orm

import string

from sqlalchemy import Column, Integer, String, create_engine 

from sqlalchemy.orm import Session, sessionmaker, declarative_base ,session 

from fastapi import Depends, FastAPI, HTTPException 

app=FastAPI()

DATABASE_URL="sqlite:///./test1.db"

engine=create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

sessionLocal=sessionmaker(bind=engine)

Base=declarative_base()

class Todo(Base):
    __tablename__="todos"

    id=Column(Integer,primary_key=True,index=True) 
    title=Column(String)
    completed=Column(String)

Base.metadata.create_all(bind=engine)


def get_db():
    db=sessionLocal()
    try:
        yield db 
    finally:
        db.close() 


# @app.get("/")

# def home(db:Session=Depends(get_db)):
#     return {
#         "message":"DB connected fine"
#     }

# Create API 
@app.post("/todos") 
def create_todo(title:str,db:Session=Depends(get_db)):
    todo=Todo(title=title,completed="False")
    db.add(todo) 
    db.commit()
    db.refresh(todo)
    return {
        "message":"Todo Created",
        "data":todo 
    }

@app.get("/todos")
def get_todos(db:Session=Depends(get_db)):
    todos=db.query(Todo).all() 

    return {
        "Total":len(todos),
        "data":todos 
    }

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()

    if not todo:
        raise HTTPException(status_code=404,detail="Todo not found")
    
    return todo

#update 

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,title:str,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()

    if not todo:
        raise HTTPException(status_code=404,detail="Todo not found")
    
    todo.title=title

    db.commit()
    db.refresh(todo)

    return {
        "message":"Todo updated successfully",
        "data":todo
    }

# delete 

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
        raise HTTPException(status_code=404,detail="Todo not found")
    
    db.delete(todo)
    db.commit()
    

    return {
        "message":"Todo deleted successfully",
       
    }
