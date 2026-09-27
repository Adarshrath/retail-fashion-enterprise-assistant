from src.data_utils import load_data
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

df = load_data().dropna(subset=["sales_volume"])

train, test = train_test_split(
    df,
    test_size=0.2,
    random_state=42
)

baseline_prediction = np.repeat(
    train["sales_volume"].mean(),
    len(test)
)

print("Baseline MAE:", round(mean_absolute_error(
    test["sales_volume"],
    baseline_prediction
), 2))

print("Baseline RMSE:", round(mean_squared_error(
    test["sales_volume"],
    baseline_prediction
) ** 0.5, 2))

print("Baseline R2:", round(r2_score(
    test["sales_volume"],
    baseline_prediction
), 3))
