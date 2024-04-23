from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("FinnhubDataProcessor") \
    .getOrCreate()

df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka:9092") \
  .option("subscribe", "finhub_data") \
  .load()


processed_df = df.selectExpr("CAST(value AS STRING)")
query = processed_df.writeStream \
    .format("org.apache.spark.sql.cassandra") \
    .option("keyspace", "finhub") \
    .option("table", "stock_data") \
    .start()

query.awaitTermination()
