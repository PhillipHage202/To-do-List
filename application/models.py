from application import db

class Todo (db.Model):
    id = db.Column(db.Integer, primary_keys=True)
    task = db.Column(db.String(30), unique=True) 
    complete = db.Column(db.Boolean, default=False)
