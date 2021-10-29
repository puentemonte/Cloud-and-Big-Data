import sys
import re

# para el mapper lo que hay que hacer es lo siguiente:
# input: un string de la entrada stdin
# output: lista de lineas que contienen la palabra word

# guardamos la palabra que hay que buscar
palabra = sys.argv[1]

for line in sys.stdin:
    words = re.sub(r'W+', ' ', line).split()

    for word in words:
        if word.lower() == palabra.lower():            
            print(line)
