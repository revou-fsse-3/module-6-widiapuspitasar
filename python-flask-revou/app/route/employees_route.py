
from flask import Blueprint
from app.controller.employees_controller import (
    create_employees,
    get_employees,
    list_employees,
    edit_employees,
    delete_employees
)

employees_blueprint = Blueprint('employees_blueprint', __name__)

employees_blueprint.route("/", methods=["GET"])(list_employees) 
employees_blueprint.route("/<string:employees_id>", methods=["GET"])(get_employees) 
employees_blueprint.route("/", methods=["POST"])(create_employees) 
employees_blueprint.route("/<string:employees_id>", methods=["PUT"])(edit_employees) 
employees_blueprint.route("/<string:employees_id>", methods=["DELETE"])(delete_employees) 
