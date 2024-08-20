import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(df):
    results = {}
    
    # Estadísticas descriptivas
    results['summary_stats'] = df.describe()
    
    # Casos totales por estado
    total_cases_by_state = df.groupby('state')['positive'].max().sort_values(ascending=False)
    plt.figure(figsize=(12, 6))
    total_cases_by_state.plot(kind='bar')
    plt.title('Casos totales de COVID-19 por estado')
    plt.xlabel('Estado')
    plt.ylabel('Casos totales')
    plt.tight_layout()
    plt.savefig('../data/total_cases_by_state.png')
    results['total_cases_by_state'] = total_cases_by_state
    
    # Evolución temporal de casos
    daily_cases = df.groupby('date')['positive'].sum()
    plt.figure(figsize=(12, 6))
    daily_cases.plot()
    plt.title('Evolución de casos diarios de COVID-19')
    plt.xlabel('Fecha')
    plt.ylabel('Casos diarios')
    plt.tight_layout()
    plt.savefig('../data/daily_cases_evolution.png')
    results['daily_cases_evolution'] = daily_cases
    
    return results