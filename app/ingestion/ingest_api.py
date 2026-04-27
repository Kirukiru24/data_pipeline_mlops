import requests
import pandas as pd
from app.config.db import engine

API_URL = "https://dummyjson.com/carts"

def fetch_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    
    data = response.json()

    if "carts" not in data:
        raise ValueError("Invalid API structure")

    return data["carts"]

def transform_raw(data):
    rows = []

    for item in data:
        rows.append({
            "order_id": str(item["id"]),
            "customer_id": str(item["userId"]),
            "amount": float(item["total"]),
            "status": "completed",
            "created_at": pd.Timestamp.now()
        })

    return pd.DataFrame(rows)

def load_raw(df):
    df.to_sql("raw_orders", engine, if_exists="append", index=False)

def run():
    data = fetch_data()
    df = transform_raw(data)
    load_raw(df)
    print("Data ingested successfully")