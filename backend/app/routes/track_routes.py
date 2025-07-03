from flask import Blueprint, request, jsonify
from app import db
from app.models.track import Track


track_routes = Blueprint("tracks", __name__)

# GET all tracks
@track_routes.route("/")
def get_tracks():
    tracks = Track.query.all()
    return jsonify([track.to_dict() for track in tracks])

# GET a track by ID
@track_routes.route("/<int:id>")
def get_track(id):
    track = Track.query.get_or_404(id)
    return track.to_dict()

# POST a new track
@track_routes.route("/", methods=["POST"])
def create_track():
    data = request.get_json()
    new_track = Track(
        title=data["title"],
        album_id=data["album_id"],
        duration=data.get("duration")
    )
    db.session.add(new_track)
    db.session.commit()
    return new_track.to_dict(), 201

# DELETE a track
@track_routes.route("/<int:id>", methods=["DELETE"])
def delete_track(id):
    track = Track.query.get_or_404(id)
    db.session.delete(track)
    db.session.commit()
    return {"message": "Track deleted"}