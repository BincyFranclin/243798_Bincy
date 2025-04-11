import unittest
import os
import pickle
from employee_mgmt.employee import Employee
from employee_mgmt.employee_manager import EmployeeManager


class TestEmployeeManager(unittest.TestCase):

    def setUp(self):
        """Setup a fresh EmployeeManager instance before each test."""
        self.manager = EmployeeManager()
        self.manager.FILE_PATH = "test_employees.pkl"  # Use a test file
        self.manager.employees = []  # Start with a clean slate

    def tearDown(self):
        """Clean up the test file after each test."""
        if os.path.exists(self.manager.FILE_PATH):
            os.remove(self.manager.FILE_PATH)

    def test_add_employee(self):
        """Test adding a new employee."""
        emp = self.manager.add_employee("Alice", "HR", "Manager", tax=2000, bonus=1000, base_salary=50000)
        self.assertEqual(len(self.manager.employees), 1)
        self.assertEqual(emp.name, "Alice")
        self.assertEqual(emp.department, "HR")
        self.assertEqual(emp.gross_salary, 51000)  # 50000 + 1000

    def test_get_all_employees(self):
        """Test retrieving all employees."""
        self.manager.add_employee("Bob", "IT", "Developer", tax=1500, bonus=500, base_salary=60000)
        self.manager.add_employee("Charlie", "Finance", "Analyst", tax=1800, bonus=600, base_salary=56000)
        employees = self.manager.get_all_employees()
        self.assertEqual(len(employees), 2)
        self.assertEqual(employees[0].name, "Bob")
        self.assertEqual(employees[1].name, "Charlie")

    def test_find_by_id(self):
        """Test finding an employee by ID."""
        emp = self.manager.add_employee("David", "Marketing", "Lead", tax=1200, bonus=800, base_salary=45000)
        found_emp = self.manager.find_by_id(emp.id)
        self.assertIsNotNone(found_emp)
        self.assertEqual(found_emp.name, "David")

    def test_delete_employee(self):
        """Test deleting an employee by ID."""
        emp = self.manager.add_employee("Emma", "Sales", "Executive", tax=1300, bonus=500, base_salary=40000)
        result = self.manager.delete_employee(emp.id)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.employees), 0)

    def test_save_and_load_data(self):
        """Test saving and loading employees using pickle."""
        self.manager.add_employee("Frank", "R&D", "Scientist", tax=1600, bonus=700, base_salary=52000)
        self.manager.save_data()

        # Load a new instance to check if data persists
        new_manager = EmployeeManager()
        new_manager.FILE_PATH = "test_employees.pkl"  # Load from test file
        new_manager.load_data()

        self.assertEqual(len(new_manager.employees), 1)
        self.assertEqual(new_manager.employees[0].name, "Frank")


if __name__ == "__main__":
    unittest.main()
