from flask import Flask, render_template, request, redirect, url_for
from storage import load_todos, save_todos

app = Flask(__name__)
todos = load_todos()


@app.route('/todos', methods=['GET'])
def todo_list():
    return render_template('todos.html', todos=todos)


@app.route('/todos/add', methods=['POST'])
def add_todo():
    todo_item = request.form['todo_item']
    todos.append(todo_item)
    save_todos(todos)
    return redirect(url_for('todo_list'))


@app.route('/todos/delete/<todo_item>', methods=['POST'])
def delete_todo(todo_item):
    todos.remove(todo_item)
    save_todos(todos)
    return redirect(url_for('todo_list'))


if __name__ == '__main__':
    app.run(debug=True)
