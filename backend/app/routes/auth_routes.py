from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required
from app.models import User
from app import db

auth_routes = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    # Just for now - replace with hashed password check later
    if user and user.password == password:
        login_user(user)
        return jsonify(user.to_dict()), 200

    return jsonify({"message": "Invalid credentials"}), 401

@auth_routes.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out"}), 200

@auth_routes.route("/me", methods=["GET"])
@login_required
def get_current_user():
    from flask_login import current_user
    return jsonify(current_user.to_dict()), 200