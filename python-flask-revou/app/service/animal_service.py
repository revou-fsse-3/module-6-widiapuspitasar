from app.repositories.animal_repo import Animal_repo
from app.models.animals_management import Animal_management

class Animal_service:
    def __init__(self):
        self.animal_repo = Animal_repo()
    
    def list_animal(self):
        animal_managements = self.animal_repo.list_animal()
        return [animal_management.as_dict() for animal_management in animal_managements]
    
    def get_animal(self, animal_id):
        animal_managements = self.animal_repo.get_animal(animal_id)
        return [animal_management.as_dict() for animal_management in animal_managements]
    
    def create_animal(self, data):
        animal_management = Animal_management()
        
        animal_management.species = data["species"]
        animal_management.age = data["age"]
        animal_management.gender = data["gender"]
        animal_management.spesial_requirements = data["spesial_requirements"]

        created_animal = self.animal_repo.create_animal(animal_management)
        return created_animal.as_dict()
    
    def edit_animals(self, animal_id, data):
        updated_animal = self.animal_repo.edit_animal(animal_id, data)
        return updated_animal.as_dict()
    
    def delete_animal(self, animal_id):
        animal_management = Animal_management.query.get(animal_id)
        if not animal_management:
            return "Animal not found"

        deleted_animal = self.animal_repo.delete_animal(animal_id)
        return deleted_animal.as_dict()
    
   



