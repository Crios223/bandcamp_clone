from app import db

class CartItem(db.Model):
    __tablename__ = "cart_items"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey("albums.id"), nullable=False)
    quantity = db.Column(db.Integer, default=1, nullable=False)

    user = db.relationship("User", back_populates="cart_items")
    album = db.relationship("Album", back_populates="cart_items")

    def __repr__(self):
        return f"<CartItem User {self.user_id} Album {self.album_id} Qty {self.quantity}>"