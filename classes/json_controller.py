import json


class JsonController:
    def __init__(self, filename, choice):
        self.filename = filename
        self.choice = choice

    def load_data(self):
        try:
            with open(f"{self.filename}", f"{self.choice}") as file:
                data = json.load(file)
                print(data)
        except FileNotFoundError:
            print(f"{self.filename} not found")

    def write_data(self, score):
        try:
            with open(f"{self.filename}", f"{self.choice}") as file:
                data = file.write(str(score // 60))
                print(data)
        except FileNotFoundError:
            print(f"{self.filename} not found")
