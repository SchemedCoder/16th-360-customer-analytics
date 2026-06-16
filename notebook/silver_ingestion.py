# =====================================================
# CUSTOMER 360 ANALYTICS PLATFORM
# SILVER TRANSFORMATION NOTEBOOK
# MICROSOFT FABRIC
# =====================================================

from pyspark.sql.functions import *
from pyspark.sql.types import *

# =====================================================
# LOAD BRONZE TABLES
# =====================================================

customers_df = spark.table("bronze_customers")

orders_df = spark.table("bronze_orders")

tickets_df = spark.table("bronze_support_tickets")

activity_df = spark.table("bronze_web_activity")

# =====================================================
# CUSTOMERS SILVER
# =====================================================

silver_customers = (

    customers_df

    .dropDuplicates(["customer_id"])

    .withColumn(
        "customer_name",
        initcap(trim(col("customer_name")))
    )

    .withColumn(
        "email",
        lower(trim(col("email")))
    )

    .withColumn(
        "city",
        initcap(trim(col("city")))
    )

    .withColumn(
        "state",
        initcap(trim(col("state")))
    )

    .withColumn(
        "country",
        upper(trim(col("country")))
    )

    .withColumn(
        "signup_date",
        to_date(col("signup_date"))
    )

    .filter(
        col("customer_id").isNotNull()
    )
)

# =====================================================
# ORDERS SILVER
# =====================================================

silver_orders = (

    orders_df

    .dropDuplicates(["order_id"])

    .withColumn(
        "order_date",
        to_date(col("order_date"))
    )

    .withColumn(
        "product_name",
        initcap(trim(col("product_name")))
    )

    .withColumn(
        "category",
        initcap(trim(col("category")))
    )

    .withColumn(
        "quantity",
        col("quantity").cast("int")
    )

    .withColumn(
        "unit_price",
        col("unit_price").cast("double")
    )

    .withColumn(
        "order_amount",
        col("order_amount").cast("double")
    )

    .filter(
        col("order_amount") > 0
    )
)

# =====================================================
# SUPPORT TICKETS SILVER
# =====================================================

silver_tickets = (

    tickets_df

    .dropDuplicates(["ticket_id"])

    .withColumn(
        "ticket_date",
        to_date(col("ticket_date"))
    )

    .withColumn(
        "category",
        initcap(trim(col("category")))
    )

    .withColumn(
        "priority",
        upper(trim(col("priority")))
    )

    .withColumn(
        "status",
        upper(trim(col("status")))
    )
)

# =====================================================
# WEB ACTIVITY SILVER
# =====================================================

silver_activity = (

    activity_df

    .dropDuplicates(["activity_id"])

    .withColumn(
        "activity_date",
        to_date(col("activity_date"))
    )

    .withColumn(
        "page_name",
        upper(trim(col("page_name")))
    )

    .withColumn(
        "device_type",
        upper(trim(col("device_type")))
    )

    .withColumn(
        "session_duration_seconds",
        col("session_duration_seconds").cast("int")
    )

    .filter(
        col("session_duration_seconds") > 0
    )
)

# =====================================================
# WRITE SILVER TABLES
# =====================================================

silver_customers.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("silver_customers")

silver_orders.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("silver_orders")

silver_tickets.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("silver_support_tickets")

silver_activity.write \
    .mode("overwrite") \
    .format("delta") \
    .saveAsTable("silver_web_activity")

# =====================================================
# DATA QUALITY CHECKS
# =====================================================

print("Customers")

print(silver_customers.count())

print("Orders")

print(silver_orders.count())

print("Tickets")

print(silver_tickets.count())

print("Web Activity")

print(silver_activity.count())

# =====================================================
# NULL CHECKS
# =====================================================

print("Customer Null IDs")

print(

    silver_customers.filter(
        col("customer_id").isNull()
    ).count()

)

print("Order Null IDs")

print(

    silver_orders.filter(
        col("order_id").isNull()
    ).count()

)

# =====================================================
# VERIFY TABLES
# =====================================================

spark.sql("""

SELECT COUNT(*)

FROM silver_customers

""").show()

spark.sql("""

SELECT COUNT(*)

FROM silver_orders

""").show()

spark.sql("""

SELECT COUNT(*)

FROM silver_support_tickets

""").show()

spark.sql("""

SELECT COUNT(*)

FROM silver_web_activity

""").show()

print("Silver Layer Created Successfully")
