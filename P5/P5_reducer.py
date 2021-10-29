import sys

recclass = None
suma = 0
i = 0

for line in sys.stdin:
    clase, masa = line.split('\t')
    if recclass != clase:
        if recclass is not None:
            print(recclass + '\t' + str(suma/i))
        recclass = clase
        suma = 0
        i = 0
    i += 1
    suma += float(masa)
print(recclass + '\t' + str(suma/i))
