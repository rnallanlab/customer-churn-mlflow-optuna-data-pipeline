## churn_optuna_mlflow

This project implements a reproducible machine learning pipeline for customer churn prediction, with a focus on automated hyperparameter optimization and experiment tracking.

**Key features:**
- **Synthetic Data Generation:** Scripts to generate realistic customer and order data for churn modeling.
- **Model Training:** Train a machine learning model (e.g., XGBoost) on the generated data.
- **Hyperparameter Optimization:** Use Optuna to automatically search for the best hyperparameters by running multiple training trials.
- **Experiment Tracking:** Use MLflow to log parameters, metrics, and artifacts for every training run, making it easy to compare and reproduce results.
- **Model Selection:** Automatically identify and select the best-performing model based on evaluation metrics.
- **Visualization:** Use the MLflow UI to visualize experiments, compare runs, and inspect model details.

This pipeline enables robust experimentation and model selection for churn prediction tasks, making it easy to track, compare, and deploy the best models.
---
## churn_prototype_elt_dbt
The churn_prototype_elt_dbt project describes a pipeline for 
-  generating data & load, 
-  transforming it with dbt, 
-  training a model.
---
## churn_prototype_etl
The churn_prototype_etl project (as shown in the README.md) uses scikit-learn for 
- training and evaluation, and - provides scripts for training, evaluating, batch scoring, and serving the model via FastAPI.
---