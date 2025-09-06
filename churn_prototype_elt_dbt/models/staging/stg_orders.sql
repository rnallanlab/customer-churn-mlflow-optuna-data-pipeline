{{ config(materialized='view') }}

select
    order_id,
    customer_id,
    order_date,
    case when status='paid' then amount else 0 end as net_amount
from raw_orders
