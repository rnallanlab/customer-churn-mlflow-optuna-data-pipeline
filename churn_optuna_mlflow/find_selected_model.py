import mlflow
from mlflow.tracking import MlflowClient

client = MlflowClient()

# Get the registered model
model_name = "model-10-trial"
versions = client.get_latest_versions(model_name)

# Pick a version (e.g., version 1)
version = versions[0]

# Source run ID
run_id = version.run_id
print("Source Run ID:", run_id)

# Get metrics and params from that run
run = client.get_run(run_id)
print("Params:", run.data.params)
print("Metrics:", run.data.metrics)
