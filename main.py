import json
from fastapi import FastAPI

with open('specs.json') as f:
    specs = json.loads(f.read())
    f.close()

description = """
Simple Todo List API.

## Tasks

You can **create tasks**, and manage them however you want.

"""

app = FastAPI(**specs, description=description)


@app.get('/')
def root():
    return "funfou"

@app.post("/todo")
def create_todo():
    return "create task"

@app.get("/todo/{id}")
def retrive_todo(id: int):
    return "retrive a single todo"

@app.put("/todo/{id}")
def update_todo(id: int):
    return "update todo"

@app.delete("/todo/{id}")
def delete_todo(id: int):
    return "delete todo item"

    
@app.get('/todo')
def root():
    return "retirve all todos"

