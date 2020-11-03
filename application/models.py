from application import db

class Todo (db.Model):
    id = db.Column(db.Integer, primary_keys=True)
    To_do = db.Column(db.String(30), unique=True) 
    finished = db.Column(db.Boolean, default=False)
