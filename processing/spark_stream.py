from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, lit, udf
from pyspark.sql.types import StructType, StructField, StringType
from textblob import TextBlob
from functools import reduce

spark = SparkSession.builder.appName("SocialSentimentStream").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

schema = StructType([StructField("text", StringType(), True)])

def analyze(text):
    return TextBlob(text).sentiment.polarity if text else 0.0

platforms = {
    "facebook": "facebook-stream",
    "twitter": "twitter-stream",
    "instagram": "instagram-stream",
    "linkedin": "linkedin-stream"
}

dfs = []
for name, topic in platforms.items():
    stream = spark.readStream.format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", topic) \
        .option("startingOffsets", "latest") \
        .load()

    parsed = stream.selectExpr("CAST(value AS STRING)") \
        .select(from_json(col("value"), schema).alias("data")) \
        .select("data.text") \
        .withColumn("platform", lit(name)) \
        .withColumn("sentiment", udf(analyze)(col("text")))

    dfs.append(parsed)

combined = reduce(lambda a, b: a.unionByName(b), dfs)

combined.writeStream \
    .outputMode("append") \
    .format("parquet") \
    .option("path", "storage/output/") \
    .option("checkpointLocation", "storage/checkpoints/") \
    .start() \
    .awaitTermination()