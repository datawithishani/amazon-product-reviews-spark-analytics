from pyspark.sql.functions import split, col, trim


def clean_data(df):

    df = df.withColumnRenamed(
        "reviews.rating", "reviews_rating"
    ).withColumnRenamed(
        "reviews.text", "reviews_text"
    ).withColumnRenamed(
        "reviews.title", "reviews_title"
    ).withColumnRenamed(
        "reviews.date", "reviews_date"
    ).withColumnRenamed(
        "reviews.username", "reviews_username"
    )

    df_clean = df.withColumn(
        "primary_category",
        trim(split(col("categories"), ",").getItem(0))
    )

    df_clean = df_clean.withColumn(
        "reviews_rating_int",
        col("reviews_rating").cast("int")
    )

    df_clean = df_clean.filter(
        (col("reviews_rating_int").isNotNull()) &
        (col("reviews_rating_int") >= 1) &
        (col("reviews_rating_int") <= 5)
    )

    return df_clean
