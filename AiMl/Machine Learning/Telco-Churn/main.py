import pandas as pd
import os

##1) create, dir structure, pull info, and make sure no redownloading
data_dir = os.path.join(os.path.dirname(__file__), "data")
csv_path = os.path.join(data_dir, "telco_churn_raw.csv")
source_url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"

def ensure_dirs():
    os.makedirs(data_dir, exist_ok=True)

def load_raw():
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path)
    try:
        df = pd.read_csv(source_url)
    except Exception as e:
        raise RuntimeError("Failed to download dataset: " + str(e))
    df.to_csv(csv_path, index=False)
    return df

if __name__ == "__main__":
    ensure_dirs()
    df = load_raw()
    print("Loaded shape:", df.shape)
    print("Columns:", list(df.columns)[:10], "...")
    print(df.head(3))
    