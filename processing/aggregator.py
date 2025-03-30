from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, avg

spark = SparkSession.builder.appName("SentimentAggregator").getOrCreate()
df = spark.read.parquet("storage/output/")
df = df.withColumn("date", to_date("timestamp"))
agg = df.groupBy("platform", "date").agg(avg("sentiment").alias("avg_sentiment"))
agg.write.mode("overwrite").parquet("storage/aggregated/")