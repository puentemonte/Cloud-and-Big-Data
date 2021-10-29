import sys
import csv

reader = csv.reader(sys.stdin)
next(reader, None)
for line in reader:
    recclass = line[3]
    mass = line[4]
    # ignoramos las entradas que no tienen masa
    if mass:
        print(recclass + '\t' + mass)
