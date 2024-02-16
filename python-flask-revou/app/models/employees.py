from app.utils.database import db

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phonenumber = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(100), nullable=False)
    schedule = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def as_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "phonenumber" : self.phonenumber,
            "role" : self.role,
            "schedule" : self.schedule,
            "email" : self.email
        }