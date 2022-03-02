from app import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True)
    description = db.Column(db.String(1024))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    created = db.Column(db.DateTime)


    def __repr__(self):
        return '<Todo {} id[{}]>'.format(self.title, self.id)