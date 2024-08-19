import requests
import os
import json

class CovidDataLoader:
    API_URL = "https://api.covidtracking.com/v1/states/daily.json"
    
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def fetch_data(self):
        response = requests.get(self.API_URL)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            response.raise_for_status()
    
    def save_data(self, data, filename="covid_data.json"):
        file_path = os.path.join(self.data_dir, filename)
        with open(file_path, 'w') as file:
            json.dump(data, file)
        print(f"Data saved to {file_path}")
    
    def load_data(self, filename="covid_data.json"):
        file_path = os.path.join(self.data_dir, filename)
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

if __name__ == "__main__":
    loader = CovidDataLoader()
    covid_data = loader.fetch_data()
    loader.save_data(covid_data)
