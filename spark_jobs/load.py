from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("EcommerceVisitLoad") \
    .enableHiveSupport() \
    .getOrCreate()

df = spark.read.parquet("wasbs://<container>@<account>.blob.core.windows.net/output/visits_summary/")

df.write.mode("overwrite").saveAsTable("ecommerce.visits_summary")
