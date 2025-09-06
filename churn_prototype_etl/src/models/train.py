import os
import argparse, json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, average_precision_score
from joblib import dump, load

FEATURE_COLS_NUM = [
    "tenure_months","orders_last_6m","avg_order_value","total_spend_12m",
    "last_order_days_ago","support_tickets_6m","returns_6m",
    "discount_rate","sessions_30d","pages_per_session","email_open_rate",
    "is_premium_member"
]
FEATURE_COLS_CAT = ["region","preferred_channel"]
TARGET = "churned"

def build_pipeline():
    pre = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(with_mean=False), FEATURE_COLS_NUM),
            ("cat", OneHotEncoder(handle_unknown="ignore"), FEATURE_COLS_CAT),
        ]
    )
    clf = LogisticRegression(max_iter=200, class_weight="balanced", n_jobs=None)
    pipe = Pipeline([
        ("pre", pre),
        ("clf", clf)
    ])
    return pipe

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True, help="Path to CSV with raw data")
    ap.add_argument("--model", required=True, help="Path to write model.joblib")
    ap.add_argument("--metrics", required=True, help="Path to write metrics.json")
    args = ap.parse_args()
    os.makedirs(os.path.dirname(args.model), exist_ok=True)
    os.makedirs(os.path.dirname(args.metrics), exist_ok=True)

    df = pd.read_csv(args.data)

    X = df[FEATURE_COLS_NUM + FEATURE_COLS_CAT]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipe = build_pipeline()
    pipe.fit(X_train, y_train)

    # Evaluate
    y_proba = pipe.predict_proba(X_test)[:, 1]
    y_pred = (y_proba >= 0.5).astype(int)
    roc = roc_auc_score(y_test, y_proba)
    pr = average_precision_score(y_test, y_proba)
    metrics = {
        "roc_auc": float(roc),
        "average_precision": float(pr),
        "n_train": int(len(X_train)),
        "n_test": int(len(X_test))
    }
    with open(args.metrics, "w") as f:
        json.dump(metrics, f, indent=2)
    dump(pipe, args.model)
    # Curious to see what the model looks like after training
    model = load(args.model)
    print(f"Model coefficients: {model.named_steps['clf'].coef_}")
    print(f"Model intercept: {model.named_steps['clf'].intercept_}")    
    print(f"Saved model -> {args.model}")
    print(f"Metrics -> {args.metrics}: {metrics}")

if __name__ == "__main__":
    main()
