from app import db

class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)

    album = db.relationship('Album', back_populates='images')
    user = db.relationship('User', back_populates='images')
    

    def __repr__(self):
        return f"<Image {self.url}>"
