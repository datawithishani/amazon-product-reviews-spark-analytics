# Project Outputs

This folder contains screenshots and result outputs generated from the Apache Spark analysis.


## Output Summary

### Data Loading

* Spark session initialized using PySpark.
* Amazon product review CSV loaded with:

  * Header enabled
  * Multi-line CSV support
  * Quote and escape handling
  * Schema inference
* Spark schema and total record count were displayed.

### Data Cleansing

* Columns containing dots were renamed for easier Spark processing:

  * `reviews.rating` → `reviews_rating`
  * `reviews.text` → `reviews_text`
  * `reviews.title` → `reviews_title`
  * `reviews.date` → `reviews_date`
  * `reviews.username` → `reviews_username`
* `primary_category` was extracted from `categories`.
* Ratings were cast to integer.
* Records with missing or invalid ratings outside the 1–5 range were removed.

### Top Products by Average Rating

* Products were grouped by product name.
* Products with at least **20 reviews** were retained.
* Products were ranked by descending average rating.

### Most Active Reviewers

* Reviewers were grouped by username.
* The top 10 reviewers were identified based on review count.

### Monthly Rating Trend by Category

* Review dates were converted into `yyyy-MM` format.
* Average ratings were calculated by primary category and month.
* Results were ordered chronologically.

### 5-Star to 1-Star Review Ratio

* 5-star and 1-star review counts were calculated for each product.
* Products with at least one 1-star review were retained.
* The 5-star/1-star ratio was calculated and ranked in descending order.

### Longest Review per Category

* Review text length was calculated.
* A Spark Window function with `row_number()` was used to identify the longest review in each category.
* Category, review title, review text, and review length were returned.

### Year-over-Year Review Growth

* Reviews were grouped by year.
* `lag()` was used to retrieve the previous year's review count.
* Year-over-year growth percentage was calculated.

### Average Rating by Review Length

Reviews were classified into three buckets:

* **Short:** fewer than 50 characters
* **Medium:** 50–200 characters
* **Long:** more than 200 characters

Average rating was then calculated for each bucket.

### Products with Declining Ratings

* Monthly average ratings were calculated for each product.
* Window functions were used to identify the first and last monthly averages.
* Rating decline was calculated as:

```text
Drop = First Average Rating - Last Average Rating
```

* Products were ordered by the largest decline.

### Declining Product Analysis

The report identifies **Amazon Echo Dot** as a declining product.

**Key finding:**

* Rating declined from **4.8 to 3.9 over 12 months**.
* Review analysis identified complaints related to connectivity and speaker quality.

**Recommendation:**

* Release firmware updates.
* Improve hardware quality.
* Address connectivity stability.

### Performance Optimization

The monthly trend analysis was identified as computationally heavy.

Performance was compared:

1. Before optimization
2. After caching the `trend` DataFrame

Caching was used to avoid repeated computation of the same DataFrame during analysis.

## Key Technologies

* **Apache Spark / PySpark**
* **Spark SQL**
* **Python**
* CSV data processing
* Aggregations
* Window functions
* Caching
* Repartitioning


## Important Spark Techniques Demonstrated

* `SparkSession`
* `spark.read.csv()`
* Schema inference
* `withColumn()`
* `withColumnRenamed()`
* `filter()`
* `groupBy()`
* `agg()`
* `avg()`
* `count()`
* `sum()`
* `when()`
* `to_timestamp()`
* `date_format()`
* `year()`
* `length()`
* `row_number()`
* `lag()`
* Window specifications
* `cache()`
* `repartition()`

## Spark Optimization Techniques
The project used caching and repartitioning to improve Spark performance. 
Caching was applied to the computationally heavy monthly trend DataFrame to avoid repeated recomputation. 
Repartitioning was used to improve data distribution and parallel processing. 
Other relevant Spark optimization practices include filtering data early, 
selecting only required columns, minimizing shuffles, and using broadcast joins for small datasets.

## Reference

The outputs documented here are based on the project report **“Amazon Product Reviews Analysis using Apache Spark.”**
