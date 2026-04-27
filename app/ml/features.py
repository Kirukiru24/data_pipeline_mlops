import pandas as pd
from app.config.db import engine

def load_data():
    query = """
    SELECT order_id, customer_id, date, amount
    FROM fact_orders
    """
    df = pd.read_sql(query, engine)

    if df.empty:
        raise ValueError("No data found in fact_orders")

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Remove nulls
    df = df.dropna()

    # Ensure correct types
    df['amount'] = df['amount'].astype(float)

    return df


def build_features(df: pd.DataFrame):
    # --- Feature Engineering ---
    
    # Log transformation (helps model stability)
    df['amount_log'] = df['amount'].apply(lambda x: x + 1)

    # Example behavioral feature
    df['high_value_flag'] = (df['amount'] > 50).astype(int)

    # Time-based feature
    df['date'] = pd.to_datetime(df['date'])
    df['day_of_week'] = df['date'].dt.dayofweek

    # --- Label (Target Variable) ---
    # Example: classify high-value orders
    df['label'] = (df['amount'] > 50).astype(int)

    # --- Feature Set ---
    feature_columns = [
        "amount",
        "amount_log",
        "day_of_week"
    ]

    X = df[feature_columns]
    y = df["label"]

    return X, y


def get_features():
    df = load_data()
    df = clean_data(df)
    X, y = build_features(df)

    return X, y