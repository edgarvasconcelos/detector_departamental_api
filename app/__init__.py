from flask import Flask
from flask_cors import CORS
from app.routes import configure_routes
from dotenv import load_dotenv 
import os
from config import DevelopmentConfig, ProductionConfig

def create_app():
    """
    Factory function to create and configure the Flask app.

    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(__name__)
    load_dotenv()  # Carregar o arquivo .env
    flask_env = os.getenv('FLASK_ENV', 'production')
    if flask_env == 'development':
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(ProductionConfig)
    CORS(app, resources={r"/*": {"origins": "*"}})
    configure_routes(app)
    return app
