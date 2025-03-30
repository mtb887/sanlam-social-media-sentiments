from pyspark.sql import SparkSession
import sqlite3

spark = SparkSession.builder.appName("ExportResults").getOrCreate()
df = spark.read.parquet("storage/aggregated/")

df.toPandas().to_csv("storage/aggregated/sentiment_summary.csv", index=False)
conn = sqlite3.connect("storage/aggregated/sentiment.db")
df.toPandas().to_sql("sentiment", conn, if_exists="replace", index=False)