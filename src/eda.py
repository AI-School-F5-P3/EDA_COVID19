import pandas as pd
from data_loader import CovidDataLoader

class CovidEDA:
    
    def __init__(self, data):
        self.df = pd.DataFrame(data)
    
    def basic_statistics(self):
        return self.df.describe()
    
    def missing_values_summary(self):
        return self.df.isnull().sum()
    
    def plot_trends(self, state):
        state_data = self.df[self.df['state'] == state]
        state_data.plot(x='date', y=['positive', 'death'], title=f'COVID-19 Trends in {state}')
    
if __name__ == "__main__":
    loader = CovidDataLoader()
    covid_data = loader.load_data()
    
    eda = CovidEDA(covid_data)
    print(eda.basic_statistics())
    print(eda.missing_values_summary())
    eda.plot_trends('NY')
