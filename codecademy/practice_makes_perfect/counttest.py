def count(sequence, item):
    counter = 0
    for itm in sequence:
        if itm == item:
            counter += 1
    return counter


print count([1, 3, 2, 4, 2, 6, 2, 4, 2, 5, 2, 2], 2)
