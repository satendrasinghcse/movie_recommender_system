from sklearn.feature_extraction.text import TfidfVectorizer
from src.utils.helpers import load_config,save_object,data_reader
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

config = load_config()



def model_trainer():
    tv = TfidfVectorizer(max_features=5000,stop_words='english')
    vector = tv.fit_transform(data_reader(config["data"]["processed_data_path"])['tags']).toarray()
    similarity = cosine_similarity(vector)
    save_object(config["artifacts"]["similarity_path"],similarity)
