import toml
import pickle
import pandas as pd

def load_config(config_path="configs/config.toml"):
    with open(config_path,"r") as f:
        config = toml.load(f)
    return config


def save_object(file_path,obj):
     with open(file_path, "wb") as file_obj:
         pickle.dump(obj, file_obj)


def data_reader(path):
    return pd.read_csv(path)
