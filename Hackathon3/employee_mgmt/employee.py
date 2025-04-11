import pickle
import uuid

class Employee:
    def __init__(self, name, department, designation, tax, bonus, base_salary, emp_id=None):
        """Initialize an Employee with input validation."""
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
        self.gross_salary = self.calculate_gross_salary(base_salary)
        self.net_salary = self.calculate_net_salary()

    def calculate_gross_salary(self, base_salary):
        """Calculate the gross salary."""
        return base_salary + self.bonus

    def calculate_net_salary(self):
        """Calculate net salary, ensuring it does not go below -gross_salary."""
        return max(self.gross_salary - self.tax, -self.gross_salary)

    def to_dict(self):
        """Convert Employee object to dictionary."""
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

    @staticmethod
    def from_dict(data):
        """Create an Employee object from a dictionary."""
        return Employee(
            name=data["name"],
            department=data["department"],
            designation=data["designation"],
            tax=data["tax"],
            bonus=data["bonus"],
            base_salary=data["gross_salary"] - data["bonus"],
            emp_id=data["id"]
        )

    def save_to_file(self, file_path):
        """Save Employee object to a file using pickle."""
        with open(file_path, "wb") as file:
            pickle.dump(self.to_dict(), file)

    @classmethod
    def load_from_file(cls, file_path):
        """Load an Employee object from a pickle file."""
        with open(file_path, "rb") as file:
            data = pickle.load(file)
            return cls.from_dict(data)
