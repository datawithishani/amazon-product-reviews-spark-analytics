df = df.withColumnRenamed("reviews.rating", "reviews_rating") \
       .withColumnRenamed("reviews.text", "reviews_text") \
       .withColumnRenamed("reviews.title", "reviews_title") \
       .withColumnRenamed("reviews.date", "reviews_date") \
       .withColumnRenamed("reviews.username", "reviews_username")

print("Columns Renamed Successfully")
df.printSchema()
