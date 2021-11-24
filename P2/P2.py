from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName('P2')
sc = SparkContext(conf = conf)

archivo = 'access_log'

# primero obtengo el url de cada log
# como en MapReduce, obtengo un par de la forma clave url y valor 1
# sumo los valores
urls = sc.textFile(archivo).map(lambda log: log.split(' ')[6]).map(lambda url: (url, 1)).reduceByKey(lambda x,y : x + y).collect()

# imprimo cada url del rdd urls
for url in urls:
    print(url)
