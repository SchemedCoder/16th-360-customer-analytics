-- ============================================
-- EXECUTIVE KPI DASHBOARD
-- ============================================

SELECT

COUNT(*) total_customers,

SUM(total_spend) total_revenue,

SUM(total_orders) total_orders,

ROUND(
AVG(avg_order_value),
2
) avg_order_value,

SUM(tickets_raised) total_tickets

FROM gold_customer360;

-- ============================================
-- CHURN RISK CUSTOMERS
-- ============================================

SELECT *

FROM gold_customer360

WHERE churn_risk='HIGH';

-- ============================================
-- MOST ACTIVE CUSTOMERS
-- ============================================

SELECT

customer_id,

customer_name,

total_web_visits

FROM gold_customer360

ORDER BY total_web_visits DESC

LIMIT 20;

-- ============================================
-- LONGEST SESSION USERS
-- ============================================

SELECT

customer_id,

customer_name,

avg_session_duration

FROM gold_customer360

ORDER BY avg_session_duration DESC

LIMIT 20;

-- ============================================
-- SUPPORT TICKET ANALYSIS
-- ============================================

SELECT

customer_id,

customer_name,

tickets_raised

FROM gold_customer360

ORDER BY tickets_raised DESC;

-- ============================================
-- REVENUE BY STATE
-- ============================================

SELECT

state,

SUM(total_spend) revenue

FROM gold_customer360

GROUP BY state

ORDER BY revenue DESC;

-- ============================================
-- CUSTOMER ACQUISITION TREND
-- ============================================

SELECT

signup_date,

COUNT(*) customers

FROM gold_customer360

GROUP BY signup_date

ORDER BY signup_date;

-- ============================================
-- CUSTOMER HEALTH SCORE
-- ============================================

SELECT

customer_id,

customer_name,

ROUND(

(
(total_orders * 0.4)
+
(total_web_visits * 0.2)
+
(customer_lifetime_value * 0.4)

),

2

) AS health_score

FROM gold_customer360

ORDER BY health_score DESC;
