# from app import db

# class Album(db.Model):
#     __tablename__ = "albums"

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), nullable=False)
#     description = db.Column(db.Text)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

#     user = db.relationship("User", back_populates="albums")
#     tracks = db.relationship("Track", back_populates="album", cascade="all, delete-orphan")
#     images = db.relationship("Image", back_populates="album", cascade="all, delete-orphan")
#     reviews = db.relationship("Review", back_populates="album", cascade="all, delete-orphan")
#     cart_items = db.relationship("CartItem", back_populates="album", cascade="all, delete-orphan")
#     wishlist_items = db.relationship("WishlistItem", back_populates="album", cascade="all, delete-orphan")  # ✅ ADD THIS LINE

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "title": self.title,
#             "description": self.description,
#             "user_id": self.user_id,
#         }

#     def __repr__(self):
#         return f"<Album {self.title}>"



from app import db

class Album(db.Model):
    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.String(50))  # optional
    price = db.Column(db.Float, default=0.0)  # USD
    cover_url = db.Column(db.String(500))     # optional URL
    artist = db.Column(db.String(255))        # optional custom artist
    description = db.Column(db.Text)          # optional
    credits = db.Column(db.Text)              # optional
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", back_populates="albums")
    tracks = db.relationship("Track", back_populates="album", cascade="all, delete-orphan")
    images = db.relationship("Image", back_populates="album", cascade="all, delete-orphan")
    reviews = db.relationship("Review", back_populates="album", cascade="all, delete-orphan")
    cart_items = db.relationship("CartItem", back_populates="album", cascade="all, delete-orphan")
    wishlist_items = db.relationship("WishlistItem", back_populates="album", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date,
            "price": self.price,
            "cover_url": self.cover_url,
            "artist": self.artist,
            "description": self.description,
            "credits": self.credits,
            "user_id": self.user_id
        }

    def __repr__(self):
        return f"<Album {self.title}>"