from src.utils.helpers import load_config,save_object,data_reader
import pandas as pd
import json

config = load_config()



def extract(str):
    text_list = json.loads(str)
    text = [genre['name'] for genre in text_list]
    return text

def extract3(str):
    text_list = json.loads(str)
    text = [genre['name'] for genre in text_list]
    return text[:3]



def find_directors(data):
    name = []
    data = json.loads(data)
    for i in data:
        if i['job']=='Director':
            name.append(i["name"])
    return name

def data_transform():
    df = data_reader(config["data"]["raw_data_path"])
    df = df[['movie_id','title','overview','genres','keywords','cast','production_companies','crew']]

    df["keywords"] = df["keywords"].apply(extract)
    df["genres"] = df["genres"].apply(extract)
    df["cast"] = df["cast"].apply(extract3)
    df["production_companies"] = df["production_companies"].apply(extract3)
    df["crew"] = df["crew"].apply(find_directors)
    df["overview"] = df["overview"].apply(lambda x:str(x).split())
    df["tags"] = df["title"].apply(lambda x:x.split())+df["cast"]+df["crew"]+df["genres"]+df["keywords"]+df["overview"]+df["production_companies"]
    new_df = df.drop(columns=['overview', 'genres', 'keywords', 'cast','production_companies', 'crew'])
    new_df["tags"] = new_df["tags"].apply(lambda x:" ".join(x))
    new_df.to_csv(config["data"]["processed_data_path"])
    save_object(config["artifacts"]["movies_list_path"],new_df)

    return new_df
