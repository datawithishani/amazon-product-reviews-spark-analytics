from pyspark.sql.functions import split, col

# Create primary category column
from pyspark.sql.functions import trim

df_clean = df.withColumn(
    "primary_category",
    trim(split(col("categories"), ",").getItem(0))
)

# Convert rating to integer
df_clean = df_clean.withColumn("reviews_rating_int", col("reviews_rating").cast("int"))

# Keep only valid ratings 1 to 5
df_clean = df_clean.filter(
    (col("reviews_rating_int").isNotNull()) &
    (col("reviews_rating_int") >= 1) &
    (col("reviews_rating_int") <= 5)
)

df_clean.printSchema()

print("Records after cleaning:", df_clean.count())
