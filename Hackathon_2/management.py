""" EMPLOYEE MANAGMENT SYSTEM """

import json

class Person:
    """ 
    Represents a person with basic attributes: name, age, and gender.
    """
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_details(self):
        """Returns a string containing the person's details."""
        details = ", ".join(["Name: " + str(self.name),"Age: " + str(self.age),"Gender: " + str(self.gender)])
        return details                       

class Employee(Person):
    """
    Represents an employee, inheriting from Person, with additional attributes such as
    employee ID, department, and salary.
    """
    def __init__(self, name, age, gender, emp_id, department, salary):
        """Initialize an Employee object."""
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = int(salary)

    def get_details(self):
        """Returns a string containing all employee details, including inherited details."""
        return f"{super().get_details()}, ID: {self.emp_id}, Dept: {self.department}, Salary: {self.salary}"

        
    def is_eligible_for_bonus(self):
        """Checks if the employee is eligible for a bonus based on salary criteria."""
        return self.salary < 50000
    
    def from_string(cls, data_string):
        """Creates an Employee object from a comma-separated string."""
        name, age, gender, emp_id, department, salary = data_string.split(',')
        return cls(name, int(age), gender, emp_id, department, int(salary))
    
    from_string = classmethod(from_string) 

    def bonus_policy():
        """Prints the company's bonus policy."""
        print('-'*20, 'COMPANY POLICY', '-'*20)
        print('-'*80)
        print("Employees earning below ₹50,000 are eligible for a bonus.")
        print('-'*80)

    bonus_policy = staticmethod(bonus_policy) 

class Department:
    """
    Represents a department that contains multiple employees.
    """
    def __init__(self, name):
        """Initialize a Department object with a name and an empty employee list."""
        self.name = name
        self.employees = []
    
    def add_employee(self, employee):
        """Adds an Employee object to the department."""
        self.employees.append(employee)
    
    def get_average_salary(self):
        """Calculates and returns the average salary of employees in the department."""
        if not self.employees:
            return 0
        return sum(emp.salary for emp in self.employees) / len(self.employees)
    
    def get_all_employees(self):
        """Returns a list of string representations of all employees in the department."""
        return [emp.get_details() for emp in self.employees]
    
def save_to_json(employees, filename='employees.json'):
    """Saves the list of Employee objects to a JSON file."""
    data = []
    for emp in employees:
        data.append({
            "name": emp.name,
            "age": emp.age,
            "gender": emp.gender,
            "emp_id": emp.emp_id,
            "department": emp.department,
            "salary": emp.salary
        })
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_from_json(filename='employees.json'):
    """Loads employee data from a JSON file and returns a list of Employee objects."""
    with open(filename, 'r') as file:
        data = json.load(file)
    employees = []
    for emp in data:
        employee = Employee(emp['name'], emp['age'], emp['gender'], emp['emp_id'], emp['department'], emp['salary'])
        employees.append(employee)
    return employees
