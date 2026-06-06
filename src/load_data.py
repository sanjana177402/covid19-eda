import pandas as pd

def load_data():
    df = pd.read_csv("data/covid-data.csv")
    df = df[df["continent"].notna()]
    df["date"] = pd.to_datetime(df["date"])
    return df