import sys
import re

for line in sys.stdin:
    data = re.sub(r'\W+', ' ', line).split()
    # imprimimos los datos para que la clave sea el rating y el valor la película
    print(data[1] + '\t' + data[0])
