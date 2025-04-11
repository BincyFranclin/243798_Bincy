import pickle
import os
from employee_mgmt.employee import Employee  

class EmployeeManager:
    FILE_PATH = "employees.pkl"  # Stores employee data in pickle format

    def __init__(self):
        """Initialize EmployeeManager and load existing employee data."""
        self.employees = []
        self.load_data()

    def add_employee(self, name, department, designation, tax, bonus, base_salary):
        """Add employee details to the list and save data."""
        employee = Employee(name, department, designation, tax, bonus, base_salary)
        self.employees.append(employee)
        self.save_data()
        return employee

    def get_all_employees(self):
        """Return all employee details."""
        return self.employees

    def find_by_id(self, emp_id):
        """Find an employee by ID."""
        return next((emp for emp in self.employees if emp.id == emp_id), None)

    def delete_employee(self, emp_id):
        """Delete an employee by ID and save the updated data."""
        employee = self.find_by_id(emp_id)
        if employee:
            self.employees.remove(employee)
            self.save_data()
            return True
        return False

    def load_data(self):
        """Load employee data from a file."""
        if os.path.exists(self.FILE_PATH) and os.path.getsize(self.FILE_PATH) > 0:
            with open(self.FILE_PATH, "rb") as file:
                self.employees = [Employee.from_dict(data) for data in pickle.load(file)]
        else:
            self.employees = []

    def save_data(self):
        """Save employee data to a pickle file."""
        with open(self.FILE_PATH, "wb") as file:
            pickle.dump(self.to_dict_list(), file)

    def to_dict_list(self):
        """Convert employee objects to a list of dictionaries for storage."""
        return [emp.to_dict() for emp in self.employees]
