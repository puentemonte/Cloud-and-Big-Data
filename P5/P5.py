from pyspark.sql import SparkSession
from pyspark.sql import functions as fun
from pyspark.sql.functions import col

archivo = 'Meteorite_Landings.csv'

spark = SparkSession.builder.appName('P5').getOrCreate()

df = spark.read.option('header', True).csv(archivo)

# únicamente necesito las columnas de recclass y mass
# casteo la masa a float
# agrupo por clase y calculo la media
df.drop('name', 'id', 'nametype', 'fall', 'year', 'reclat', 'reclong', 'GeoLocation').select('recclass', col('mass (g)').cast('float').alias('mass')).groupBy('recclass').agg(fun.mean('mass')).show()
