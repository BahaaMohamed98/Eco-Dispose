from flask import Flask
from .models import db


def create_app():
    app = Flask(__name__)
    app.secret_key = "dev"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    db.init_app(app)

    from .auth import auth
    from .devices import devices

    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(devices, url_prefix="/devices")

    with app.app_context():
        db.create_all()

    return app
