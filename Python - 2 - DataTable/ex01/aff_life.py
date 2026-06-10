from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd
import sys


def aff_life(path: str):
    data = load(path)
    spain_data = data[data["country"] == "Spain"]
    if spain_data.empty:
        print("Error: 'Spain' not found in the dataset.")
        return
    years_df = spain_data.drop(columns=["country"])
    x = pd.to_numeric(years_df.columns)

    y = spain_data.drop(columns=["country"]).values.flatten()

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label="Spain", color="pink", linewidth=2)
    plt.title("Life Expectancy in Spain (1800 - 2100)")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy (Years)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    try:
        aff_life("life_expectancy_years.csv")
    except OSError:
        sys.exit(1)
    except (KeyboardInterrupt, EOFError):
        plt.close("all")
        sys.exit(0)
