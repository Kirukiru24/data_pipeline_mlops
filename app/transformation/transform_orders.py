import pandas as pd
from app.config.db import engine

def load_raw():
    return pd.read_sql("SELECT * FROM raw_orders", engine)

def transform(df):
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['date'] = df['created_at'].dt.date

    dim_customers = df[['customer_id']].drop_duplicates()

    dim_dates = df[['date']].drop_duplicates()
    dim_dates['year'] = pd.to_datetime(dim_dates['date']).dt.year
    dim_dates['month'] = pd.to_datetime(dim_dates['date']).dt.month
    dim_dates['day'] = pd.to_datetime(dim_dates['date']).dt.day

    fact_orders = df[['order_id', 'customer_id', 'date', 'amount']]

    return dim_customers, dim_dates, fact_orders

def load(dim_customers, dim_dates, fact_orders):
    dim_customers.to_sql("dim_customers", engine, if_exists="append", index=False)
    dim_dates.to_sql("dim_dates", engine, if_exists="append", index=False)
    fact_orders.to_sql("fact_orders", engine, if_exists="append", index=False)

def run():
    df = load_raw()
    dim_customers, dim_dates, fact_orders = transform(df)
    load(dim_customers, dim_dates, fact_orders)
    print("Transformation complete")

if __name__ == "__main__":
    run()
