from app import db
from datetime import datetime

class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.id"), nullable=False)
    track_id = db.Column(db.Integer, db.ForeignKey("tracks.id"), nullable=True)  # new column, optional

    rating = db.Column(db.Integer, nullable=False)  # 1 to 5 stars
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    user = db.relationship("User", back_populates="reviews")
    album = db.relationship("Album", back_populates="reviews")
    track = db.relationship("Track", back_populates="reviews")  # new relationship

    def __repr__(self):
        return f"<Review {self.id} - User {self.user_id} Album {self.album_id} Track {self.track_id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "album_id": self.album_id,
            "track_id": self.track_id,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "user": {
                "id": self.user.id,
                "username": self.user.username
            } if self.user else None
        }