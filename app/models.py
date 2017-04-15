from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    pins = db.relationship('Pin', backref='user', lazy='dynamic')

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.email)

class Pin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.Text)

    def __init__(self, name, user_id, description):
        self.name = name
        self.user_id = user_id
        self.description = description
