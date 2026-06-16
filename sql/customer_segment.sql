-- ============================================
-- CUSTOMER SEGMENT DISTRIBUTION
-- ============================================

SELECT

customer_segment,

COUNT(*) total_customers

FROM gold_customer360

GROUP BY customer_segment

ORDER BY total_customers DESC;

-- ============================================
-- REVENUE BY SEGMENT
-- ============================================

SELECT

customer_segment,

SUM(total_spend) revenue

FROM gold_customer360

GROUP BY customer_segment

ORDER BY revenue DESC;

-- ============================================
-- AVG SPEND BY SEGMENT
-- ============================================

SELECT

customer_segment,

ROUND(
AVG(total_spend),
2
) avg_spend

FROM gold_customer360

GROUP BY customer_segment;

-- ============================================
-- PLATINUM CUSTOMERS
-- ============================================

SELECT *

FROM gold_customer360

WHERE customer_segment='PLATINUM';

-- ============================================
-- GOLD CUSTOMERS
-- ============================================

SELECT *

FROM gold_customer360

WHERE customer_segment='GOLD';

-- ============================================
-- SILVER CUSTOMERS
-- ============================================

SELECT *

FROM gold_customer360

WHERE customer_segment='SILVER';

-- ============================================
-- BRONZE CUSTOMERS
-- ============================================

SELECT *

FROM gold_customer360

WHERE customer_segment='BRONZE';
