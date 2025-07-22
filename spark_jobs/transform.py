from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp, col, countDistinct

spark = SparkSession.builder.appName("EcommerceVisitTransform").getOrCreate()

df = spark.read.parquet("wasbs://<container>@<account>.blob.core.windows.net/parquet_raw/")

df_clean = df.withColumn("timestamp", to_timestamp("timestamp")) \
             .filter(col("page").isNotNull()) \
             .filter(col("user_id").isNotNull())

df_sessions = df_clean.groupBy("session_id").agg(
    countDistinct("user_id").alias("unique_users"),
    countDistinct("page").alias("unique_pages_visited")
)

df_sessions.write.mode("overwrite").parquet("wasbs://<container>@<account>.blob.core.windows.net/output/visits_summary/")
