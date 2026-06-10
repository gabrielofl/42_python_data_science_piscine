import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Loads a CSV file, prints its shape, and returns the DataFrame."""
    try:
        data = pd.read_csv(path)

        if data.empty:
            print("Error: The file is empty.")
            return None

        shape = data.shape
        print(f"Loading dataset of dimensions {shape}")

        return data

    except FileNotFoundError:
        print(f"Error: The file at '{path}' was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty or has no columns.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
