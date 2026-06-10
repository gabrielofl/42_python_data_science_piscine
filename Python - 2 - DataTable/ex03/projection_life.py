import sys
import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def parse_gdp_string(val):
    """Converts '3.5k' into numeric floats."""
    if pd.isna(val):
        return None
    val_str = str(val).strip().upper()
    try:
        if "K" in val_str:
            return float(val_str.replace("K", "")) * 1_000
        elif "M" in val_str:
            return float(val_str.replace("M", "")) * 1_000_000
        return float(val_str)
    except ValueError:
        return None


def projection_life():
    """Creates projection life vs GDP in 1900 graphs."""
    data_life = load("life_expectancy_years.csv")
    data_gdp = load("income_per_person_gdppercapita.csv")

    if "1900" not in data_life.columns or "1900" not in data_gdp.columns:
        print("Error: Year '1900' column not found in one or both files.")
        return

    life_1900 = data_life[["country", "1900"]]\
        .rename(columns={"1900": "Life Expectancy"})
    gdp_1900 = data_gdp[["country", "1900"]]\
        .rename(columns={"1900": "GDP"})

    gdp_1900["GDP"] = gdp_1900["GDP"].apply(parse_gdp_string)
    life_1900["Life Expectancy"] = pd\
        .to_numeric(life_1900["Life Expectancy"], errors="coerce")

    merged_data = pd.merge(life_1900, gdp_1900, on="country").dropna()

    if merged_data.empty:
        print("Error: No overlapping country data found for the year 1900.")
        return
    x = merged_data["GDP"]
    y = merged_data["Life Expectancy"]

    plt.figure(figsize=(10, 6))

    plt.scatter(x, y, color="cyan", alpha=0.7,
                edgecolors="black", label="Countries in 1900")

    plt.title("Life Expectancy vs GDP Per Capita (Year 1900)")
    plt.xlabel("Gross Domestic Product Per Capita (PPP, Inflation Adjusted)")
    plt.ylabel("Life Expectancy (Years)")

    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend(loc="lower right")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        projection_life()
    except OSError:
        sys.exit(1)
    except (KeyboardInterrupt, EOFError):
        plt.close("all")
        sys.exit(0)
