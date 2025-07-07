# from flask import Blueprint, request, jsonify
# from app import db
# from app.models.review import Review

# review_routes = Blueprint("reviews", __name__)

# # GET all reviews
# @review_routes.route("/")
# def get_reviews():
#     reviews = Review.query.all()
#     return jsonify([r.to_dict() for r in reviews])

# # POST a new review
# @review_routes.route("/", methods=["POST"])
# def create_review():
#     data = request.get_json()
#     review = Review(
#         content=data["content"],
#         rating=data["rating"],
#         user_id=data["user_id"],
#         album_id=data["album_id"]
#     )
#     db.session.add(review)
#     db.session.commit()
#     return review.to_dict(), 201

# # DELETE a review
# @review_routes.route("/<int:id>", methods=["DELETE"])
# def delete_review(id):
#     review = Review.query.get_or_404(id)
#     db.session.delete(review)
#     db.session.commit()
#     return {"message": "Review deleted"}

from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from app import db
from app.models import Review, User

review_routes = Blueprint("reviews", __name__, url_prefix="/api/reviews")


# -------- Get all reviews for an album --------
@review_routes.route("/album/<int:album_id>")
def get_reviews_for_album(album_id):
    reviews = Review.query.filter_by(album_id=album_id).all()
    return jsonify([r.to_dict() for r in reviews])


# -------- Create a review --------
@review_routes.route("", methods=["POST"])  # ✅ correct path, no slash
@login_required
def create_review():
    data = request.get_json()

    # ✅ Use .get() safely
    rating = data.get("rating")
    comment = data.get("comment")
    album_id = data.get("album_id")

    if not rating or not album_id:
        return jsonify({"message": "Missing required fields"}), 400

    review = Review(
        rating=rating,
        comment=comment or "",
        album_id=album_id,
        user_id=current_user.id
    )

    db.session.add(review)
    db.session.commit()
    return jsonify(review.to_dict()), 201


# -------- Update a review --------
@review_routes.route("/<int:id>", methods=["PUT"])
@login_required
def update_review(id):
    review = Review.query.get_or_404(id)
    if review.user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 403

    data = request.get_json()
    review.rating = data.get("rating", review.rating)
    review.comment = data.get("comment", review.comment)

    db.session.commit()
    return jsonify(review.to_dict())


# -------- Delete a review --------
@review_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_review(id):
    review = Review.query.get_or_404(id)
    if review.user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 403

    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": "Review deleted"})