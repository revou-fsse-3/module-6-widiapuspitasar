
from flask import Blueprint
from app.controller.animal_controller import (
    create_animal,
    get_animal, 
    list_animal,
    edit_animal,
    delete_animal
)

animal_blueprint = Blueprint('animal_blueprint', __name__)

animal_blueprint.route("/", methods=["GET"])(list_animal) 
animal_blueprint.route("/<string:animal_id>", methods=["GET"])(get_animal) 
animal_blueprint.route("/", methods=["POST"])(create_animal) 
animal_blueprint.route("/<string:animal_id>", methods=["PUT"])(edit_animal) 
animal_blueprint.route("/<string:animal_id>", methods=["DELETE"])(delete_animal) 