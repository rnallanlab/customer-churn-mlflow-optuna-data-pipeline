{{ config(materialized='table') }}

with orders_agg as (
    select
        customer_id,
        count(*) as total_orders,
        sum(net_amount) as total_revenue,
        max(order_date) as last_order_date
    from {{ ref('stg_orders') }}
    group by customer_id
)

select
    c.customer_id,
    c.is_premium_member,
    o.total_orders,
    o.total_revenue,
    -- Subtracting dates gives integer days in Postgres
    (current_date - coalesce(o.last_order_date::date, current_date)) as days_since_last_order,
    case 
        when (current_date - coalesce(o.last_order_date::date, current_date)) > 90 then 1 
        else 0 
    end as churned
from {{ ref('stg_customers') }} c
left join orders_agg o on c.customer_id = o.customer_id