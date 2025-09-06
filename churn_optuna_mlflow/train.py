import mlflow
import mlflow.sklearn
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

def load_data(path="data/raw_customers.csv"):
    df = pd.read_csv(path)
    # Features should align with your build_features logic
    feature_cols = [
        "tenure_months", "orders_last_6m", "avg_order_value",
        "total_spend_12m", "support_tickets_6m", "returns_6m",
        "is_premium_member", "discount_rate", "sessions_30d",
        "pages_per_session", "email_open_rate"
    ]
    X = df[feature_cols]
    y = df["churned"]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_and_log(params: dict, run_name="manual_run"):
    X_train, X_test, y_train, y_test = load_data()

    with mlflow.start_run(run_name=run_name):
        # Train
        model = xgb.XGBClassifier(
            n_estimators=params.get("n_estimators", 100),
            max_depth=params.get("max_depth", 5),
            learning_rate=params.get("learning_rate", 0.1),
            subsample=params.get("subsample", 0.8),
            colsample_bytree=params.get("colsample_bytree", 0.8),
            random_state=42,
            use_label_encoder=False,
            eval_metric="logloss"
        )
        model.fit(X_train, y_train)

        # Evaluate
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        f1 = f1_score(y_test, preds)

        # Log params and metrics
        mlflow.log_params(params)
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1_score", f1)

        # Save model
        mlflow.sklearn.log_model(model, "model")

        return acc, f1
