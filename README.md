# Spark

Example of python script execution (executed while being located in ```spark/python folder```): </p>

<code>spark-submit --master spark://hadoop-master:7077 ~/Downloads/spark-3.0.1-bin-hadoop2.7/python/ratings-counter.py</code> 

From jupyter notebook (executed while being located in ```spark/python folder```): </p>
<code>
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
df = spark.read.format("csv").option("header", "true").load("file:///home/nesov/Desktop/Financial_2020-09-17.csv")
df.show()
</code>

Very valuable ressource:
https://phoenixnap.com/kb/install-spark-on-ubuntu
