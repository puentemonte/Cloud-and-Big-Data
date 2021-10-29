import sys
import csv

# el primer dato es la fecha, de la cual nos interesa el año
# separamos la fecha (en formato YYYY-MM-DD) para obtener el año
# nos quedamos con el close_price que es el precio de la acción para ese día

reader = csv.reader(sys.stdin)
next(reader, None)

for line in reader:
        date = line[0].split('-')
        year = date[0]
        close_price = line[4]
        print(year + '\t' + close_price)
