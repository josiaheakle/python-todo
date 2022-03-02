from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin # required fns and properties for flask_login 

from app import db, login

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64), index=True)
    lastName = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __init__(self):
        super().__init__()
        

    def __repr__(self):
        return '<User {}, id[{}]>'.format(self.username, self.id)

@login.user_loader # To show flask_login how to load user from db
def loadUser(id):
    return User.query.get(int(id))