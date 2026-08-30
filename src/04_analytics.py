from pyspark.sql.functions import col, avg, count


def get_top_products(df):

    return df.groupBy("name") \
        .agg(
            avg("reviews_rating_int").alias("avg_rating"),
            count("reviews_rating_int").alias("review_count")
        ) \
        .filter(col("review_count") >= 20) \
        .orderBy(col("avg_rating").desc())
