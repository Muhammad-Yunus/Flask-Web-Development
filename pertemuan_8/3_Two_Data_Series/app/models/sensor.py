from . import db 

class Sensor(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80))
    device_no = db.Column(db.String(80))
    device_type = db.Column(db.String(80))
    time = db.Column(db.DateTime())
    value = db.Column(db.Float(2))