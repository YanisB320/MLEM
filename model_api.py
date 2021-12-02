from fastapi import FastAPI
import joblib as jb
from pydantic import BaseModel

class DataToPredict(BaseModel):
    X: list


app = FastAPI()

model = jb.load('model/clf.joblib')

prediction = None


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict")
async def post_prediction(data: DataToPredict):
    prediction = model.predict(data.X).tolist()

    return {"prediction": prediction}
