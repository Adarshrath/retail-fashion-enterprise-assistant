
from fastapi import FastAPI
from pydantic import BaseModel,Field
from src.eda import summary
from src.demand_model import estimate
from src.recommendation import recommend
from src.rag.engine import RAG
from src.agents.system import Supervisor
app=FastAPI(title="Retail Fashion Enterprise Assistant")
rag=RAG(); supervisor=Supervisor()
class ProductRequest(BaseModel):
    product_id:str
class ChatRequest(BaseModel):
    question:str
class AgentRequest(BaseModel):
    task:str
    product_id:str|None=None
@app.get("/")
def root(): return {"status":"ok"}
@app.get("/health")
def health(): return {"status":"healthy"}
@app.get("/eda/summary")
def eda(): return summary()
@app.post("/demand")
def demand(r:ProductRequest): return estimate(r.product_id)
@app.post("/recommend")
def rec(r:ProductRequest): return {"recommendations":recommend(r.product_id)}
@app.post("/chat")
def chat(r:ChatRequest): return rag.answer(r.question)
@app.post("/agent")
def agent(r:AgentRequest): return supervisor.route(r.task,r.product_id)
