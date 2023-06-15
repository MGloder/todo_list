from flask import Flask, render_template, request, redirect, url_for

from storage import load_todos, save_todos

app = Flask(__name__)
todos = load_todos()


@app.route('/todos', methods=['GET'])
def todo_list():
    enumerated_todos = enumerate(todos, start=1)
    return render_template('todos.html', todos=enumerated_todos)


@app.route('/todos/add', methods=['POST'])
def add_todo():
    todo_item = request.form['todo_item']
    todos.append(todo_item)
    save_todos(todos)
    return redirect(url_for('todo_list'))


@app.route('/todos/complete/<int:index>', methods=['POST'])
def complete_todo(index):
    if 1 <= index <= len(todos):
        # Mark the todo item as complete (you can define your own logic here)
        # For demonstration purposes, let's append a prefix '[Complete]' to the todo item
        todos[index - 1] = '[Complete] ' + todos[index - 1]
    return redirect('/todos')


if __name__ == '__main__':
    app.run(debug=True)
