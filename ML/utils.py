import pandas as pd
from datetime import datetime

def csv_json(file_path):
    df = pd.read_csv(file_path, sep=';')
    n = str(datetime.now())
    df.to_json(f"./data/{n}.json")