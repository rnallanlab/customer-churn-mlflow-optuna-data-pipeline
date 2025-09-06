import argparse
import pandas as pd

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("in_csv", type=str)
    ap.add_argument("out_parquet", type=str)
    args = ap.parse_args()

    df = pd.read_csv(args.in_csv)

    # Light cleanup / sanity
    df = df.dropna(subset=["customer_id", "snapshot_date"])
    # Ensure types
    df["is_premium_member"] = df["is_premium_member"].astype(int)
    df["churned"] = df["churned"].astype(int)

    # Save as parquet for faster IO
    df.to_parquet(args.out_parquet, index=False)
    print(f"Wrote features to {args.out_parquet} (shape={df.shape})")

if __name__ == "__main__":
    main()
