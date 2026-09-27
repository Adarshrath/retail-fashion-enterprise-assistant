
from ..recommendation import recommend
from ..demand_model import estimate
from ..rag.engine import RAG
from ..data_utils import load_data
class InventoryAgent:
    def run(self):
        df=load_data()
        g=df.groupby(["product_id","name"],as_index=False)["sales_volume"].sum().sort_values("sales_volume",ascending=False)
        return {"top_demand_products":g.head(10).to_dict("records"),
                "note":"Inventory optimization needs stock-on-hand data; this dataset does not provide current inventory levels."}
class RecommendationAgent:
    def run(self,product_id): return recommend(product_id,5)
class CustomerServiceAgent:
    def __init__(self): self.rag=RAG()
    def run(self,q): return self.rag.answer(q)
class Supervisor:
    def __init__(self):
        self.inv=InventoryAgent(); self.rec=RecommendationAgent(); self.cs=CustomerServiceAgent()
    def route(self,task,product_id=None):
        t=task.lower()
        if any(x in t for x in ["inventory","stock","demand","sales"]): return {"agent":"Inventory Agent","result":self.inv.run()}
        if any(x in t for x in ["recommend","similar","suggest"]): return {"agent":"Recommendation Agent","result":self.rec.run(product_id)} if product_id else {"agent":"Recommendation Agent","result":[],"message":"product_id required"}
        return {"agent":"Customer Service Agent","result":self.cs.run(task)}
