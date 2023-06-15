import sqlite3


def init_database():
    conn = sqlite3.connect(':memory:', check_same_thread=False)  # Create an in-memory SQLite database
    cursor = conn.cursor()

    # Create the todos table
    cursor.execute('''
        CREATE TABLE todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            todo_item TEXT
        )
    ''')

    conn.commit()
    return conn


def load_todos(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT todo_item FROM todos')
    todos = [row[0] for row in cursor.fetchall()]
    return todos


def save_todos(conn, todos):
    cursor = conn.cursor()

    # Clear the existing todos
    cursor.execute('DELETE FROM todos')

    # Insert the new todos
    for todo_item in todos:
        cursor.execute('INSERT INTO todos (todo_item) VALUES (?)', (todo_item,))

    conn.commit()
