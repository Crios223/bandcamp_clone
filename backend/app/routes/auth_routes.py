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
#         login_user(user)  # This sets the session cookie
#         return jsonify(user.to_dict()), 200

#     return jsonify({"message": "Invalid credentials"}), 401


# # -------- LOGOUT --------
# @auth_routes.route("/logout", methods=["DELETE"])
# @login_required
# def logout():
#     logout_user()
#     return jsonify({"message": "Logged out"}), 200


# # -------- GET CURRENT USER (used on page load) --------
# @auth_routes.route("/", methods=["GET"])
# def get_current_user():
#     if current_user.is_authenticated:
#         return jsonify(current_user.to_dict()), 200
#     return jsonify({"user": None}), 200



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
#         login_user(user)  # This sets the session cookie
#         return jsonify(user.to_dict()), 200

#     return jsonify({"message": "Invalid credentials"}), 401


# # -------- SIGNUP --------
# @auth_routes.route("/signup", methods=["POST"])
# def signup():
#     data = request.get_json()

#     if data["email"] != data["confirmEmail"]:
#         return jsonify({"message": "Emails do not match"}), 400

#     existing_email = User.query.filter_by(email=data["email"]).first()
#     existing_username = User.query.filter_by(username=data["username"]).first()

#     if existing_email:
#         return jsonify({"message": "Email already exists"}), 400
#     if existing_username:
#         return jsonify({"message": "Username already exists"}), 400

#     user = User(
#         artist_name=data["artist_name"],
#         username=data["username"],
#         email=data["email"],
#         genre=data.get("genre"),
#         genre_tags=data.get("genre_tags"),
#         location=data.get("location"),
#         bandcamp_url=f"{data['bandcamp_url']}.bandcamp.com"
#     )
#     user.set_password(data["password"])

#     db.session.add(user)
#     db.session.commit()
#     login_user(user)

#     return jsonify(user.to_dict()), 201


# # -------- LOGOUT --------
# @auth_routes.route("/logout", methods=["DELETE"])
# @login_required
# def logout():
#     logout_user()
#     return jsonify({"message": "Logged out"}), 200


# # -------- GET CURRENT USER (used on page load) --------
# @auth_routes.route("/", methods=["GET"])
# def get_current_user():
#     if current_user.is_authenticated:
#         return jsonify(current_user.to_dict()), 200
#     return jsonify({"user": None}), 200



# from flask import Blueprint, request, jsonify, session
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


# # -------- SIGNUP --------
# @auth_routes.route("/signup", methods=["POST"])
# def signup():
#     data = request.get_json()

#     if data["email"] != data["confirmEmail"]:
#         return jsonify({"message": "Emails do not match"}), 400

#     existing_email = User.query.filter_by(email=data["email"]).first()
#     existing_username = User.query.filter_by(username=data["username"]).first()

#     if existing_email:
#         return jsonify({"message": "Email already exists"}), 400
#     if existing_username:
#         return jsonify({"message": "Username already exists"}), 400

#     user = User(
#         artist_name=data["artist_name"],
#         username=data["username"],
#         email=data["email"],
#         genre=data.get("genre"),
#         genre_tags=data.get("genre_tags"),
#         location=data.get("location"),
#         bandcamp_url=f"{data['bandcamp_url']}.bandcamp.com"
#     )
#     user.set_password(data["password"])

#     db.session.add(user)
#     db.session.commit()
#     login_user(user)

#     return jsonify(user.to_dict()), 201


# # -------- LOGOUT --------
# # @auth_routes.route("/logout", methods=["DELETE"])
# # @login_required
# # def logout():
# #     logout_user()
# #     session.clear()  # ✅ this clears the session cookie
# #     return jsonify({"message": "Logged out"}), 200


# # -------- LOGOUT --------
# @auth_routes.route("/logout", methods=["DELETE"])
# def logout():
#     logout_user()
#     session.clear()  # clear session cookie explicitly
#     return jsonify({"message": "Logged out"}), 200


# # -------- GET CURRENT USER (used on page load) --------
# @auth_routes.route("/", methods=["GET"])
# def get_current_user():
#     if current_user.is_authenticated:
#         return jsonify(current_user.to_dict()), 200
#     return jsonify({"user": None}), 200



# from flask import Blueprint, request, jsonify, session
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


# # -------- SIGNUP --------
# @auth_routes.route("/signup", methods=["POST"])
# def signup():
#     data = request.get_json()

#     confirm_email = data.get("confirmEmail")
#     if not confirm_email:
#         return jsonify({"message": "Missing confirmEmail field"}), 400

#     if data["email"] != confirm_email:
#         return jsonify({"message": "Emails do not match"}), 400

#     existing_email = User.query.filter_by(email=data["email"]).first()
#     existing_username = User.query.filter_by(username=data["username"]).first()

#     if existing_email:
#         return jsonify({"message": "Email already exists"}), 400
#     if existing_username:
#         return jsonify({"message": "Username already exists"}), 400

#     user = User(
#         artist_name=data["artist_name"],
#         username=data["username"],
#         email=data["email"],
#         genre=data.get("genre"),
#         genre_tags=data.get("genre_tags"),
#         location=data.get("location"),
#         bandcamp_url=f"{data['bandcamp_url']}.bandcamp.com"
#     )
#     user.set_password(data["password"])

#     db.session.add(user)
#     db.session.commit()
#     login_user(user)

#     return jsonify(user.to_dict()), 201


# # -------- LOGOUT --------
# @auth_routes.route("/logout", methods=["DELETE"])
# def logout():
#     logout_user()
#     session.clear()  # clear session cookie explicitly
#     return jsonify({"message": "Logged out"}), 200


# # -------- GET CURRENT USER (used on page load) --------
# @auth_routes.route("/", methods=["GET"])
# def get_current_user():
#     if current_user.is_authenticated:
#         return jsonify(current_user.to_dict()), 200
#     return jsonify({"user": None}), 200




from flask import Blueprint, request, jsonify, session
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
        login_user(user)
        return jsonify(user.to_dict()), 200

    return jsonify({"message": "Invalid credentials"}), 401

# -------- SIGNUP --------
@auth_routes.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()

    existing_email = User.query.filter_by(email=data["email"]).first()
    existing_username = User.query.filter_by(username=data["username"]).first()

    if existing_email:
        return jsonify({"message": "Email already exists"}), 400
    if existing_username:
        return jsonify({"message": "Username already exists"}), 400

    user = User(
        artist_name=data["artist_name"],
        username=data["username"],
        email=data["email"],
        genre=data.get("genre"),
        genre_tags=data.get("genre_tags"),
        location=data.get("location"),
        bandcamp_url=f"{data['bandcamp_url']}.bandcamp.com"
    )
    user.set_password(data["password"])

    db.session.add(user)
    db.session.commit()
    login_user(user)

    return jsonify(user.to_dict()), 201

# -------- LOGOUT --------
@auth_routes.route("/logout", methods=["DELETE"])
def logout():
    logout_user()
    session.clear()
    return jsonify({"message": "Logged out"}), 200

# -------- GET CURRENT USER --------
@auth_routes.route("/", methods=["GET"])
def get_current_user():
    if current_user.is_authenticated:
        return jsonify(current_user.to_dict()), 200
    return jsonify({"user": None}), 200