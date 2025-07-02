# from app import db
# from flask_login import UserMixin  # Add this

# class User(db.Model, UserMixin):  # Inherit from UserMixin
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(40), nullable=False, unique=True)
#     email = db.Column(db.String(255), nullable=False, unique=True)
#     password = db.Column(db.String(255), nullable=False)

#     albums = db.relationship("Album", back_populates="user", cascade="all, delete-orphan")
#     images = db.relationship("Image", back_populates="user", cascade="all, delete-orphan")
#     reviews = db.relationship("Review", back_populates="user", cascade="all, delete-orphan")
#     cart_items = db.relationship("CartItem", back_populates="user", cascade="all, delete-orphan")
#     wishlist_items = db.relationship("WishlistItem", back_populates="user", cascade="all, delete-orphan")

#     def __repr__(self):
#         return f"<User {self.username}>"

from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)  # will store hashed password

    albums = db.relationship("Album", back_populates="user", cascade="all, delete-orphan")
    images = db.relationship("Image", back_populates="user", cascade="all, delete-orphan")
    reviews = db.relationship("Review", back_populates="user", cascade="all, delete-orphan")
    cart_items = db.relationship("CartItem", back_populates="user", cascade="all, delete-orphan")
    wishlist_items = db.relationship("WishlistItem", back_populates="user", cascade="all, delete-orphan")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User {self.username}>"