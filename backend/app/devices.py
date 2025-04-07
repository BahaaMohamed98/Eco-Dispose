from flask import Blueprint

devices = Blueprint("devices", __name__)


@devices.get("/")
def index():
    return "<h1>Hello, world</h1>"
