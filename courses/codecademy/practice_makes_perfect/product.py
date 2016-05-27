def product(sequence):
    result = 1
    for item in sequence:
        result *= item
    return int(result)


print product([1, 3, 2, 5, 6, 2, 6, 7, 8])
