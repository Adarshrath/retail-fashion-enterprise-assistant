
import pandas as pd, numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from .data_utils import load_data

FEATURES=["product_position","promotion","product_category","seasonal","brand","price"]
def train_model():
    df=load_data().dropna(subset=["sales_volume","price"]).copy()
    X=df[FEATURES].copy(); y=df["sales_volume"]
    cat=[c for c in FEATURES if c!="price"]; num=["price"]
    pre=ColumnTransformer([("cat",OneHotEncoder(handle_unknown="ignore"),cat)],remainder="passthrough")
    model=Pipeline([("pre",pre),("rf",RandomForestRegressor(n_estimators=300,random_state=42,min_samples_leaf=2))])
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42)
    model.fit(Xtr,ytr); p=model.predict(Xte)
    return model,{"mae":round(float(mean_absolute_error(yte,p)),2),
                    "rmse":round(float(mean_squared_error(yte,p)**.5),2),
                    "r2":round(float(r2_score(yte,p)),3)}
def estimate(product_id):
    df=load_data(); row=df[df.product_id.astype(str)==str(product_id)]
    if row.empty:return {"error":"Product ID not found"}
    model,metrics=train_model()
    pred=model.predict(row[FEATURES])[0]
    return {"product_id":str(product_id),"estimated_sales_volume":round(float(max(0,pred)),1),"metrics":metrics}
