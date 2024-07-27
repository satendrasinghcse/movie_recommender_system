import pickle
from src.utils.helpers import load_config

config = load_config()


def recommend(movie):
    with open(config["artifacts"]["movies_list_path"],"rb") as f:
        ndf = pickle.load(f)

    with open(config["artifacts"]["similarity_path"],"rb") as f:
        similarity = pickle.load(f)
        
    index = ndf[ndf['title'].str.lower() == str(movie).lower()].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommend_movies = []
    for i in distances[1:6]:
        recommend_movies.append(ndf.iloc[i[0]].title)
    return recommend_movies

