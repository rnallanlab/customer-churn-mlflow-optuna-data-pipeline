import optuna
import mlflow
from train import train_and_log

mlflow.set_tracking_uri("http://127.0.0.1:5000")  # if running MLflow UI locally
mlflow.set_experiment("Churn Prediction - Optuna")


def objective(trial):
    params = {
        "n_estimators": trial.suggest_int("n_estimators", 50, 60),
        "max_depth": trial.suggest_int("max_depth", 3, 5),
        "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.3, log=True),
        "subsample": trial.suggest_float("subsample", 0.5, 1.0),
        "colsample_bytree": trial.suggest_float("colsample_bytree", 0.5, 1.0),
    }
    acc, f1 = train_and_log(params, run_name=f"optuna_trial_{trial.number}")
    # Optimize for F1 (or accuracy depending on your preference)
    return f1


if __name__ == "__main__":
    study = optuna.create_study(direction="maximize")
    study.optimize(objective, n_trials=20)

    print("Best Trial:", study.best_trial.params)
