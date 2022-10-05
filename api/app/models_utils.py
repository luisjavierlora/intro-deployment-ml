from joblib import load
import joblib
from sklearn.pipeline import Pipeline
from pydantic import BaseModel
from pandas import DataFrame
import os 
from io import BytesIO
import pickle

def get_model() -> Pipeline:
    model_path = os.environ.get('MODEL_PATH','model/model.pkl')
    with open(model_path,'rb') as model_file :
        
        model = joblib.load(model_file)

    return model

def transform_to_dataframe(class_model : BaseModel)->DataFrame:
    transition_dictionary = {key: [value] for key,value in class_model.dict().items()}
    data_frame = DataFrame(transition_dictionary)
    return data_frame