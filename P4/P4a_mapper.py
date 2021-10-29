import sys
import csv

reader = csv.reader(sys.stdin)
next(reader, None)
for line in reader:
    movieId = line[1]
    rating = line[2]
    print(movieId + '\t' + rating)
