from pyspark.sql import SparkSession
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv("PG_USER", "postgres")
POSTGRES_PASS = os.getenv("PG_PASS", "password")
POSTGRES_HOST = os.getenv("PG_HOST", "localhost")
POSTGRES_DB   = os.getenv("PG_DB", "sentiments")
POSTGRES_PORT = os.getenv("PG_PORT", "5432")

# Assemble PostgreSQL connection string
conn_str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Start Spark
spark = SparkSession.builder.appName("ExportToPostgres").getOrCreate()

# Load the parquet data
df = spark.read.parquet("storage/aggregated/")

# Export to PostgreSQL
try:
    pandas_df = df.toPandas()
    engine = create_engine(conn_str)
    pandas_df.to_sql("sentiment_summary", engine, if_exists="replace", index=False)
    print("✅ Exported sentiment data to PostgreSQL successfully.")
except Exception as e:
    print("❌ Failed to export to PostgreSQL:", str(e))