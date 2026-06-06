import pandas as pd

def run_eda(df):
    print("=== BASIC INFO ===")
    print("Shape:", df.shape)
    print("\nColumns:", list(df.columns))
    
    print("\n=== NULL VALUES (top 10 cols) ===")
    print(df.isnull().sum().sort_values(ascending=False).head(10))
    
    print("\n=== TOP 10 COUNTRIES BY TOTAL CASES ===")
    latest = df.groupby("location")["total_cases"].max().sort_values(ascending=False).head(10)
    print(latest)
    
    print("\n=== TOP 10 COUNTRIES BY TOTAL DEATHS ===")
    latest_deaths = df.groupby("location")["total_deaths"].max().sort_values(ascending=False).head(10)
    print(latest_deaths)
    
    print("\n=== INDIA STATS ===")
    india = df[df["location"] == "India"]
    print("Total rows for India:", len(india))
    print("Max cases:", india["total_cases"].max())
    print("Max deaths:", india["total_deaths"].max())