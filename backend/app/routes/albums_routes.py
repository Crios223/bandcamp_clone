from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import Album

albums_bp = Blueprint("albums", __name__, url_prefix="/api/albums")

# GET /api/albums - Get all albums
@albums_bp.route("/", methods=["GET"])
def get_all_albums():
    albums = Album.query.all()
    return jsonify([album.to_dict() for album in albums]), 200

# GET /api/albums/<int:id> - Get album by ID
@albums_bp.route("/<int:id>", methods=["GET"])
def get_album_by_id(id):
    album = Album.query.get(id)
    if not album:
        return jsonify({"message": "Album not found"}), 404
    return jsonify(album.to_dict()), 200

# POST /api/albums - Create album (auth required)
@albums_bp.route("/", methods=["POST"])
@login_required
def create_album():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description", "")

    if not title:
        return jsonify({"errors": {"title": "Title is required"}}), 400

    new_album = Album(title=title, description=description, user_id=current_user.id)
    db.session.add(new_album)
    db.session.commit()

    return jsonify(new_album.to_dict()), 201

# PUT /api/albums/<int:id> - Update album (auth + ownership required)
@albums_bp.route("/<int:id>", methods=["PUT"])
@login_required
def update_album(id):
    album = Album.query.get(id)
    if not album:
        return jsonify({"message": "Album not found"}), 404
    if album.user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 403

    data = request.get_json()
    album.title = data.get("title", album.title)
    album.description = data.get("description", album.description)

    db.session.commit()
    return jsonify(album.to_dict()), 200

# DELETE /api/albums/<int:id> - Delete album (auth + ownership required)
@albums_bp.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_album(id):
    album = Album.query.get(id)
    if not album:
        return jsonify({"message": "Album not found"}), 404
    if album.user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 403

    db.session.delete(album)
    db.session.commit()
    return jsonify({"message": "Album deleted"}), 200