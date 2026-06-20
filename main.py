from fastapi import FastAPI 

app=FastAPI() 

@app.get("/")
def home():
    return {"message":"Hello world from Fastapi  vern"}



@app.get("/about")
def about():
    return {"message":"This is about page of Fastapi  vern"}

# @app.get("/users")
# def users():
#     return {"message":"This is users page of Fastapi  vern"}

# @app.get("/users/{user_id}")
# def get_user(user_id):
#     return {"user_id":user_id}



# @app.get("/users/{user_id}")
# def get_user(user_id:int):
#     return {"user_id":user_id}


@app.get("/users/{user_id}")
def get_user(user_id:str):
    return {"user_id":user_id}

@app.get("/users")
def users(name:str):
    return {"Name":name}

@app.get("/products")
def products(limit:int=10):
    return {"limit":limit}

@app.get("/items")
def items(name:str=None, price:int=0):
    return {"name":name, "price":price}