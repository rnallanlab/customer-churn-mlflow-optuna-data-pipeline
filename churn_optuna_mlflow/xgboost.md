We used **`XGBClassifier`** because it’s a very effective and widely adopted algorithm for **tabular classification problems** like churn prediction. Let me break down why, step by step:

---

### 1 Nature of the problem

* Your problem is **binary classification**: `churned = 1` or `0`.
* The dataset is tabular (features like `total_orders`, `avg_order_value`, `days_since_last_order`, etc.), not images or text.

---

### 2 Why XGBoost specifically

* **Gradient boosting algorithm**: combines many weak learners (decision trees) into a strong model.
* **Handles non-linear relationships well**: Unlike logistic regression, it can capture complex interactions between features.
* **Built-in handling for missing values**: avoids needing extensive imputation.
* **Robust to feature scaling**: tree-based, so you don’t need to normalize numeric features.
* **Fast & scalable**: optimized C++ implementation with multi-threading.

---

### 3 Comparison with alternatives

| Model              | When to use                             | Pros                                                         | Cons                                           |
| ------------------ | --------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| LogisticRegression | Simple, interpretable                   | Very fast, easy to explain to business                       | Struggles with non-linear relationships        |
| RandomForest       | Tabular data, robust                    | Handles non-linearity, less hyperparameter tuning            | Can be slower for large datasets               |
| XGBoost            | Tabular data, non-linear, moderate size | High accuracy, handles missing data, supports regularization | More hyperparameters to tune, slightly complex |

**In short:** XGBoost is often a **go-to choice for structured, tabular data**, especially when you want good predictive performance without overly complex neural networks.

---

### 4️Connection to our pipeline

* We can plug **`XGBClassifier`** directly into:

  * **Optuna** for hyperparameter tuning (`n_estimators`, `max_depth`, `learning_rate`, etc.)
  * **MLflow** for experiment tracking and leaderboard visualization
* Works well even with **hundreds of features** and **moderate datasets**, like our synthetic churn dataset.

---

