import json
import os

class Json_controller():
    def __init__(self, path):
        self.path = path

    def load_data(self):
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                return json.load(f)
        else:
            return {}
    
    def save_data(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)