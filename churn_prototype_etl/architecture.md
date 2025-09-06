## Pipeline Dependency Diagram

Below is a diagram showing the dependencies and flow between the main stages of the churn_prototype pipeline:

```mermaid
flowchart TD
    A[Data Generation<br>(generate_data.py)] --> B[Model Training<br>(train.py)]
    B --> C[Model Evaluation<br>(evaluate.py)]
    B --> D[Batch Scoring<br>(score_batch.py)]
    B --> E[Model Serving<br>(serve/app.py via FastAPI)]
    C --> F[Reports & Metrics<br>(reports/, metrics/)]
    D --> G[Predictions Output<br>(CSV)]
    E --> H[REST API<br>(/predict endpoint)]

    subgraph Artifacts
        B1[model.joblib]
        B2[metrics.json]
    end

    B --> B1
    B --> B2
    C --> F
    D --> G
    E --> H
```

### Explanation

- **Data Generation:** Synthetic data is created and saved as a CSV.
- **Model Training:** Reads the data, preprocesses it, trains the model, and saves both the model (`model.joblib`) and metrics (`metrics.json`).
- **Model Evaluation:** Loads the trained model and data, evaluates performance, and writes reports (e.g., confusion matrix, classification report).
- **Batch Scoring:** Loads the model and applies it to new data in bulk, outputting predictions as a CSV.
- **Model Serving:** Loads the model and exposes it via a REST API for real-time predictions.
- **Artifacts:** The trained model and metrics are central outputs used by multiple downstream stages.

This diagram helps visualize how each stage depends on the outputs of the previous stage, ensuring a clear, reproducible workflow.

## Importance of Feature Engineering

Feature engineering is a critical step in the churn_prototype workflow. It involves creating, selecting, and transforming raw data features to improve model performance and interpretability. In this project:

- **Why Feature Engineering Matters:**
  - Good features help the model capture important patterns related to customer churn, leading to better predictions.
  - Poor or missing features can limit model accuracy, regardless of the algorithm used.
- **What We Did:**
  - Identified key numeric and categorical features (e.g., tenure, order history, region, preferred channel) that influence churn.
  - Applied scaling to numeric features and one-hot encoding to categorical features using a `ColumnTransformer`.
  - Ensured all preprocessing steps are included in the pipeline, so the same transformations are applied during both training and inference.
- **Impact:**
  - Well-engineered features improved the model’s ability to distinguish between churned and non-churned customers.
  - The pipeline design makes feature engineering reproducible and easy to update as new data or business insights become available.

Feature engineering is often the most important factor in achieving high model performance, and its careful design is a key strength of this project.