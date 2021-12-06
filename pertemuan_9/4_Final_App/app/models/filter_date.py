from . import db 

class FilterDate(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    quick_range = db.Column(db.Boolean())
    data = db.Column(db.String(3))
    from_date = db.Column(db.DateTime())
    to_date = db.Column(db.DateTime())