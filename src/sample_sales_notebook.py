from pyspark.sql.functions import *
from pyspark.sql.types import *

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")
volume = dbutils.widgets.get("volume")

directory = "lab4"
data_path = "data"

work_folder = f"/Volumes/{catalog}/{schema}/{volume}/{directory}/{data_path}"

print("Work path:", work_folder)

salesSchema = StructType([
    StructField("Date", DateType()),
    StructField("Product", StringType()),
    StructField("Quantity", IntegerType()),
    StructField("Price", FloatType())
])

df = spark.read.load(work_folder, format='csv', header='true', schema=salesSchema)
df = df.withColumn("Revenue", col("Quantity") * col("Price"))

display(df)
