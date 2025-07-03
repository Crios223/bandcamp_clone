from flask import Blueprint, request, jsonify
from app import db
from app.models.image import Image

image_routes = Blueprint("images", __name__)

# GET all images
@image_routes.route("/")
def get_images():
    images = Image.query.all()
    return jsonify([img.to_dict() for img in images])

# POST a new image
@image_routes.route("/", methods=["POST"])
def create_image():
    data = request.get_json()
    image = Image(
        url=data["url"],
        user_id=data.get("user_id"),
        album_id=data.get("album_id"),
        track_id=data.get("track_id")
    )
    db.session.add(image)
    db.session.commit()
    return image.to_dict(), 201

# DELETE an image
@image_routes.route("/<int:id>", methods=["DELETE"])
def delete_image(id):
    image = Image.query.get_or_404(id)
    db.session.delete(image)
    db.session.commit()
    return {"message": "Image deleted"}