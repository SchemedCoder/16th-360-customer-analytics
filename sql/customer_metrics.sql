-- ============================================
-- TOTAL CUSTOMERS
-- ============================================

SELECT
COUNT(*) AS total_customers
FROM gold_customer360;

-- ============================================
-- TOTAL REVENUE
-- ============================================

SELECT
SUM(total_spend) AS total_revenue
FROM gold_customer360;

-- ============================================
-- AVG ORDER VALUE
-- ============================================

SELECT
ROUND(
AVG(avg_order_value),
2
) AS average_order_value
FROM gold_customer360;

-- ============================================
-- TOTAL ORDERS
-- ============================================

SELECT
SUM(total_orders) AS total_orders
FROM gold_customer360;

-- ============================================
-- TOP 10 CUSTOMERS
-- ============================================

SELECT *

FROM gold_customer360

ORDER BY total_spend DESC

LIMIT 10;

-- ============================================
-- TOP 10 CITIES BY REVENUE
-- ============================================

SELECT

city,

SUM(total_spend) revenue

FROM gold_customer360

GROUP BY city

ORDER BY revenue DESC;

-- ============================================
-- COUNTRY REVENUE
-- ============================================

SELECT

country,

SUM(total_spend) revenue

FROM gold_customer360

GROUP BY country

ORDER BY revenue DESC;

-- ============================================
-- CUSTOMER LIFETIME VALUE
-- ============================================

SELECT

customer_id,

customer_name,

customer_lifetime_value

FROM gold_customer360

ORDER BY customer_lifetime_value DESC;
