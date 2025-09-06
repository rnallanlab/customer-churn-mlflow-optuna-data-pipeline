from fastapi import FastAPI
from pydantic import BaseModel, Field
from joblib import load
import pandas as pd
import os

MODEL_PATH = os.environ.get("CHURN_MODEL_PATH", "models/model.joblib")
pipe = load(MODEL_PATH)

class ChurnRequest(BaseModel):
    tenure_months: int
    orders_last_6m: int
    avg_order_value: float
    total_spend_12m: float
    last_order_days_ago: int
    support_tickets_6m: int
    returns_6m: int
    is_premium_member: int = Field(0, description="0 or 1")
    discount_rate: float
    sessions_30d: int
    pages_per_session: float
    email_open_rate: float
    region: str
    preferred_channel: str

app = FastAPI(title="Churn Predictor")

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(req: ChurnRequest):
    row = pd.DataFrame([req.dict()])
    proba = pipe.predict_proba(row)[:, 1][0]
    pred = int(proba >= 0.5)
    return {"churn_probability": float(proba), "churn_pred": pred}
