
from pathlib import Path
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
ROOT=Path(__file__).resolve().parents[2]
class RAG:
    def __init__(self):
        chunks=[]; sources=[]
        for p in (ROOT/"data/raw").glob("*.txt"):
            for c in re.split(r"\n\s*\n",p.read_text(encoding="utf-8")):
                if c.strip(): chunks.append(c.strip()); sources.append(p.name)
        self.chunks,self.sources=chunks,sources
        self.vec=TfidfVectorizer(stop_words="english",ngram_range=(1,2))
        self.mat=self.vec.fit_transform(chunks)
    def answer(self,q,k=3):
        scores=cosine_similarity(self.vec.transform([q]),self.mat).ravel()
        ids=scores.argsort()[::-1][:k]
        docs=[{"source":self.sources[i],"text":self.chunks[i],"score":round(float(scores[i]),4)}
              for i in ids if scores[i]>0]
        if not docs:return {"answer":"I could not find this in the enterprise knowledge base.","sources":[]}
        return {"answer":"Based on the retrieved enterprise information:\n\n"+"\n\n".join(d["text"] for d in docs),
                "sources":docs}
