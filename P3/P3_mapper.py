import sys
import csv

# el formato de la entrada es el siguiente
# 2018-02-21,1106.469971,1133.969971,1106.329956,1111.339966,1111.339966,1505300
# así que si separamos la entrada por comas obtenemos 7 items
# el primer item contiene la fecha, de la cual nos interesa el año

reader = csv.reader(sys.stdin)
next(reader, None)

for line in reader:
        date = line[0].split('-')
        year = date[0]
        close_price = line[4]
        print(year + '\t' + close_price)

