import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

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
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    app.config["SESSION_COOKIE_SECURE"] = False
    app.config["SESSION_COOKIE_HTTPONLY"] = True
    db.init_app(app)

    CORS(
        app,
        origins=["http://localhost:3000", "http://localhost:8080"],
        supports_credentials=True,
    )

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
