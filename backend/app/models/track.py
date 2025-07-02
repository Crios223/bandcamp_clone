from app import db

class Track(db.Model):
    __tablename__ = 'tracks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    duration = db.Column(db.Integer)  # in seconds, optional
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=False)

    album = db.relationship('Album', back_populates='tracks')
    reviews = db.relationship("Review", back_populates="track", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Track {self.title}>"