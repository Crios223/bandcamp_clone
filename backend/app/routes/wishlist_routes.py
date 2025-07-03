from flask import Blueprint, request, jsonify
from app import db
from app.models import WishlistItem

wishlist_routes = Blueprint("wishlist", __name__, url_prefix="/api/wishlist")

# GET all wishlist items
@wishlist_routes.route("/")
def get_all_wishlist_items():
    items = WishlistItem.query.all()
    return jsonify([item.to_dict() for item in items])

# POST: Add album to wishlist
@wishlist_routes.route("/", methods=["POST"])
def add_to_wishlist():
    data = request.get_json()
    new_item = WishlistItem(
        user_id=data["user_id"],
        album_id=data["album_id"]
    )
    db.session.add(new_item)
    db.session.commit()
    return new_item.to_dict(), 201

# DELETE: Remove album from wishlist
@wishlist_routes.route("/<int:id>", methods=["DELETE"])
def remove_from_wishlist(id):
    item = WishlistItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return {"message": "Removed from wishlist"}