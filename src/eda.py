
from .data_utils import load_data
def summary():
    df=load_data()
    return {
      "rows":len(df),"columns":list(df.columns),
      "missing":df.isna().sum().to_dict(),
      "categories":df["product_category"].value_counts().to_dict(),
      "promotion_share":round(float(df["promotion_flag"].mean()),4),
      "total_sales_volume":int(df["sales_volume"].sum()),
      "revenue_proxy":round(float(df["revenue_proxy"].sum()),2),
      "top_products":df.nlargest(10,"sales_volume")[["name","sales_volume"]].to_dict("records")
    }
