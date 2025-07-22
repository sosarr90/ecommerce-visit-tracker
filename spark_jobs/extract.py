from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("EcommerceVisitExtract") \
    .enableHiveSupport() \
    .getOrCreate()

#
blob_path = "wasbs://raw-data-ecommerce@blobstoreecommerce.blob.core.windows.net/sample_visits.csv"

#
spark._jsc.hadoopConfiguration().set(
    "fs.azure.account.key.blobstoreecommerce.blob.core.windows.net",
    ""
)

df = spark.read.option("header", True).csv(blob_path)
df.show(5)

print("✅ Extraction terminée avec succès.")

#df.write.mode("overwrite").parquet("wasbs://<container>@<account>.blob.core.windows.net/parquet_raw/")
