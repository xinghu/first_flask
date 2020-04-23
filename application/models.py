from application.extension import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    gender = db.Column(db.Integer, default=0)

    def __init__(self, username, gender, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.gender = gender


    def __repr__(self):
        return '<User %r>' % self.username
