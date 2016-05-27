def remove_duplicates(sequence):
    new_sequence = []
    for item in sequence:
        if item not in new_sequence:
            new_sequence.append(item)
    return new_sequence


print remove_duplicates([1, 2, 4, 5,2, 5, 6, 7, 2, 5, 1, 5, 4, 6, 7, 2, 5, 6, 4, 6])
