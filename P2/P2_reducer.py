import sys

prev = None
sum = 0

for line in sys.stdin:
    key, value = line.split('\t')

    if key != prev:
        if prev is not None:
            print(prev + '\t' + str(sum))
        prev = key
        sum = 0

    sum += int(value)

print(prev + '\t' + str(sum))
