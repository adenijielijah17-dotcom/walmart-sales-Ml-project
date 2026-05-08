from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Create app
app = FastAPI()

# Load your trained model
model = joblib.load("xgb_model.pkl")


# Input schema (MATCHES YOUR COLUMNS)
class InputData(BaseModel):
    store: float
    holiday_flag: float
    temperature: float
    fuel_price: float
    cpi: float
    unemployment: float
    weekly_sales_log: float
    fuel_price_log: float


# Home route
@app.get("/")
def home():
    return {"message": "Model API is running"}


# Prediction route
@app.post("/predict")
def predict(data: InputData):

    df = pd.DataFrame([{
        "store": data.store,
        "holiday_flag": data.holiday_flag,
        "temperature": data.temperature,
        "fuel_price": data.fuel_price,
        "cpi": data.cpi,
        "unemployment": data.unemployment,
        "weekly_sales_log": data.weekly_sales_log,
        "fuel_price_log": data.fuel_price_log
    }])

    prediction = model.predict(df)

    return {
        "prediction": prediction.tolist()
}