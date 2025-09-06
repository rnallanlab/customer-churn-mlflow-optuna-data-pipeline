{{ config(materialized='view') }}

select
    customer_id,
    signup_date,
    is_premium_member
from raw_customers
