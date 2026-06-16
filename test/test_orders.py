from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()


def test_total_orders():

    df = spark.table("silver_orders")

    assert df.count() > 0


def test_order_amount_positive():

    df = spark.table("silver_orders")

    assert df.filter(
        "order_amount <= 0"
    ).count() == 0


def test_order_id_not_null():

    df = spark.table("silver_orders")

    assert df.filter(
        "order_id IS NULL"
    ).count() == 0


def test_customer_id_not_null():

    df = spark.table("silver_orders")

    assert df.filter(
        "customer_id IS NULL"
    ).count() == 0
