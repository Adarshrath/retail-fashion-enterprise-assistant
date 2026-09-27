
from src.data_utils import load_data
from src.recommendation import recommend
def test_data(): assert len(load_data())==252
def test_recommendation(): assert len(recommend(str(load_data().iloc[0].product_id)))>0
