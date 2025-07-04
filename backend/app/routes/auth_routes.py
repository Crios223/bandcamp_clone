# from flask import Blueprint, request, jsonify
# from flask_login import login_user, logout_user, login_required, current_user
# from app.models import User
# from app import db

# auth_routes = Blueprint("auth", __name__, url_prefix="/api/auth")

# # -------- LOGIN --------
# @auth_routes.route("/login", methods=["POST"])
# def login():
#     data = request.get_json()
#     email = data.get("email")
#     password = data.get("password")

#     if not email or not password:
#         return jsonify({"message": "Email and password required"}), 400

#     user = User.query.filter_by(email=email).first()

#     if user and user.check_password(password):
#         login_user(user)
#         return jsonify(user.to_dict()), 200

#     return jsonify({"message": "Invalid credentials"}), 401


# # -------- LOGOUT --------
# @auth_routes.route("/logout", methods=["DELETE"])  # <-- switched to DELETE
# @login_required
# def logout():
#     logout_user()
#     return jsonify({"message": "Logged out"}), 200


# # -------- GET CURRENT USER --------
# @auth_routes.route("/", methods=["GET"])
# def get_current_user():
#     if current_user.is_authenticated:
#         return jsonify(current_user.to_dict()), 200
#     return jsonify({"user": None}), 200

# Above worked with AlbumCRUD

from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app import db

auth_routes = Blueprint("auth", __name__, url_prefix="/api/auth")

# -------- LOGIN --------
@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password required"}), 400

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        login_user(user)  # This sets the session cookie
        return jsonify(user.to_dict()), 200

    return jsonify({"message": "Invalid credentials"}), 401


# -------- LOGOUT --------
@auth_routes.route("/logout", methods=["DELETE"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out"}), 200


# -------- GET CURRENT USER (used on page load) --------
@auth_routes.route("/", methods=["GET"])
def get_current_user():
    if current_user.is_authenticated:
        return jsonify(current_user.to_dict()), 200
    return jsonify({"user": None}), 200