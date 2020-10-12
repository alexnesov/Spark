import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
df = spark.read.format("csv").option("header", "true").load("file:///home/nesov/Desktop/Financial_2020-09-17.csv")
df.show()
