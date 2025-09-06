import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Customers
n_customers = 1000
customers = pd.DataFrame({
    "customer_id": range(1, n_customers+1),
    "signup_date": [datetime(2020,1,1) + timedelta(days=np.random.randint(0,1000)) for _ in range(n_customers)],
    "is_premium_member": np.random.choice([0,1], n_customers)
})

# Orders
orders = []
for c in range(1, n_customers+1):
    n_orders = np.random.poisson(5)
    for _ in range(n_orders):
        orders.append({
            "order_id": f"{c}_{_}",
            "customer_id": c,
            "order_date": datetime(2025,1,1) + timedelta(days=np.random.randint(0,200)),
            "amount": np.random.exponential(100),
            "status": np.random.choice(["paid","refunded"], p=[0.9,0.1])
        })
orders = pd.DataFrame(orders)

# Save CSVs
customers.to_csv("data/customers.csv", index=False)
orders.to_csv("data/orders.csv", index=False)
