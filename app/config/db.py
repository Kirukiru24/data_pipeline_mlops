from sqlalchemy import create_engine

DB_URL = "postgresql://postgres:kira@localhost:5432/de_db"

engine = create_engine(DB_URL)
