# Architecture
Streamlit Dashboard -> FastAPI -> Domain Services

Domain services:
- EDA / analytics
- Demand estimation model
- Content-based recommendation
- Local RAG
- Specialist agents + supervisor

Data:
Kaggle Zara Fashion Sales Dataset.

Important data limitation:
The supplied dataset has 252 product records and `scraped_at` timestamps from a short scraping run. It is NOT a multi-period daily sales history. Therefore the forecasting module is implemented as **demand estimation / sales-volume prediction**, not a true time-series forecast. A true forecasting model requires historical sales by date.
