import sys

# lo que queremos hacer ahora es por cada clave igual (el mismo año)
# sumar los precios y el número de apariciones del año
# la salida tiene que ser el año y la media (precios/num apariciones)

prev = None
suma = 0
i = 0

for line in sys.stdin:
    year, close_price = line.split('\t')
    
    if year != prev:
        if prev is not None:
            print(prev + '\t' + str(suma/i))
        prev = year
        suma = 0
        i = 0
    suma += float(close_price)
    i += 1

print(prev + '\t' + str(suma/i))
    
