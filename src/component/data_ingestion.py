import pandas as pd
from src.utils.helpers import load_config

def data_lodder():
    config = load_config()
    df1 = pd.read_csv("notebooks/tmdb_5000_credits.csv")
    df2 = pd.read_csv("notebooks/tmdb_5000_movies.csv")
    df = df1.merge(df2,on="title")
    df.to_csv(config["data"]["raw_data_path"])
    return df1
