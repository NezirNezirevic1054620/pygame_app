import json


class JsonController:

    def __init__(self, filename, choice):
        self.filename = filename
        self.choice = choice

    def load_data(self):
        try:
            with open(f"{self.filename}", f"{self.choice}") as file:
                file_data = json.load(file)
                high_score = max(file_data["scores"])
                return high_score
        except FileNotFoundError:
            print(f"{self.filename} not found")

    def write_json(self, score):
        try:
            with open(f"{self.filename}", f"{self.choice}") as file:
                file_data = json.load(file)
                file_data["scores"].append(score // 60)
                file.seek(0)
                json.dump(file_data, file, indent=4)
        except FileNotFoundError:
            print(f"{self.filename} not found")
