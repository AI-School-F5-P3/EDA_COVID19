import requests
import pandas as pd

def load_covid_data():
    url = "https://api.covidtracking.com/v1/states/daily.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
        return df
    else:
        raise Exception(f"Error al cargar datos: {response.status_code}")