from app import db
from datetime import datetime

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True)
    description = db.Column(db.String(1024))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    createdDate = db.Column(db.DateTime, default=datetime.utcnow)
    dueDate = db.Column(db.DateTime)
    completedDate = db.Column(db.DateTime)
    completed = db.Column(db.Boolean)

    def toggle(self):
        self.completed = not self.completed

    def __repr__(self):
        return '<Todo {} id[{}]>'.format(self.title, self.id)