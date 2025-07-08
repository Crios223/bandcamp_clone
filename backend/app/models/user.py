from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(100), nullable=False)  # Artist/Band name
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    genre = db.Column(db.String(50), nullable=True)
    genre_tags = db.Column(db.String(255), nullable=True)  
    location = db.Column(db.String(100), nullable=True)
    bandcamp_url = db.Column(db.String(100), unique=True)  

    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    albums = db.relationship("Album", back_populates="user", cascade="all, delete-orphan")
    images = db.relationship("Image", back_populates="user", cascade="all, delete-orphan")
    reviews = db.relationship("Review", back_populates="user", cascade="all, delete-orphan")
    cart_items = db.relationship("CartItem", back_populates="user", cascade="all, delete-orphan")
    wishlist_items = db.relationship("WishlistItem", back_populates="user", cascade="all, delete-orphan")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "artist_name": self.artist_name,
            "username": self.username,
            "email": self.email,
            "genre": self.genre,
            "genre_tags": self.genre_tags,
            "location": self.location,
            "bandcamp_url": self.bandcamp_url,
            "date_created": self.date_created.isoformat()
        }

    def __repr__(self):
        return f"<User {self.username}>"