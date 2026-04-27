import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from app.ml.features import get_features

def train():
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    # 1. Set the experiment name (creates it if it doesn't exist)
    mlflow.set_experiment("order_prediction")

    X, y = get_features()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    # 2. Start the run within that experiment
    with mlflow.start_run():
        mlflow.log_param("model_type", "RandomForest")
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("accuracy", accuracy)
        
        # Using artifact_path to avoid deprecation warnings
        mlflow.sklearn.log_model(model, artifact_path="model")

    print(f"✅ Model trained and logged to 'order_prediction'. Accuracy: {accuracy}")

if __name__ == "__main__":
    print("🚀 Starting training script...")
    train()