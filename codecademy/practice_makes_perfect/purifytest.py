def purify(sequence):
    new_sequence = []
    for item in sequence:
        if item % 2 == 0:
            new_sequence.append(item)
    return new_sequence


print purify([1, 3, 2, 4, 2, 5, 6, 6, 7, 8, 8, 9])
