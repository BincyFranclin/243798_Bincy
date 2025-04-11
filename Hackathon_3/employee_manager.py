from employee import Employee

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, department, designation, tax, bonus, base_salary):
        employee = Employee(name, department, designation, tax, bonus, base_salary)
        self.employees.append(employee)
        return employee

    def get_all_employees(self):
        return self.employees

    def find_by_id(self, emp_id):
        return next((emp for emp in self.employees if emp.id == emp_id), None)

    def delete_employee(self, emp_id):
        employee = self.find_by_id(emp_id)
        if employee:
            self.employees.remove(employee)
            return True
        return False

    def load_employees(self, employee_dicts):
        self.employees = [Employee.from_dict(data) for data in employee_dicts]

    def to_dict_list(self):
        return [emp.to_dict() for emp in self.employees]
