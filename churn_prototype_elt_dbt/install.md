##  Pre-req: Install database & create user
##  install postgress dbt-progress
```
brew install postgresql
brew install dbt-postgres   ##  for Postgres
```
##  Start datbase & setup user:
```
brew services start postgresql@14
psql -d postgres -U $(whoami)
-- Create the database
CREATE DATABASE customer;

-- Create the user with password
CREATE USER churnuser WITH PASSWORD 'churnpassword';

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON DATABASE customer TO churnuser;
```

###  Python packages
```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install pandas scikit-learn sqlalchemy psycopg2-binary dbt-postgres
```
###  Gemerate Synthetic Data - Generates customers.csv and orders.csv 
```
python src/generate_raw_data.py 
``` 

###  Load it into Database - write to raw_customers and raw_order tables in DB.
```
python load_data.py 
```

###  Run dbt
```
dbt debug         ##  check connection
dbt run           ##  build models - This will execute all sqls under models(from dbt_project.yml) : Under analytics schema (from dbt_project.yml), it will create table churn_features, and views: stg_customers and stg_orders (as defined in sql files) 
dbt test          ##  run any tests you add 
dbt docs generate
dbt docs serve     ##  optional: visualize lineage
```
###  Train ML Model - Utilizes analytics.churn_features table  for training the model.
```
python src/train.py 
```
