import pathlib
from contextlib import asynccontextmanager

from fastapi import FastAPI

from .ml import KMeans
from .models import Request

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "km.pkl"


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = KMeans(MODEL_PATH)
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/predict")
def predict(req: Request):
    pred = app.state.model.predict(req.data)
    return pred
