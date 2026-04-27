-- RAW TABLE
CREATE TABLE IF NOT EXISTS raw_orders (
    id SERIAL PRIMARY KEY,
    order_id TEXT,
    customer_id TEXT,
    amount NUMERIC,
    status TEXT,
    created_at TIMESTAMP
);

-- DIMENSIONS
CREATE TABLE IF NOT EXISTS dim_customers (
    customer_id TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS dim_dates (
    date DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT
);

-- FACT TABLE
CREATE TABLE IF NOT EXISTS fact_orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT,
    date DATE,
    amount NUMERIC,
    FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id),
    FOREIGN KEY (date) REFERENCES dim_dates(date)
);
