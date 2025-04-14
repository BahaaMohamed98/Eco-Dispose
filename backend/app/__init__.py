import os

from dotenv import load_dotenv
from flask import Flask, jsonify

from .auth import login_manager
from .config import UPLOAD_FOLDER
from .models import db


def create_app():
    app = Flask(__name__)

    load_dotenv()
    app.secret_key = os.getenv("SECRET_KEY")

    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1000 * 1000

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    db.init_app(app)

    login_manager.init_app(app)

    from .auth import auth
    from .devices import devices

    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(devices, url_prefix="/devices")

    # Global error handler for 404 (Page Not Found)
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Resource not found"}), 404

    # Global error handler for 500 (Internal Server Error)
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "An unexpected error occurred"}), 500

    with app.app_context():
        db.create_all()

    return app
