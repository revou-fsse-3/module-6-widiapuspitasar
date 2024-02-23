from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.employees import Employees
from app.utils.api_response import api_response
from app.service.employees_service import Employees_service
from pydantic import ValidationError

employees_blueprint = Blueprint('employees_endpoint', __name__)

@employees_blueprint.route("/", methods=["GET"])
def list_employees():
    try:
        employees_service = Employees_service()

        employees = employees_service.list_employees()

        return api_response(
            status_code=200,
            message="",
            data=employees
        )
    
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )
    
@employees_blueprint.route("/<string:employees_id>", methods=["GET"])
def get_employees(employees_id):
    try:
        employees_service = Employees.query.get(employees_id)

        if not employees_service:
            return "Animal not found", 404
        
        return employees_service.as_dict(), 200
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data=employees_service
        )


@employees_blueprint.route("/", methods=["POST"])
def create_employees():
    try:
        data = request.json
        employees_service = Employees_service()

        employees = employees_service.create_employees(data)

        return api_response(
            status_code=200,
            message="updated",
            data=employees
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
    
@employees_blueprint.route("/<string:employees_id>", methods=["PUT"])
def edit_employees(employees_id):
    try: 
        data = request.json
        employees_service = Employees_service()

        employees = employees_service.edit_employees(employees_id, data)

        return api_response(
            status_code=200,
            message="updated",
            data=employees
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
    
@employees_blueprint.route("/<string:employees_id>", methods=["DELETE"])
def delete_employees(employees_id): 
    try:
        employees_service = Employees_service()

        employees = employees_service.delete_employees(employees_id)
        if employees == "Employees not found":
            return api_response(
                status_code=404,
                message=employees,
                data="empty"
            )
        return api_response(
            status_code=200,
            message="Deleted",
            data=employees
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )

    
