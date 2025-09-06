import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

engine = create_engine("postgresql://churnuser:churnpassword@localhost:5432/customer")
df = pd.read_sql("select * from analytics.churn_features", engine)
features = ["is_premium_member", "total_orders", "total_revenue", "days_since_last_order"]
X = df[features].fillna(0)
y = df["churned"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

joblib.dump(model, "model.joblib")
