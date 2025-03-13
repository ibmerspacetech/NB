from pyspark.sql import SparkSession
import os
spark = SparkSession.builder \
    .appName("HELLO_WORLD") \
    .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4") \
    .getOrCreate()
print ("HELLO WORLD")