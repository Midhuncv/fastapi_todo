from fastapi import FastAPI

app = FastAPI()

todos = []

@app.get("/")
def read_root():
    return {"message": "FastAPI Todo App running!"}

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def add_todo(item: dict):
    todos.append(item)
    return {"message": "Todo added", "data": item}
