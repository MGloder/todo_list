import json

def load_todos():
    try:
        with open('todos.json', 'r') as f:
            todos = json.load(f)
    except FileNotFoundError:
        todos = []
    return todos

def save_todos(todos):
    with open('todos.json', 'w') as f:
        json.dump(todos, f)
