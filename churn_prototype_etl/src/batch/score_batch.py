import os
import argparse
import pandas as pd
from joblib import load

FEATURE_COLS = [
    "tenure_months","orders_last_6m","avg_order_value","total_spend_12m",
    "last_order_days_ago","support_tickets_6m","returns_6m",
    "discount_rate","sessions_30d","pages_per_session","email_open_rate",
    "is_premium_member","region","preferred_channel"
]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--in", dest="in_path", required=True)
    ap.add_argument("--out", dest="out_path", required=True)
    args = ap.parse_args()
    print(f"output path: {args.out_path}")

    # makesure output path exists
    out_dir = os.path.dirname(args.out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)


    df = pd.read_csv(args.in_path)
    pipe = load(args.model)
    proba = pipe.predict_proba(df[FEATURE_COLS])[:, 1]
    pred = (proba >= 0.5).astype(int)
    out = df.copy()
    out["churn_probability"] = proba
    out["churn_pred"] = pred
    out.to_csv(args.out_path, index=False)
    print(f"Wrote predictions -> {args.out_path}")

if __name__ == "__main__":
    main()
