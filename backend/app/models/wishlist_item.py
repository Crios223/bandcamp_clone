from app import db

class WishlistItem(db.Model):
    __tablename__ = "wishlist_items"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.id"), nullable=False)

    user = db.relationship("User", back_populates="wishlist_items")
    album = db.relationship("Album", back_populates="wishlist_items")

    def __repr__(self):
        return f"<WishlistItem User {self.user_id} Album {self.album_id}>"