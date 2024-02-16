from app.models.animals_management import Animal_management
from app.utils.database import db
from flask import jsonify, request
from http.client import CREATED, INTERNAL_SERVER_ERROR, NOT_FOUND, OK

def list_animal():
    try:
        animals = Animal_management.query.all()
        return [animal.as_dict() for animal in animals], OK
    except Exception as e:
        return e, INTERNAL_SERVER_ERROR

def get_animal(animal_id: str):
    try:
        animal_management = Animal_management.query.get(animal_id)

        if animal_management:
            return jsonify({
                "id" : animal_management.id,
                "species" : animal_management.species,
                "age" : animal_management.age,
                "gender" : animal_management.gender,
                "spesial_requirements" : animal_management.spesial_requirements
            }), OK
        return jsonify({'error': 'Animal not Found'}), NOT_FOUND
    except Exception as e:
        return e, INTERNAL_SERVER_ERROR
    
def create_animal():
    try:
        data = request.json
        animal_management = Animal_management()

        if data is not None:
            animal_management.species = data["species"]
            animal_management.age = data["age"]
            animal_management.gender = data["gender"]
            animal_management.spesial_requirements = data["spesial_requirements"]

        db.session.add(animal_management)
        db.session.commit()

        return jsonify('success'), CREATED
    except Exception as e:
        return jsonify({'error': str(e)}), INTERNAL_SERVER_ERROR

def delete_animal(animal_id: str):
    try:
        animal_management = Animal_management.query.get(animal_id)

        if animal_management is None:
            return jsonify({'error': 'Animal not Found'}), NOT_FOUND
        
        db.session.delete(animal_management)
        db.session.commit()

        return jsonify({'message': 'Animal Deleted Succsesfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), INTERNAL_SERVER_ERROR
    
def edit_animal(animal_id: str):
    try: 
        animal_management = Animal_management.query.get(animal_id)

        if animal_management is None:
            return jsonify({'error': 'Animal not found'}), NOT_FOUND
        
        data = request.json
        if data is not None:
             animal_management.species = data["species"]
             animal_management.age = data["age"]
             animal_management.gender = data["gender"]
             animal_management.spesial_requirements = data["spesial_requirements"]

        db.session.commit()

        return jsonify({'message': 'Animal Update Succesfully'}), OK
    except Exception as e:
        return jsonify({'error': str(e)}), INTERNAL_SERVER_ERROR