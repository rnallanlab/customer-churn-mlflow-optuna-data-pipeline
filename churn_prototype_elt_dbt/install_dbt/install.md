psql -U macuser -d postgres
CREATE ROLE postgres WITH LOGIN SUPERUSER PASSWORD 'mypassword';
CREATE DATABASE churn_elt OWNER postgres;
