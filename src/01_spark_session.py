from pyspark.sql import SparkSession


def create_spark_session():
    spark = SparkSession.builder \
        .appName("AmazonProductReviewsAnalytics") \
        .getOrCreate()

    return spark
