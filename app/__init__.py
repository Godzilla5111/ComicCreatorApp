# # app/__init__.py
# from flask import Flask

# def create_app():
#     app = Flask(__name__)

#     with app.app_context():
#         # Import parts of our application
#         from .views import app_routes

#         # Register Blueprints
#         app.register_blueprint(app_routes)

#         return app
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

def create_app():
    app = Flask(__name__)

    # Initialize Flask-Limiter with the application and key function
    limiter = Limiter(key_func=get_remote_address)

    # Apply the limiter to the app
    limiter.init_app(app)

    from app.views import app_routes
    app.register_blueprint(app_routes)

    return app


