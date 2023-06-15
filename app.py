from flask import Flask, redirect, url_for
from routes import todos_routes

app = Flask(__name__)

# Register the routes from the separate routes file
app.register_blueprint(todos_routes)
