from app.repositories.employees_repo import Employees_repo
from app.models.employees import Employees

class Employees_service:
    def __init__(self):
        self.employees_repo = Employees_repo()
    
    def list_employees(self):
        employees = self.employees_repo.list_employees()
        return [employe.as_dict() for employe in employees]
    
    def get_employees(self, employees_id):
        employees = self.employees_repo.get_employees(employees_id)
        return [employee.as_dict() for employee in employees]
    
    def create_employees(self, data):
        employees = Employees()
        
        employees.name = data["name"]
        employees.phonenumber = data["phonenumber"]
        employees.role = data["role"]
        employees.schedule = data["schedule"]
        employees.email = data["email"]

        created_employees = self.employees_repo.create_employees(employees)
        return created_employees.as_dict()
    
    def edit_employees(self, employees_id, data):
        updated_employees = self.employees_repo.edit_employees(employees_id, data)
        return updated_employees.as_dict()
    
    def delete_employees(self, employees_id):
        employees = Employees.query.get(employees_id)
        if not employees:
            return "Employees not found"

        deleted_employees = self.employees_repo.delete_employees(employees_id)
        return deleted_employees.as_dict()
    
   



