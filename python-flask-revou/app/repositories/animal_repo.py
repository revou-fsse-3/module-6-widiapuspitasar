from app.models.animals_management import Animal_management
from app.utils.database import db

class Animal_repo():
    def list_animal(self):
        animal_management = Animal_management.query.all()
        return animal_management
    
    def get_animal(self, animal_id):
        animal_management = Animal_management.query.get(animal_id)
        return animal_management
    
    def create_animal(self, data):
        db.session.add(data)
        db.session.commit()
        return data
    
    def delete_animal(self, animal_id):
        animal_management = Animal_management.query.get(animal_id)

        db.session.delete(animal_management)
        db.session.commit()
        return animal_management
    
    def edit_animal(self, animal_id, data):
        animal_management = Animal_management.query.get(animal_id)

        animal_management.species = data["species"]
        animal_management.age = data["age"]
        animal_management.gender = data["gender"]
        animal_management.spesial_requirements = data["spesial_requirements"]

        db.session.commit()
        return animal_management

    
  
    
