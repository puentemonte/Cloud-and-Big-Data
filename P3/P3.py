from pyspark.sql import SparkSession
from pyspark.sql import functions as fun
from pyspark.sql.functions import to_date, year, col

archivo = 'GOOGLE.csv'

spark = SparkSession.builder.appName('P3').getOrCreate()

df = spark.read.option('header', True).csv(archivo)

# únicamente hacen falta las columnas de date y close
date_and_close = df.drop('Open', 'High', 'Low', 'Adj Close', 'Volume')
# cambio el tipo de la columna date de string a date y me quedo con el año
# casteo la columna close a float
# agrupo por año y calculo la media de la columna close
date_and_close.select(to_date('Date').alias('Date'), 'Close').select(year('Date').alias('Date'), col('Close').cast('float')).groupBy('Date').agg(fun.mean('Close')).sort('Date').show()
