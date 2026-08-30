def load_data(spark, file_path):

    df = spark.read \
        .option("header", "true") \
        .option("multiLine", "true") \
        .option("escape", "\"") \
        .option("quote", "\"") \
        .option("inferSchema", "true") \
        .csv(file_path)

    return df
