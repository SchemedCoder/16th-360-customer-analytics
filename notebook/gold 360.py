# =====================================================
# CUSTOMER 360 ANALYTICS PLATFORM
# GOLD CUSTOMER 360 NOTEBOOK
# MICROSOFT FABRIC
# =====================================================

from pyspark.sql.functions import *

# =====================================================
# LOAD SILVER TABLES
# =====================================================

customers_df = spark.table("silver_customers")

orders_df = spark.table("silver_orders")

tickets_df = spark.table("silver_support_tickets")

activity_df = spark.table("silver_web_activity")

# =====================================================
# ORDER METRICS
# =====================================================

order_metrics = (

    orders_df

    .groupBy("customer_id")

    .agg(

        countDistinct("order_id")
        .alias("total_orders"),

        sum("order_amount")
        .alias("total_spend"),

        avg("order_amount")
        .alias("avg_order_value"),

        max("order_date")
        .alias("last_order_date")

    )

)

# =====================================================
# SUPPORT METRICS
# =====================================================

ticket_metrics = (

    tickets_df

    .groupBy("customer_id")

    .agg(

        count("ticket_id")
        .alias("tickets_raised")

    )

)

# =====================================================
# WEB ACTIVITY METRICS
# =====================================================

activity_metrics = (

    activity_df

    .groupBy("customer_id")

    .agg(

        max("activity_date")
        .alias("last_activity_date"),

        count("activity_id")
        .alias("total_web_visits"),

        avg("session_duration_seconds")
        .alias("avg_session_duration")

    )

)

# =====================================================
# CUSTOMER 360 TABLE
# =====================================================

gold_customer360 = (

    customers_df

    .join(
        order_metrics,
        "customer_id",
        "left"
    )

    .join(
        ticket_metrics,
        "customer_id",
        "left"
    )

    .join(
        activity_metrics,
        "customer_id",
        "left"
    )

)

# =====================================================
# HANDLE NULLS
# =====================================================

gold_customer360 = (

    gold_customer360

    .fillna(
        {
            "total_orders": 0,
            "total_spend": 0,
            "avg_order_value": 0,
            "tickets_raised": 0,
            "total_web_visits": 0,
            "avg_session_duration": 0
        }
    )

)

# =====================================================
# CUSTOMER SEGMENTATION
# =====================================================

gold_customer360 = (

    gold_customer360

    .withColumn(

        "customer_segment",

        when(
            col("total_spend") >= 100000,
            "PLATINUM"
        )

        .when(
            col("total_spend") >= 50000,
            "GOLD"
        )

        .when(
            col("total_spend") >= 10000,
            "SILVER"
        )

        .otherwise("BRONZE")

    )

)

# =====================================================
# CUSTOMER LIFETIME VALUE
# =====================================================

gold_customer360 = (

    gold_customer360

    .withColumn(

        "customer_lifetime_value",

        round(
            col("total_spend") * 1.2,
            2
        )

    )

)

# =====================================================
# CHURN FLAG
# =====================================================

gold_customer360 = (

    gold_customer360

    .withColumn(

        "churn_risk",

        when(

            datediff(
                current_date(),
                col("last_activity_date")
            ) > 90,

            "HIGH"

        )

        .otherwise("LOW")

    )

)

# =====================================================
# WRITE GOLD TABLE
# =====================================================

gold_customer360.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("gold_customer360")

# =====================================================
# VALIDATION
# =====================================================

print("Customer 360 Records")

print(

    gold_customer360.count()

)

# =====================================================
# TOP CUSTOMERS
# =====================================================

gold_customer360.orderBy(

    desc("total_spend")

).show(10)

# =====================================================
# SEGMENT DISTRIBUTION
# =====================================================

gold_customer360.groupBy(

    "customer_segment"

).count().show()

# =====================================================
# CHURN DISTRIBUTION
# =====================================================

gold_customer360.groupBy(

    "churn_risk"

).count().show()

# =====================================================
# SQL VALIDATION
# =====================================================

spark.sql("""

SELECT COUNT(*)

FROM gold_customer360

""").show()

print("Gold Layer Created Successfully")
