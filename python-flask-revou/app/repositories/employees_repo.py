from app.models.employees import Employees
from app.utils.database import db

class Employees_repo():
    def list_employees(self):
        employees = Employees.query.all()
        return employees
    
    def get_employees(self, employees_id):
        employees = Employees.query.get(employees_id)
        return employees
    
    def create_employees(self, data):
        db.session.add(data)
        db.session.commit()
        return data
    
    def delete_employees(self, employees_id):
        employees = Employees.query.get(employees_id)

        db.session.delete(employees)
        db.session.commit()
        return employees
    
    def edit_employees(self, employees_id, data):
        employees = Employees.query.get(employees_id)

        employees.name = data["name"]
        employees.phonenumber = data["phonenumber"]
        employees.role = data["role"]
        employees.schedule = data["schedule"]
        employees.email = data["email"]
        
        db.session.commit()
        return employees
    