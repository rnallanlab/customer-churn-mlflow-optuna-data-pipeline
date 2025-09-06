from mlflow.tracking import MlflowClient

client = MlflowClient()

# Create the registered model
client.create_registered_model("model-10-trial")

# Register the artifact from a run
client.create_model_version(
    name="model-10-trial",
    source=f"runs:/7c4942e0dce94ab39e4fe48f5b5af5cc/model",
    run_id=run_id
)
