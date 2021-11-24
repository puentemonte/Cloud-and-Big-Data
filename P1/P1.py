from pyspark import SparkConf, SparkContext
import sys

conf = SparkConf().setAppName('P1')
sc = SparkContext(conf = conf)

archivo = 'input.txt'
word = sys.argv[1]

# filtro las lineas que contienen la palabra en ellas
rdd = sc.textFile(archivo).filter(lambda line: word in line).collect()

# imprimo las lineas del rdd
for line in rdd:
    print(line)
