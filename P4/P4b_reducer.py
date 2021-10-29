import sys

prevRating = -1

for line in sys.stdin:
    data = line.split('\t')
    rating = data[0]
    movieId = data[1]
    if rating != prevRating:
        if int(rating) >= 0 and int(rating) <= 1:
            print("Range 1:")
        elif int(rating) > 1 and int(rating) <= 2:
            print("Range 2:")
        elif int(rating) > 2 and int(rating) <= 3:
            print("Range 3:")
        elif int(rating) > 3 and int(rating) <= 4:
            print("Range 4:")
        else:
            print("Range 5:")
    prevRating = rating
    print(movieId, end=' ')
