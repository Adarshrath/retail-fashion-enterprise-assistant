
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from src.data_utils import load_data
from src.demand_model import estimate
from src.recommendation import recommend
from src.rag.engine import RAG
from src.agents.system import Supervisor
st.set_page_config(page_title="Retail Fashion Enterprise Assistant",layout="wide")

# Inject Vercel Web Analytics script
components.html(
    """
    <script defer src="https://cdn.vercel-insights.com/v1/script.js"></script>
    """,
    height=0,
)
df=load_data()
st.title("Retail Fashion Enterprise Assistant")
st.caption("Kaggle Zara Fashion Sales Dataset • EDA • Demand Estimation • Recommendations • RAG • Agents")
a,b,c,d=st.columns(4)
a.metric("Products",len(df)); b.metric("Sales Volume",f"{df.sales_volume.sum():,.0f}")
c.metric("Avg Price",f"${df.price.mean():,.2f}"); d.metric("Promotion Rate",f"{df.promotion_flag.mean()*100:.1f}%")
t1,t2,t3,t4=st.tabs(["Insights","Demand","Recommendations","AI Assistant"])
with t1:
    st.subheader("Sales Volume by Category")
    st.bar_chart(df.groupby("product_category")["sales_volume"].sum())
    st.subheader("Top Products")
    st.dataframe(df.nlargest(10,"sales_volume")[["product_id","name","product_category","sales_volume","price"]],use_container_width=True)
with t2:
    pid=st.selectbox("Product ID",df.product_id.astype(str).tolist())
    if st.button("Estimate Demand"):
        st.json(estimate(pid))
with t3:
    pid=st.selectbox("Base product",df.product_id.astype(str).tolist(),key="rec")
    if st.button("Recommend"):
        st.dataframe(pd.DataFrame(recommend(pid)),use_container_width=True)
with t4:
    q=st.text_input("Ask about returns, shipping, sizing or the project")
    if st.button("Ask") and q: st.write(RAG().answer(q))
    task=st.text_input("Agent task")
    pid2=st.text_input("Optional product ID")
    if st.button("Run Agent") and task: st.json(Supervisor().route(task,pid2 or None))
