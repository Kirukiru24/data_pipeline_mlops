import pandas as pd
from datetime import datetime

def build_inference_features(amount: float, date: str = None) -> pd.DataFrame:
    """
    Build features for inference.
    
    Args:
        amount (float): Order amount
        date (str): Optional ISO date string (e.g., '2026-04-01')
    
    Returns:
        pd.DataFrame: Model-ready features
    """

    # Default to current date if not provided
    if date is None:
        date_obj = datetime.now()
    else:
        date_obj = datetime.fromisoformat(date)

    # Feature engineering (MUST match training logic)
    amount_log = amount + 1
    day_of_week = date_obj.weekday()

    df = pd.DataFrame([{
        "amount": amount,
        "amount_log": amount_log,
        "day_of_week": day_of_week
    }])

    return df