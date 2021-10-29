import sys

prev = None
i = 0
sum = 0

for line in sys.stdin:
    key, value = line.split('\t')

    if key != prev:
        if prev is not None:
            print(prev + '\t' + str((sum/i)))
        prev = key
        sum = 0
        i = 0
    sum += float(value)
    i += 1

print(prev + '\t' + str(round(sum/i, 1)))
