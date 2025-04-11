import unittest
from employee_manager import EmployeeManager
from employee import Employee

class TestEmployeeManager(unittest.TestCase):
    def setUp(self):
        self.manager = EmployeeManager()
    
    # Test that employees can be added and retrieved
    
    def test_add_and_get_all_employees(self):
        self.manager.add_employee("Bincy", "IT", "Developer", tax=1500, bonus=15000, base_salary=50000)
        self.manager.add_employee("Aruna", "HR", "Junior HR", tax=3600, bonus=10000, base_salary=33000)
        all_emps = self.manager.get_all_employees()
        self.assertEqual(len(all_emps), 2)
        self.assertEqual(all_emps[0].name, "Bincy")
        self.assertEqual(all_emps[1].name, "Aruna")
        
    #To find employee by ID

    def test_find_by_id(self):
        emp = self.manager.add_employee("Bincy", "IT", "Developer", tax=1500, bonus=15000, base_salary=50000)
        found = self.manager.find_by_id(emp.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Bincy")
        self.assertEqual(found.designation, "Developer")
    
    # To delete an existing employee  detail

    def test_delete_existing_employee(self):
        emp1 = self.manager.add_employee("Aruna", "HR", "Junior HR", tax=3600, bonus=10000, base_salary=33000)
        emp2 = self.manager.add_employee("Hema", "Finance", "Analyst", tax=2000, bonus=8000, base_salary=40000)
        result = self.manager.delete_employee(emp1.id)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.get_all_employees()), 1)
        
    # To delete an employee with  non-existent ID

    def test_delete_nonexistent_employee(self):
        fake_id = "non-existent-id"
        result = self.manager.delete_employee(fake_id)
        self.assertFalse(result)
        
    
    def test_to_dict_list_and_load_employees(self):
        emp = self.manager.add_employee("Arya", "Design", "Artist", tax=800, bonus=5000, base_salary=12000)
        dict_list = self.manager.to_dict_list()
        self.assertEqual(len(dict_list), 1)
        self.assertEqual(dict_list[0]["name"], "Arya")

        new_manager = EmployeeManager()
        new_manager.load_employees(dict_list)
        self.assertEqual(len(new_manager.employees), 1)
        self.assertEqual(new_manager.employees[0].name, "Arya")

    def tearDown(self):
        return None

if __name__ == "__main__":
    unittest.main()
