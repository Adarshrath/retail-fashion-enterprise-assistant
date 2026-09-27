
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"/"processed"/"zara_cleaned.csv"
def load_data():
    return pd.read_csv(DATA,parse_dates=["scraped_at"])
