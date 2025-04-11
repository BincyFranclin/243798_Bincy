import unittest
import uuid
from employee_mgmt.employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        """Setup an Employee instance before each test."""
        self.employee = Employee("Alice", "HR", "Manager", tax=2000, bonus=1000, base_salary=50000)

    def test_employee_creation(self):
        """Test if the Employee instance is created correctly."""
        self.assertIsNotNone(self.employee.id)
        self.assertEqual(self.employee.name, "Alice")
        self.assertEqual(self.employee.department, "HR")
        self.assertEqual(self.employee.designation, "Manager")
        self.assertEqual(self.employee.tax, 2000)
        self.assertEqual(self.employee.bonus, 1000)
        self.assertEqual(self.employee.gross_salary, 51000)  # 50000 + 1000
        self.assertEqual(self.employee.net_salary, 49000)  # 51000 - 2000

    def test_employee_custom_id(self):
        """Test if the Employee instance is assigned a custom ID when provided."""
        custom_id = str(uuid.uuid4())
        emp = Employee("Bob", "IT", "Developer", tax=1500, bonus=800, base_salary=60000, emp_id=custom_id)
        self.assertEqual(emp.id, custom_id)

    def test_calculate_gross_salary(self):
        """Test if gross salary calculation is correct."""
        self.assertEqual(self.employee.calculate_gross_salary(50000), 51000)

    def test_calculate_net_salary(self):
        """Test if net salary calculation is correct."""
        self.assertEqual(self.employee.calculate_net_salary(), 49000)

    def test_to_dict(self):
        """Test if Employee is correctly converted to a dictionary."""
        emp_dict = self.employee.to_dict()
        self.assertEqual(emp_dict["id"], self.employee.id)
        self.assertEqual(emp_dict["name"], "Alice")
        self.assertEqual(emp_dict["gross_salary"], 51000)
        self.assertEqual(emp_dict["net_salary"], 49000)

    def test_from_dict(self):
        """Test if Employee is correctly created from a dictionary."""
        data = {
            "id": str(uuid.uuid4()),
            "name": "Charlie",
            "department": "Finance",
            "designation": "Analyst",
            "gross_salary": 56000,
            "tax": 1800,
            "bonus": 600,
            "net_salary": 54200
        }
        emp = Employee.from_dict(data)
        self.assertEqual(emp.id, data["id"])
        self.assertEqual(emp.name, "Charlie")
        self.assertEqual(emp.department, "Finance")
        self.assertEqual(emp.designation, "Analyst")
        self.assertEqual(emp.gross_salary, 56000)
        self.assertEqual(emp.net_salary, 54200)

    def test_negative_base_salary(self):
        """Test edge case where base salary is negative."""
        with self.assertRaises(ValueError):
            Employee("Derek", "Marketing", "Lead", tax=1000, bonus=500, base_salary=-45000)

    def test_negative_tax_or_bonus(self):
        """Test edge cases where tax or bonus is negative."""
        with self.assertRaises(ValueError):
            Employee("Eve", "Sales", "Executive", tax=-1000, bonus=500, base_salary=50000)

        with self.assertRaises(ValueError):
            Employee("Eve", "Sales", "Executive", tax=1000, bonus=-500, base_salary=50000)


if __name__ == "__main__":
    unittest.main()
