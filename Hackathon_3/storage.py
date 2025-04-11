import pickle
import os

class Storage:
    def __init__(self, filepath="employees.pkl"):
        self.filepath = filepath

    def save(self, employee_dict_list):
        with open(self.filepath, "wb") as f:
            pickle.dump(employee_dict_list, f)

    def load(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, "rb") as f:
            return pickle.load(f)
