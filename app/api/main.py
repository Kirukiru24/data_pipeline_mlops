from fastapi import FastAPI
import mlflow.pyfunc
import pandas as pd
import numpy as np
from datetime import datetime

app = FastAPI()

# --- MLflow setup ---
mlflow.set_tracking_uri("sqlite:///mlflow.db")
MODEL_NAME = "model"

# 🔥 Load latest Production model automatically
model = mlflow.pyfunc.load_model(f"models:/{MODEL_NAME}@production")

# --- Feature engineering ---
def build_inference_features(amount: float, date: str = None):
    # Parse date
    if date:
        try:
            date_obj = datetime.fromisoformat(date)
        except ValueError:
            date_obj = datetime.strptime(date, "%m/%d/%Y")
    else:
        date_obj = datetime.now()

    # Exact same features as training
    df = pd.DataFrame([{
        "amount": amount,
        "amount_log": np.log1p(amount),
        "day_of_week": date_obj.weekday()
    }])
    return df

# --- Endpoints ---
@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(amount: float, date: str = None):
    df = build_inference_features(amount, date)
    prediction = model.predict(df)[0]

    return {
        "prediction": int(prediction),
        "features": df.to_dict(orient="records")[0]
    }