from flask import Blueprint, jsonify

animals_blueprint = Blueprint('animals_endpoint', __name__)

animals = [
    {
        
        "name" : "momo",
        "species" : "cat",
        "gender" : "femalex",
        "age" : 3,
        "spesial_requirement" : "healthy"
    },
    {
        "name" : "bocil",
        "species" : "cat",
        "gender" : "female",
        "age" : 3,
        "spesial_requirement" : "healthy"
    }
]

@animals_blueprint.route("/", methods=["GET"])
def get_animal():
    return jsonify(animals)

@animals_blueprint.route("/", methods=["POST"])
def create_animal():
    return "get animals"

@animals_blueprint.route("/<int:animals_id>", methods=["PUT"])
def update_animal(animals_id):
    return str(animals_id)

@animals_blueprint.route("/<int:animals_id>", methods=["DELETE"])
def delete_animal(animals_id):
    return str(animals_id)