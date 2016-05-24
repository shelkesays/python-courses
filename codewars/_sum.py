"""
My solution
"""
def get_sum(a, b):
    total = 0
    if a == b:
        return a
    elif a > b:
        a = a + b
        b = a - b
        a = a - b
    else:
        pass
    for count in range(a, b + a):
        total += count
    return total


"""
Best solution from community
"""
def _get_sum(a, b):
    return sum(xrange(min(a, b), max(a, b) + 1))


print get_sum(1, 3)
print _get_sum(1, 3)
