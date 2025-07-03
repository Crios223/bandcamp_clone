from flask import Blueprint, request, jsonify
from app import db
from app.models import CartItem

cart_routes = Blueprint("cart", __name__, url_prefix="/api/cart")

# GET all cart items
@cart_routes.route("/")
def get_cart_items():
    items = CartItem.query.all()
    return jsonify([item.to_dict() for item in items])

# POST: Add album to cart
@cart_routes.route("/", methods=["POST"])
def add_to_cart():
    data = request.get_json()
    new_item = CartItem(
        user_id=data["user_id"],
        album_id=data["album_id"]
    )
    db.session.add(new_item)
    db.session.commit()
    return new_item.to_dict(), 201

# DELETE: Remove album from cart
@cart_routes.route("/<int:id>", methods=["DELETE"])
def remove_from_cart(id):
    item = CartItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return {"message": "Removed from cart"}