from fastapi import FastAPI
import joblib as jb
from pydantic import BaseModel
from trainer import Trainer
import os.path

class DataToPredict(BaseModel):
    X: list


app = FastAPI()

model = None

# load model if it exists
if (os.path.isfile('model/model.joblib')):
    model = jb.load('model/model.joblib')

trainer = Trainer(model)


@app.get("/")
async def root():
    return {"message": "Projet ML Embarqué"}

@app.get("/train")
async def train():
    return {"train": trainer.train()}

@app.post("/predict")
async def post_prediction(data: DataToPredict):
    prediction = trainer.predict(data.X).tolist()

    return {"prediction": prediction}
