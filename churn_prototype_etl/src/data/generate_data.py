import argparse, csv, random, math, datetime, os

REGIONS = ["NA", "EU", "APAC", "LATAM"]
CHANNELS = ["web", "mobile", "email", "store"]

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

def gen_row(i, base_date):
    # core attributes
    tenure_months = max(0, int(random.gauss(12, 10)))
    orders_last_6m = max(0, int(random.gauss(3, 2)))
    avg_order_value = max(5.0, min(300.0, random.gauss(65, 25)))
    total_spend_12m = max(0.0, avg_order_value * max(0, int(random.gauss(8, 4))) + random.uniform(-50, 50))
    last_order_days_ago = max(0, min(400, int(abs(random.gauss(45, 60)))))
    support_tickets_6m = max(0, int(random.gauss(0.6, 1.1)))
    returns_6m = max(0, int(random.gauss(0.4, 0.9)))
    is_premium_member = 1 if random.random() < 0.25 else 0
    discount_rate = max(0.0, min(0.6, random.random() * (0.3 if is_premium_member else 0.6)))
    sessions_30d = max(0, int(abs(random.gauss(12, 10))))
    pages_per_session = max(1.0, min(15.0, random.gauss(4.0, 1.5)))
    email_open_rate = max(0.0, min(1.0, random.gauss(0.28, 0.2)))
    region = random.choice(REGIONS)
    preferred_channel = random.choice(CHANNELS)

    # derive label via logistic model (transparent rules)
    logit = -0.2
    if tenure_months < 3: logit += 1.4
    if orders_last_6m == 0: logit += 1.1
    if last_order_days_ago > 90: logit += 0.9
    if support_tickets_6m > 2: logit += 0.6
    if returns_6m > 1: logit += 0.5
    if is_premium_member: logit -= 1.0
    if total_spend_12m > 500: logit -= 0.8
    if sessions_30d > 10 and pages_per_session > 3: logit -= 0.6
    if email_open_rate > 0.3: logit -= 0.5
    if discount_rate > 0.15: logit -= 0.2
    # slight regional/channel noise
    if region in ("LATAM", "APAC"): logit += 0.1
    if preferred_channel == "email": logit += 0.1
    logit += random.gauss(0.0, 0.4)

    churn_prob = max(0.001, min(0.999, sigmoid(logit)))
    churned = 1 if random.random() < churn_prob else 0

    # dates
    snapshot_date = base_date.strftime("%Y-%m-%d")
    last_order_date = (base_date - datetime.timedelta(days=last_order_days_ago)).strftime("%Y-%m-%d")

    return {
        "customer_id": f"C{i:06d}",
        "snapshot_date": snapshot_date,
        "region": region,
        "preferred_channel": preferred_channel,
        "tenure_months": tenure_months,
        "orders_last_6m": orders_last_6m,
        "avg_order_value": round(avg_order_value, 2),
        "total_spend_12m": round(total_spend_12m, 2),
        "last_order_days_ago": last_order_days_ago,
        "last_order_date": last_order_date,
        "support_tickets_6m": support_tickets_6m,
        "returns_6m": returns_6m,
        "is_premium_member": is_premium_member,
        "discount_rate": round(discount_rate, 3),
        "sessions_30d": sessions_30d,
        "pages_per_session": round(pages_per_session, 2),
        "email_open_rate": round(email_open_rate, 3),
        "churned": churned
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=10000, help="Number of customers")
    ap.add_argument("--out", type=str, default="data/churn.csv", help="Output CSV path")
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    base_date = datetime.date.today()
    fieldnames = [
        "customer_id","snapshot_date","region","preferred_channel",
        "tenure_months","orders_last_6m","avg_order_value","total_spend_12m",
        "last_order_days_ago","last_order_date","support_tickets_6m","returns_6m",
        "is_premium_member","discount_rate","sessions_30d","pages_per_session",
        "email_open_rate","churned"
    ]
    with open(args.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for i in range(1, args.n + 1):
            row = gen_row(i, base_date)
            w.writerow(row)
    print(f"Wrote {args.n} rows -> {args.out}")

if __name__ == "__main__":
    main()
