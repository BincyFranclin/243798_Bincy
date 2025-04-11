import unittest
import os
import pickle
from employee_mgmt.storage import Storage

class TestStorage(unittest.TestCase):
    def setUp(self):
        """Set up a test file before each test."""
        self.test_file = "test_employees.pkl"
        self.storage = Storage(self.test_file)

    def test_save_and_load(self):
        """Test saving and loading employee data."""
        data = [{"id": "1", "name": "John Doe", "department": "HR", "designation": "Manager"}]
        self.storage.save(data)
        loaded = self.storage.load()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["name"], "John Doe")

    def tearDown(self):
        """Clean up test file after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == "__main__":
    unittest.main()
