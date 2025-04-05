from flask import Blueprint

routes = Blueprint("routes", __name__)


@routes.route("/")
def index():
    return "<h1>Hello, world</h1>"
