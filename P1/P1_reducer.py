import sys

# con el reducer lo que tenemos que hacer es eliminar duplicados, es decir, lineas en las que word aparece más de una vez

prevLine = None

for line in sys.stdin:
    if line != prevLine:
        if prevLine is not None:
            print(prevLine + '\t')
        prevLine = line

print(prevLine + '\t')
