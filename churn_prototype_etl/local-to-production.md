## 1. Data Ingestion & Storage
- Data Sources: Transaction DBs (Postgres, MySQL), clickstream, CRM, support tickets, etc.
- ETL / ELT tools:
Airflow, Prefect (workflow orchestration)
dbt (transformations in data warehouses)
Fivetran / Informatica / Talend (managed ingestion)
- Storage / Lakehouse:
Data Lake: S3, GCS, Azure Data Lake
Data Warehouse: Snowflake, BigQuery, Redshift
Lakehouse: Databricks, Apache Iceberg, Delta Lake
## 2. Feature Engineering

- Pandas → Scalable versions:
Spark / PySpark (distributed tabular processing)
Dask / Ray (parallel Python dataframes)
- Feature Stores (to reuse features across models & teams):
Feast
Tecton
Databricks Feature Store
## 3. Model Development (your prototype stage)
- Notebooks: Jupyter, VS Code, Databricks notebooks, SageMaker notebooks
- ML Libraries:
Scikit-learn for classic ML
TensorFlow/Keras, PyTorch for deep learning
XGBoost, LightGBM, CatBoost for tabular data (often outperform deep nets here)
## 4. Experiment Tracking & Versioning
- MLflow (open source, widely used)
- Weights & Biases (W&B)
- Neptune.ai
These tools help log experiments, metrics, models, and hyperparameters.
## 5. Model Training at Scale
- Single-node: Sklearn, Keras locally
- Distributed Training:
TensorFlow distributed strategy
PyTorch Lightning / HuggingFace Accelerate
Spark MLlib (for some cases)
- Cloud Training Platforms:
AWS SageMaker
GCP Vertex AI
Azure ML
## 6. Model Serving & Deployment
- Batch scoring: Spark jobs, Airflow DAGs writing predictions back to DBs
- Real-time APIs:
FastAPI, Flask → containerized with Docker, deployed with Kubernetes
BentoML, KFServing (KServe), Seldon Core for production ML serving
- Model Registry:
MLflow Model Registry
SageMaker Model Registry
Databricks MLflow integration

## 7. CI/CD & MLOps
- CI/CD pipelines:
GitHub Actions, GitLab CI, Jenkins, Azure DevOps
- MLOps frameworks:
Kubeflow
MLflow
TFX (TensorFlow Extended)
Flyte
These handle model retraining, validation, deployment automation.
## 8. Monitoring & Feedback Loop
- Data drift detection (is data distribution changing?)
- Model drift monitoring (is accuracy degrading?)
-  Tools:
Evidently AI
Arize AI
Fiddler AI
WhyLabs

## Example: Customer Churn Prediction @ Scale
- Data: Transaction data ingested nightly into Snowflake.
- Orchestration: Airflow DAG runs dbt jobs → creates clean tables.
- Feature Store: Customer tenure, activity, support calls stored in Feast.
- Modeling: Data scientist trains churn model in Databricks (XGBoost + Keras variant).
- Experiment Tracking: MLflow logs all runs.
- Deployment: Model registered in MLflow Registry → automatically deployed as an API on Kubernetes via KServe.
- Monitoring: Evidently AI monitors prediction drift; retraining triggered if drift > threshold.