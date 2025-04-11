import unittest
from employee import Employee 

class TestEmployee(unittest.TestCase):
    
    #Test for creation of  Employee instance with valid values
    def test_create_employee(self):
               
        emp = Employee("Bincy", "IT", "Developer", tax=500, bonus=10000, base_salary=50000)
        self.assertEqual(emp.name, "Bincy")
        self.assertEqual(emp.department, "IT")
        self.assertEqual(emp.designation, "Developer")
        self.assertEqual(emp.tax, 500)
        self.assertEqual(emp.bonus, 10000)
        self.assertEqual(emp.gross_salary, 60000) 
        self.assertEqual(emp.net_salary, 59500)    
        self.assertIsNotNone(emp.id)
    
    #test for dictionary conversion

    def test_dict_conversion(self):
        emp = Employee("Johns", "project owner", "Manager", tax=3000, bonus=5000, base_salary=85000)
        d = emp.to_dict()
        emp2 = Employee.from_dict(d)
        self.assertEqual(emp.id, emp2.id)
        self.assertEqual(emp.name, emp2.name)
        self.assertEqual(emp.department, emp2.department)
        self.assertEqual(emp.designation, emp2.designation)
        self.assertEqual(emp.tax, emp2.tax)
        self.assertEqual(emp.bonus, emp2.bonus)
        self.assertEqual(emp.gross_salary, emp2.gross_salary)
        self.assertEqual(emp.net_salary, emp2.net_salary)
        
    #Test that negative values for tax, bonus, and base_salary raise a ValueError

    def test_negative_values_raise_exception(self):
        with self.assertRaises(ValueError):
            Employee("Invalid", "Dept", "Title", tax=-1, bonus=1000, base_salary=50000)
        with self.assertRaises(ValueError):
            Employee("Invalid", "Dept", "Title", tax=100, bonus=-1000, base_salary=50000)
        with self.assertRaises(ValueError):
            Employee("Invalid", "Dept", "Title", tax=100, bonus=1000, base_salary=-50000)

if __name__ == '__main__':
    unittest.main()
