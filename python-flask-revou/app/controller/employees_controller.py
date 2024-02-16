from app.models.employees import Employees
from app.utils.database import db
from flask import jsonify, request
from http.client import CREATED, INTERNAL_SERVER_ERROR, NOT_FOUND, OK

def list_employees():
    try:
        employees = Employees.query.all()
        return [employee.as_dict() for employee in employees], OK
    except Exception as e:
        return e, INTERNAL_SERVER_ERROR
    
def get_employees(employees_id: str):
    try:
        employees = Employees.query.get(employees_id)

        if employees:
            return jsonify({
                "id" : employees.id,
                "name" : employees.name,
                "phonenumber" : employees.phonenumber,
                "role" : employees.role,
                "schedule" : employees.schedule
            }), OK
        return jsonify({'error': 'Employees Not Found'}), NOT_FOUND
    except Exception as e:
        return e, INTERNAL_SERVER_ERROR
    
def create_employees():
    try:
        data = request.json
        employees = Employees()

        if data is not None:
            employees.name = data["name"]
            employees.phonenumber = data["phonenumber"]
            employees.role = data["role"]
            employees.schedule = data["schedule"]
        
        db.session.add(employees)
        db.session.commit()

        return jsonify('Success'), CREATED
    except Exception as e:
        return jsonify({'error': str(e)}), INTERNAL_SERVER_ERROR
    
def delete_employees(employees_id: str):
    try:
        employees = Employees.query.get(employees_id)

        if employees is None:
            return jsonify({'error': 'Employees Deleted Succesfully'})

        db.session.delete(employees)
        db.session.commit()
        
        return jsonify({'message': 'Employees Deleted Succesfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), INTERNAL_SERVER_ERROR

def edit_employees(employees_id: str):
    try:
        employees = Employees.query.get(employees_id)

        if employees is None:
            return jsonify({'error': 'Employees Not Found'}), NOT_FOUND
        
        data = request.json
        if data is not None:
            employees.name = data["name"]
            employees.phonenumber = data["phonenumber"]
            employees.role = data["role"]
            employees.schedule = data["schedule"]
        
        db.session.commit()

        return jsonify({'message': 'Animal Update Succesfully'}), OK
    except Exception as e:
        return jsonify({'error': str(e)}), INTERNAL_SERVER_ERROR

