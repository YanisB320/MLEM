from fastapi import FastAPI
from pydantic import BaseModel
from trainer import Trainer

class DataToPredict(BaseModel):
    X: list

class DataToTrain(BaseModel):
    X: list
    y: int


app = FastAPI()

trainer = Trainer()


@app.get("/")
async def root():
    return {"message": "Projet ML Embarqué"}

@app.post("/train")
async def train(data: DataToTrain):
    return {"train": trainer.train(data.X, data.y)}

@app.post("/predict")
async def post_prediction(data: DataToPredict):
    prediction = trainer.predict(data.X).tolist()

    return {"prediction": prediction}
