import uuid

class Employee:
    
    # To check whether salary components are not negative
    
    def __init__(self, name, department, designation, tax, bonus, base_salary, emp_id=None):
        if base_salary < 0:
            raise ValueError("Base salary cannot be negative.")
        if tax < 0:
            raise ValueError("Tax cannot be negative.")
        if bonus < 0:
            raise ValueError("Bonus cannot be negative.")

        self.id = emp_id if emp_id else str(uuid.uuid4())
        self.name = name
        self.department = department
        self.designation = designation
        self.tax = tax
        self.bonus = bonus
        self.gross_salary = base_salary + bonus
        self.net_salary = max(self.gross_salary - tax, -self.gross_salary)
        
    # Convert the Employee object to a dictionary representation

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation,
            "gross_salary": self.gross_salary,
            "tax": self.tax,
            "bonus": self.bonus,
            "net_salary": self.net_salary
        }
    # Create an Employee object from a dictionary.
    
    @staticmethod
    def from_dict(data):
        base_salary = data["gross_salary"] - data["bonus"]
        return Employee(
            name=data["name"],
            department=data["department"],
            designation=data["designation"],
            tax=data["tax"],
            bonus=data["bonus"],
            base_salary=base_salary,
            emp_id=data["id"]
        )
