from flask import Flask

from app.routes import todos_routes

app = Flask(__name__)

# Register the routes from the separate routes file
app.register_blueprint(todos_routes)
