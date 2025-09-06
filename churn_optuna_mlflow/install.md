# Installation & Setup Guide .

## 1. Install PostgreSQL (if using as MLflow backend)
```bash
brew install postgresql
brew services start postgresql
```

## 2. Create a database and user for MLflow (optional, for DB backend)
```bash
createdb mlflow_registry

# Enter the psql shell to create a user and grant privileges:
psql postgres

-- In the psql shell, run:
CREATE USER mlflowuser WITH PASSWORD 'mlflowpassword';
GRANT ALL PRIVILEGES ON DATABASE mlflow_registry TO mlflowuser;
\q
```

## 3. Set up Python environment and install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install mlflow optuna scikit-learn xgboost pandas numpy psycopg2-binary
```

## 4. Start the MLflow Tracking Server

### (A) Using the default local file backend:
```bash
mlflow server --host 127.0.0.1 --port 8080
```
- The UI will be available at: [http://127.0.0.1:8080](http://127.0.0.1:8080)

### (B) Using PostgreSQL as backend:
```bash
mlflow server \
    --backend-store-uri postgresql://mlflowuser:mlflowpassword@localhost/mlflow_registry \
    --default-artifact-root ./mlruns \
    --host 127.0.0.1 --port 5000
```
- The UI will be available at: [http://127.0.0.1:5000/#/experiments](http://127.0.0.1:5000/#/experiments)

## 5. Generate synthetic data for experiments
```bash
python generate_raw_data.py
```

## 6. Run hyperparameter optimization and model training
```bash
python optimize.py
```
- This script handles automated hyperparameter tuning and training.

---

## Troubleshooting

- **If you see an error about `libxgboost.dylib` or OpenMP on Mac:**
    ```bash
    brew install libomp
    ```

---

For more details, see the README or open
