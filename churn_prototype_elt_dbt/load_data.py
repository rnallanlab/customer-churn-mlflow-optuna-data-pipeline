# load_data.py
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://churnuser:churnpassword@localhost:5432/customer")

pd.read_csv("data/customers.csv").to_sql("raw_customers", engine, if_exists="replace", index=False)
pd.read_csv("data/orders.csv").to_sql("raw_orders", engine, if_exists="replace", index=False)
