FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Inject Vercel Web Analytics script into Streamlit's index.html
RUN sed -i "/<\/head>/i\
<script defer src=\"https://cdn.vercel-insights.com/v1/script.js\"></script>" \
$(python -c "import streamlit, os; print(os.path.join(os.path.dirname(streamlit.__file__), 'static', 'index.html'))")

EXPOSE 8501
CMD ["streamlit","run","dashboard/app.py","--server.address=0.0.0.0"]
