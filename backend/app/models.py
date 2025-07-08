from app import db
from .user import User
from .album import Album

class User(db.Model):
    __tablename__ = 'users'



    
#                 ---- User Modlel   -----------
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    cover_image = db.Column(db.String(255))  # URL to album cover added 7/1
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationships added 7/1
    user = db.relationship('User', backref=db.backref('albums', lazy=True))

    def __repr__(self):
        return f"<User {self.username}>"