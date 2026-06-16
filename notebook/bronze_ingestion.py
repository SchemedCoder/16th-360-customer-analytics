# =====================================================
# CUSTOMER 360 ANALYTICS PLATFORM
# BRONZE INGESTION NOTEBOOK
# MICROSOFT FABRIC
# =====================================================

from pyspark.sql import SparkSession

# =====================================================
# READ CUSTOMERS
# =====================================================

customers_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("Files/data/customers.csv")

# =====================================================
# READ ORDERS
# =====================================================

orders_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("Files/data/orders.csv")

# =====================================================
# READ SUPPORT TICKETS
# =====================================================

tickets_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("Files/data/support_tickets.csv")

# =====================================================
# READ WEB ACTIVITY
# =====================================================

activity_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("Files/data/web_activity.csv")

# =====================================================
# DATA VALIDATION
# =====================================================

print("Customers Count")

print(customers_df.count())

print("Orders Count")

print(orders_df.count())

print("Tickets Count")

print(tickets_df.count())

print("Web Activity Count")

print(activity_df.count())

# =====================================================
# WRITE BRONZE TABLES
# =====================================================

customers_df.write.mode("overwrite") \
    .format("delta") \
    .saveAsTable("bronze_customers")

orders_df.write.mode("overwrite") \
    .format("delta") \
    .saveAsTable("bronze_orders")

tickets_df.write.mode("overwrite") \
    .format("delta") \
    .saveAsTable("bronze_support_tickets")

activity_df.write.mode("overwrite") \
    .format("delta") \
    .saveAsTable("bronze_web_activity")

# =====================================================
# VERIFY TABLES
# =====================================================

spark.sql("""

SELECT COUNT(*)

FROM bronze_customers

""").show()

spark.sql("""

SELECT COUNT(*)

FROM bronze_orders

""").show()

spark.sql("""

SELECT COUNT(*)

FROM bronze_support_tickets

""").show()

spark.sql("""

SELECT COUNT(*)

FROM bronze_web_activity

""").show()

print("Bronze Layer Load Completed Successfully")
