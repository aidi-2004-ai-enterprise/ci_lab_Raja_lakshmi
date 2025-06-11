import pandas as pd

def load_penguin_data():
    """Load penguin dataset and return DataFrame shape"""
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
    df = pd.read_csv(url)
    return df.shape

if __name__ == "__main__":
    shape = load_penguin_data()
    print(f"Penguin dataset shape: {shape}")
