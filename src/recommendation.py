
from .data_utils import load_data
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def recommend(product_id,k=5):
    df=load_data().reset_index(drop=True)
    idx=df.index[df.product_id.astype(str)==str(product_id)].tolist()
    if not idx:return []
    text=(df["product_category"].fillna("")+" "+df["brand"].fillna("")+" "+
          df["terms"].fillna("")+" "+df["name"].fillna("")+" "+df["description"].fillna(""))
    mat=TfidfVectorizer(stop_words="english").fit_transform(text)
    scores=cosine_similarity(mat[idx[0]],mat).ravel()
    order=scores.argsort()[::-1]
    out=[]
    for i in order:
        if i==idx[0]:continue
        out.append({"product_id":str(df.iloc[i]["product_id"]),"name":df.iloc[i]["name"],
                    "category":df.iloc[i]["product_category"],"similarity":round(float(scores[i]),4)})
        if len(out)>=k:break
    return out
