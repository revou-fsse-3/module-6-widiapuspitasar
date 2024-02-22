from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.animals_management import Animal_management
from app.utils.api_response import api_response
from app.service.animal_service import Animal_service
from pydantic import ValidationError

animal_blueprint = Blueprint('animal_endpoint', __name__)

@animal_blueprint.route("/", methods=["GET"])
def list_animal():
    try:
        animal_service = Animal_service()

        animal_managements = animal_service.list_animal()

        return api_response(
            status_code=200,
            message="",
            data=animal_managements
        )
    
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )
    
@animal_blueprint.route("/<string:animal_id>", methods=["GET"])
def get_animal(animal_id):
    try:
        animal_service = Animal_management.query.get(animal_id)

        if not animal_service:
            return "Animal not found", 404
        
        return animal_service.as_dict(), 200
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data=animal_service
        )


@animal_blueprint.route("/", methods=["POST"])
def create_animal():
    try:
        data = request.json
        animal_service = Animal_service()

        animal_management = animal_service.create_animal(data)

        return api_response(
            status_code=200,
            message="updated",
            data=animal_management
        )
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={}
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )
    
@animal_blueprint.route("/<string:animal_id>", methods=["PUT"])
def edit_animal(animal_id):
    try: 
        data = request.json
        animal_service = Animal_service()

        animal_management = animal_service.edit_animals(animal_id, data)

        return api_response(
            status_code=200,
            message="updated",
            data=animal_management
        )
    
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={}
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )
    
@animal_blueprint.route("/<string:animal_id>", methods=["DELETE"])
def delete_animal(animal_id): 
    try:
        animal_service = Animal_service()

        animal_management = animal_service.delete_animal(animal_id)
        if animal_management == "Animal not found":
            return api_response(
                status_code=404,
                message=animal_management,
                data="empty"
            )
        return api_response(
            status_code=200,
            message="Deleted",
            data=animal_management
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )

    
