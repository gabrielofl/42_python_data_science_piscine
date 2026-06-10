import sys
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def parse_population_string(val):
    """Converts shorthand text numbers like
    '45M' or '300k' into actual floats."""
    if pd.isna(val):
        return 0.0

    val_str = str(val).strip().upper()

    try:
        if "M" in val_str:
            return float(val_str.replace("M", "")) * 1_000_000
        elif "K" in val_str:
            return float(val_str.replace("K", "")) * 1_000
        return float(val_str)
    except ValueError:
        return 0.0


def aff_pop(path: str):
    data = load(path)

    spain_data = data[data["country"] == "Spain"]
    france_data = data[data["country"] == "France"]

    if spain_data.empty:
        print("Error: 'Spain' not found in the dataset.")
        return
    if france_data.empty:
        print("Error: 'France' not found in the dataset.")
        return

    all_years = pd.to_numeric(data.columns.drop("country"))
    year_mask = all_years <= 2050
    filtered_years = all_years[year_mask]
    string_cols = filtered_years.astype(str).tolist()

    x = filtered_years

    y_spain = spain_data[string_cols].map(
        parse_population_string).values.flatten()
    y_france = france_data[string_cols].map(
        parse_population_string).values.flatten()

    y_spain_m = y_spain / 1_000_000
    y_france_m = y_france / 1_000_000

    plt.figure(figsize=(10, 5))
    plt.plot(x, y_spain_m, label="Spain", color="pink", linewidth=2)
    plt.plot(x, y_france_m, label="France", color="black", linewidth=2)

    plt.xlim(1800, 2050)
    plt.title("Population Comparison (1800 - 2050)")
    plt.xlabel("Year")
    plt.ylabel("Population (Millions)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    try:
        aff_pop("population_total.csv")
    except OSError:
        sys.exit(1)
    except (KeyboardInterrupt, EOFError):
        plt.close("all")
        sys.exit(0)
