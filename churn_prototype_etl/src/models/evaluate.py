import argparse, os, json
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, average_precision_score
from joblib import load
import matplotlib.pyplot as plt

FEATURE_COLS_NUM = [
    "tenure_months","orders_last_6m","avg_order_value","total_spend_12m",
    "last_order_days_ago","support_tickets_6m","returns_6m",
    "discount_rate","sessions_30d","pages_per_session","email_open_rate",
    "is_premium_member"
]
FEATURE_COLS_CAT = ["region","preferred_channel"]
TARGET = "churned"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True, help="CSV path")
    ap.add_argument("--model", required=True, help="model.joblib")
    ap.add_argument("--outdir", required=True, help="reports directory")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    df = pd.read_csv(args.data)
    X = df[FEATURE_COLS_NUM + FEATURE_COLS_CAT]
    y = df[TARGET]

    pipe = load(args.model)
    y_proba = pipe.predict_proba(X)[:, 1]
    y_pred = (y_proba >= 0.5).astype(int)

    # Metrics
    roc = roc_auc_score(y, y_proba)
    pr = average_precision_score(y, y_proba)
    report = classification_report(y, y_pred, output_dict=True)
    with open(os.path.join(args.outdir, "classification_report.json"), "w") as f:
        json.dump(report, f, indent=2)
    with open(os.path.join(args.outdir, "summary.txt"), "w") as f:
        f.write(f"ROC AUC: {roc:.4f}\n")
        f.write(f"Average Precision (PR AUC): {pr:.4f}\n")

    # Confusion matrix plot (single chart, default colors)
    cm = confusion_matrix(y, y_pred)
    plt.figure()
    plt.imshow(cm, interpolation='nearest')
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    for (i, j), val in np.ndenumerate(cm):
        plt.text(j, i, int(val), ha='center', va='center')
    plt.tight_layout()
    plt.savefig(os.path.join(args.outdir, "confusion_matrix.png"))
    plt.close()

    print(f"Wrote reports to {args.outdir}")

if __name__ == "__main__":
    import numpy as np
    main()
