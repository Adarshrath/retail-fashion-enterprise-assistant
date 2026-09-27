# Retail Fashion Enterprise Assistant — Kaggle Version

## Dataset
Kaggle Zara Fashion Sales Dataset, supplied as `zara_fashion_sales.csv`.

## Run
python -m venv venv
Windows: venv\\Scripts\\activate
pip install -r requirements.txt

Dashboard:
streamlit run dashboard/app.py

API:
uvicorn api.main:app --reload

EDA:
python notebooks/01_eda.py

Tests:
pytest

## What is implemented
1. EDA and visualization
2. Demand/sales-volume prediction
3. Content-based recommendation using TF-IDF + cosine similarity
4. Local RAG over enterprise policy/product documents
5. Inventory, Recommendation and Customer Service agents
6. Supervisor routing
7. FastAPI API
8. Streamlit dashboard

## Honest modeling note
This Kaggle dataset is product-level data rather than a full longitudinal transaction history. Thus this project does not falsely claim a time-series sales forecast. The ML module predicts sales volume from available product attributes. For true forecasting, add historical daily/weekly sales data.
