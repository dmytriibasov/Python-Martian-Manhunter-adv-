import os
import json


class FileHandler:

    def __init__(self, filename):
        self.json_file = filename

        if os.path.isfile(f'./{self.json_file}'):
            self._create()

    def _create(self):
        with open(self.json_file, 'w') as file:
            pass

    def update(self, data, **kwargs):
        with open(self.json_file, 'w') as file:
            json.dump(data, file)

    def delete(self):
        if os.path.exists(f'./{self.json_file}'):
            os.remove(self.json_file)
        else:
            print("The file does not exist")

    @property
    def data(self):
        with open(self.json_file) as file:
            data = json.load(file)
            return data
