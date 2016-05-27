def median(sequence):
    sequence.sort()
    length = len(sequence)
    index = length / 2
    median = 0
    if length % 2 == 0:
        numerator = sequence[index - 1] + sequence[index]
        median = numerator / 2.0
    else:
        median = sequence[index]
    return median


print median([1, 3, 2, 5, 2, 5, 6, 7, 8, 45, 8, 9])
