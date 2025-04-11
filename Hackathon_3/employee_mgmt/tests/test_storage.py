import unittest
import os
from storage import Storage
from employee import Employee

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.filename = "test_employees.pkl"
        self.storage = Storage(self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            
    # Test to save and load employee dictionaries using pickle
    
    def test_save_and_load_employee_dicts(self):
        emp1 = Employee("Bincy", "IT", "Developer", tax=1500, bonus=15000, base_salary=50000)
        emp2 = Employee("Aruna", "HR", "Junior HR", tax=3600, bonus=10000, base_salary=33000)

        emp_dict_list = [emp1.to_dict(), emp2.to_dict()]
        self.storage.save(emp_dict_list)

        loaded_dicts = self.storage.load()

        self.assertEqual(len(loaded_dicts), 2)
        self.assertEqual(loaded_dicts[0]["name"], "Bincy")
        self.assertEqual(loaded_dicts[0]["designation"], "Developer")
        self.assertEqual(loaded_dicts[1]["name"], "Aruna")
        self.assertEqual(loaded_dicts[1]["bonus"], 10000)
    
    # Test that loading from a non-existent file returns an empty list
    
    def test_load_when_file_missing(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        result = self.storage.load()
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
