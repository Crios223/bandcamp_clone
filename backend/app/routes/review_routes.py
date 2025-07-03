from flask import Blueprint, request, jsonify
from app import db
from app.models.review import Review

review_routes = Blueprint("reviews", __name__)

# GET all reviews
@review_routes.route("/")
def get_reviews():
    reviews = Review.query.all()
    return jsonify([r.to_dict() for r in reviews])

# POST a new review
@review_routes.route("/", methods=["POST"])
def create_review():
    data = request.get_json()
    review = Review(
        content=data["content"],
        rating=data["rating"],
        user_id=data["user_id"],
        album_id=data["album_id"]
    )
    db.session.add(review)
    db.session.commit()
    return review.to_dict(), 201

# DELETE a review
@review_routes.route("/<int:id>", methods=["DELETE"])
def delete_review(id):
    review = Review.query.get_or_404(id)
    db.session.delete(review)
    db.session.commit()
    return {"message": "Review deleted"}