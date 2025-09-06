Scenario: An e-commerce company wants to predict customer churn.

Raw tables (raw.customers, raw.orders) are loaded into a warehouse (here we’ll simulate a Postgres database locally).

dbt transforms raw data → staging → marts → feature table ready for ML.

ML model (scikit-learn / optionally Keras) is trained on the ELT output.

