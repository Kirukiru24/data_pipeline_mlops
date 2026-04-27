# End-to-End MLOps Pipeline

This project demonstrates a full AI lifecycle system:

## 🚀 Features
- Data ingestion from API
- Data warehouse (PostgreSQL)
- Feature engineering
- Model training with MLflow
- Model registry (Production stage)
- FastAPI inference service

## 🧱 Architecture
API → Data Pipeline → Feature Engineering → MLflow → Model Registry → FastAPI

## 🛠 Tech Stack
- Python
- PostgreSQL
- MLflow
- FastAPI
- Docker

## ▶️ Run
```bash
docker-compose up -d
python -m app.main
python -m app.ml.train
python -m uvicorn app.api.main:app --reload
