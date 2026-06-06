import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import os

os.makedirs("outputs/plots", exist_ok=True)

def run_visualise(df):

    # 1. India cases over time
    india = df[df["location"] == "India"]
    plt.figure(figsize=(12, 5))
    plt.plot(india["date"], india["total_cases"], color="steelblue")
    plt.title("India - Total COVID Cases Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.tight_layout()
    plt.savefig("outputs/plots/india_cases.png")
    plt.close()
    print("Saved: india_cases.png")

    # 2. India deaths over time
    plt.figure(figsize=(12, 5))
    plt.plot(india["date"], india["total_deaths"], color="crimson")
    plt.title("India - Total Deaths Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Deaths")
    plt.tight_layout()
    plt.savefig("outputs/plots/india_deaths.png")
    plt.close()
    print("Saved: india_deaths.png")

    # 3. Global daily new cases
    global_daily = df.groupby("date")["new_cases"].sum().reset_index()
    plt.figure(figsize=(12, 5))
    plt.plot(global_daily["date"], global_daily["new_cases"], color="darkorange")
    plt.title("Global Daily New Cases Over Time")
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.tight_layout()
    plt.savefig("outputs/plots/global_new_cases.png")
    plt.close()
    print("Saved: global_new_cases.png")

    # 4. Top 10 countries by total cases (bar)
    top_cases = df.groupby("location")["total_cases"].max().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12, 5))
    plt.bar(top_cases.index, top_cases.values, color="steelblue")
    plt.title("Top 10 Countries by Total Cases")
    plt.xlabel("Country")
    plt.ylabel("Total Cases")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("outputs/plots/top10_cases.png")
    plt.close()
    print("Saved: top10_cases.png")

    # 5. Top 10 countries by total deaths (bar)
    top_deaths = df.groupby("location")["total_deaths"].max().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12, 5))
    plt.bar(top_deaths.index, top_deaths.values, color="crimson")
    plt.title("Top 10 Countries by Total Deaths")
    plt.xlabel("Country")
    plt.ylabel("Total Deaths")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("outputs/plots/top10_deaths.png")
    plt.close()
    print("Saved: top10_deaths.png")

    # 6. Top 10 vaccinated countries (horizontal bar)
    top_vax = df.groupby("location")["people_fully_vaccinated_per_hundred"].max().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    plt.barh(top_vax.index, top_vax.values, color="seagreen")
    plt.title("Top 10 Countries - % Fully Vaccinated")
    plt.xlabel("% Fully Vaccinated")
    plt.tight_layout()
    plt.savefig("outputs/plots/top10_vaccinated.png")
    plt.close()
    print("Saved: top10_vaccinated.png")

    # 7. India vaccination timeline
    plt.figure(figsize=(12, 5))
    plt.plot(india["date"], india["people_fully_vaccinated"], color="seagreen")
    plt.title("India - Fully Vaccinated Over Time")
    plt.xlabel("Date")
    plt.ylabel("People Fully Vaccinated")
    plt.tight_layout()
    plt.savefig("outputs/plots/india_vaccination.png")
    plt.close()
    print("Saved: india_vaccination.png")

    print("\nAll plots saved to outputs/plots/")