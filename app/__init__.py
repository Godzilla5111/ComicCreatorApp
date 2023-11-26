# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        # Import parts of our application
        from .views import app_routes

        # Register Blueprints
        app.register_blueprint(app_routes)

        return app
