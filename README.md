# amazon-product-reviews-spark-analytics
Large-scale Amazon Product Reviews analysis using Apache Spark and PySpark, featuring data cleansing, distributed analytics, window functions, time-series analysis, and Spark performance optimization.
# Amazon Product Reviews Analytics using Apache Spark

## 📌 Project Overview

This project demonstrates large-scale data processing and analysis using **Apache Spark and PySpark** on the Amazon Product Reviews dataset.

The project covers the complete data analytics workflow, including data ingestion, schema inference, data cleansing, transformation, aggregation, Spark SQL operations, window functions, time-series analysis, and performance optimization.

The objective is to derive meaningful insights from customer reviews, product ratings, reviewer activity, category-level trends, and changes in product ratings over time.

We had finished this project as a part of our Big Data Analytics Curriculum; while playing with Apache Spark. 

---

## 🛠️ Technologies Used

* Python
* Apache Spark
* PySpark
* Spark SQL
* Window Functions
* Google Colab / Jupyter Notebook

---

## 📂 Dataset

The project uses the **Amazon Product Reviews Dataset**.

The primary columns used for analysis are:

| Column           | Description              |
| ---------------- | ------------------------ |
| categories       | Product categories       |
| name             | Product name             |
| reviews.date     | Date of review           |
| reviews.rating   | Rating given by reviewer |
| reviews.text     | Full review text         |
| reviews.title    | Review title             |
| reviews.username | Reviewer username        |

---

## 🔄 Project Workflow

### 1. Data Loading

The dataset is loaded into Apache Spark using appropriate CSV parsing options.

The dataset contains:

* Multi-line reviews
* Commas inside review text
* Embedded quotes

Therefore, appropriate Spark options such as `multiLine`, `quote`, and `escape` are used during ingestion.

---

### 2. Data Cleansing and Transformation

The following transformations are performed:

* Renamed columns containing dots for easier processing.
* Created a new column called `primary_category`.
* Extracted the first category from the `categories` column.
* Converted review ratings into integer format.
* Removed records with missing ratings.
* Removed ratings outside the valid range of 1 to 5.

---

## 📊 Analytical Approach

### 1. Data Loading

Loaded the Amazon Product Reviews dataset into Apache Spark and displayed:

* Dataset schema
* Total number of records

### 2: Data Cleansing

Performed schema modifications and data cleansing operations.

### 3: Top Products by Average Rating

Identified products having at least 20 reviews and ranked them based on their average rating.

### 4: Most Active Reviewers

Identified the top 10 reviewers based on the number of reviews submitted.

### 5: Monthly Trend of Average Ratings

Analyzed how average ratings evolve over time across product categories.

### 6: Ratio of 5-Star to 1-Star Reviews

Identified products that are highly loved while receiving relatively fewer negative reviews.

### 7: Longest Review Text per Category

Identified the longest review for each primary product category.

### 8: Year-over-Year Growth in Review Volume

Analyzed changes in review volume across different years.

### 9: Average Rating by Review Length

Classified reviews into three categories:

* Short: Less than 50 characters
* Medium: Between 50 and 200 characters
* Long: More than 200 characters

The average rating was calculated for each category.

### 10: Products with Declining Ratings

Identified products whose monthly average ratings dropped the most over time.

### 11: Declining Product Analysis

Performed a data-driven analysis of a selected product with declining ratings and provided recommendations.

### 12: Performance Optimization

Identified a performance bottleneck in the Spark job and implemented optimization techniques.

Caching was used to reduce recomputation and improve execution performance.

---

## ⚡ Performance Optimization

The monthly rating trend analysis was identified as a computationally intensive operation.

The following optimization technique was implemented:

* Spark DataFrame caching

Execution times were compared before and after optimization to evaluate the impact on performance.

---

## 📁 Project Structure

```text
amazon-product-reviews-spark-analytics/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebooks/
│   └── Amazon_Product_Reviews_Analysis.ipynb
│
├── src/
│   ├── data_loading.py
│   ├── data_cleaning.py
│   ├── analytics.py
│   └── performance_optimization.py
│
├── data/
│   └── README.md
│
└── outputs/
    └── README.md
```

---

## 🚀 How to Run the Project

### Clone the repository

```bash
git clone <your-repository-url>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/Amazon_Product_Reviews_Analysis.ipynb
```

---

## 🎯 Key Spark Concepts Demonstrated

* Distributed Data Processing
* DataFrame API
* Schema Inference
* Data Cleansing
* Aggregations
* Filtering
* Spark SQL Functions
* Window Functions
* Time-Series Analysis
* Performance Optimization
* Data Caching

---

## 👩‍💻 Author

**Ishani Joardar**

Data Engineering | Cloud | Apache Spark | PySpark | Microsoft Fabric
