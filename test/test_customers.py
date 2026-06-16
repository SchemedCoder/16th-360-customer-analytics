from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()


def test_customer_count():

    df = spark.table("gold_customer360")

    assert df.count() > 0


def test_customer_ids_not_null():

    df = spark.table("gold_customer360")

    assert df.filter(
        "customer_id IS NULL"
    ).count() == 0


def test_unique_customers():

    df = spark.table("gold_customer360")

    total = df.count()

    unique = df.select(
        "customer_id"
    ).distinct().count()

    assert total == unique


def test_customer_segment_exists():

    df = spark.table("gold_customer360")

    assert df.filter(
        "customer_segment IS NULL"
    ).count() == 0
