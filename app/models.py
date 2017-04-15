from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    pins = db.relationship('Pin', back_populates='user')

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.email)

class Pin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.Text)
    lat = db.Column(db.Float(Precision=9))
    lng = db.Column(db.Float(Precision=9))
    user = db.relationship('User', back_populates='pins')

    def __init__(self, name, user_id, lat, lng, description):
        self.name = name
        self.user_id = user_id
        self.lat = lat
        self.lng = lng
        self.description = description
