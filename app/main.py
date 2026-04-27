from app.ingestion.ingest_api import run as ingest
from app.transformation.transform_orders import run as transform

def pipeline():
    ingest()
    transform()

if __name__ == "__main__":
    pipeline()
