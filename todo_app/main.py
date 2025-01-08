from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TodoItem(BaseModel):
    title: str
    description: str = None
    completed: bool = False

todo_list = []

@app.post("/items")
def create_item(item: TodoItem):
    todo_list.append(item)
    return item

@app.get("/items")
def get_items():
    return todo_list
