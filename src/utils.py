import json

def save_results(results, filename):
    with open(f'../data/{filename}', 'w') as f:
        json.dump(results, f, indent=4)

def load_results(filename):
    with open(f'../data/{filename}', 'r') as f:
        return json.load(f)