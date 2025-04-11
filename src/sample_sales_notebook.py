from pyspark.sql.types import *
from pyspark.sql.functions import *

import argparse


parser = argparse.ArgumentParser(description="Download and read data")
parser.add_argument('-c', '--catalog')
parser.add_argument('-s', '--schema')
parser.add_argument('-v', '--volume')
args = parser.parse_args()

catalog = args.catalog
schema = args.schema
volume = args.volume

directory = "lab4"
data_path = "data"

work_folder = f"/Volumes/{catalog}/{schema}/{volume}/{directory}/{data_path}"

salesSchema = StructType([
    StructField("Date", DateType()),
    StructField("Product", StringType()),
    StructField("Quantity", IntegerType()),
    StructField("Price", FloatType())
])

df = spark.read.load(f"{work_folder}/data", format='csv', header='true', schema=salesSchema)
df = df.withColumn("Revenue", col("Quantity") * col("Price"))

display(df)
