def run_insights(df):
    print("\n=== KEY INSIGHTS ===")

    top_case = df.groupby("location")["total_cases"].max().idxmax()
    print(f"1. Highest cases: {top_case}")

    top_death = df.groupby("location")["total_deaths"].max().idxmax()
    print(f"2. Highest deaths: {top_death}")

    india = df[df["location"] == "India"]
    peak_date = india.loc[india["new_cases"].idxmax(), "date"]
    print(f"3. India peak new cases date: {peak_date.date()}")

    top_vax = df.groupby("location")["people_fully_vaccinated_per_hundred"].max().idxmax()
    print(f"4. Most vaccinated country: {top_vax}")

    death_rate = df.groupby("location").apply(
        lambda x: x["total_deaths"].max() / x["total_cases"].max() * 100
    ).sort_values(ascending=False).head(3)
    print(f"5. Highest death rates (%):\n{death_rate.round(2)}")