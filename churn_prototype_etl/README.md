## Churn Prediction Prototype (Local Mac)

A self-contained, local prototype to predict e-commerce customer churn using pandas and scikit-learn. Includes data generation, feature processing, training, evaluation, batch scoring, and an API for online inference.
---

### Technologies Used

- **Python**: Core programming language for all scripts and logic.
- **pandas**: Data manipulation and analysis.
- **scikit-learn**: Machine learning pipeline, including preprocessing, model training, and evaluation.
- **joblib**: Model serialization and persistence.
- **FastAPI**: Building the REST API for online inference.
- **Uvicorn**: ASGI server to run the FastAPI app.
- **matplotlib**: Generating evaluation charts and visualizations.
---

### Quickstart

For detailed, step-by-step setup and usage instructions, see [instructions.md](./instructions.md).

#### Project Structure

```
churn_prototype/
  data/                     ## input data + batch output
  metrics/                  ## metrics JSON
  models/                   ## trained model artifacts
  reports/                  ## evaluation charts/reports
  src/
    batch/score_batch.py    ## batch inference
    data/generate_data.py   ## synthetic dataset generator
    features/build_features.py  ## (simple) feature cleanup (not strictly required)
    models/train.py         ## train & save pipeline
    models/evaluate.py      ## evaluate and emit artifacts
    serve/app.py            ## FastAPI app for online inference
  requirements.txt
  README.md
  instructions.md
```

---

### Notes
- We are using LogisticRegression with two hyper-parameters(class_weight & max_iter), we can use MLFlow other other fine-tuning frameworks to run with different (range) of values, automate process and publish to MLFlow.
- The scikit-learn **Pipeline** includes preprocessing (scaling + one-hot encoding) and the classifier, so serving and batch scoring are simple.
- You can swap the model for GradientBoosting, XGBoost, LightGBM, or even Keras if you install those packages and adjust `train.py`.
- The synthetic data is generated via a transparent function so you can tweak churn drivers and class balance easily.

---
Hyperparameters used in LogisticRegression
---
max_iter=200
Sets the maximum number of iterations for the solver to converge. If the model does not converge within 200 iterations, it will stop and may raise a warning. This is useful for ensuring the optimization process completes in a reasonable time.

class_weight="balanced"
Automatically adjusts weights inversely proportional to class frequencies in the data. This helps the model handle imbalanced datasets by giving more importance to the minority class, improving performance on rare outcomes (like churn).
---
For any questions or issues, please refer to the [instructions.md](./instructions.md)
