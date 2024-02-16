from app.utils.database import db

class Animal_management(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    spesial_requirements = db.Column(db.String(100), nullable=True)

    def as_dict(self):
        return {
            "id" : self.id,
            "species" : self.species,
            "age" : self.age,
            "gender" : self.gender,
            "spesial_requirements" : self.spesial_requirements
        }

