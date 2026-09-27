
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
import matplotlib.pyplot as plt
from src.data_utils import load_data
df=load_data()
print("Shape:",df.shape)
print("\nMissing values:\n",df.isna().sum())
print("\nDuplicate rows:",df.duplicated().sum())
print("\nNumeric summary:\n",df[["price","sales_volume","revenue_proxy"]].describe())
print("\nCategories:\n",df["product_category"].value_counts())
print("\nTop products:\n",df.nlargest(10,"sales_volume")[["product_id","name","sales_volume"]])
df.groupby("product_category")["sales_volume"].sum().sort_values().plot(kind="barh",figsize=(10,6),title="Sales Volume by Category")
plt.tight_layout(); plt.show()
