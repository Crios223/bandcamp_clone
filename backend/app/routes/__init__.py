from flask import Blueprint
from .albums_routes import albums_bp

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return "Bandcamp Backend is working!"