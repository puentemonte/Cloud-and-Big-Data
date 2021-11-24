from pyspark.sql import SparkSession
from pyspark.sql import functions as fun
from pyspark.sql.functions import col

ratings = 'ratings.csv'
movies = 'movies.csv'

spark = SparkSession.builder.appName('P4').getOrCreate()

# leo las películas y los ratings
df_r = spark.read.option('header', True).csv(ratings)
df_m = spark.read.option('header', True).csv(movies)

# hago un join de los dos dataframes para tener el titulo y el rating
df = df_m.join(df_r, df_m.movieId == df_r.movieId)

# agrupo por titulo y hago la media de la columna rating
result = df.drop('movieId', 'genres', 'userId', 'timestamp').groupBy('title').agg(fun.mean('rating'))

# imprimo todos los rangos por separado
range_1 = result.filter(col('avg(rating)') <= 1).show()
range_2 = result.filter((col('avg(rating)') > 1) & (col('avg(rating)') <= 2)).show()
range_3 = result.filter((col('avg(rating)') > 2) & (col('avg(rating)') <= 3)).show()
range_4 = result.filter((col('avg(rating)') > 3) & (col('avg(rating)') <= 4)).show()
range_5 = result.filter(col('avg(rating)') > 4).show()
