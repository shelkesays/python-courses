# this solution is efficient than mysoultions.py
def fibonacci():
    total = 0
    first = second = 1
    last = first + second
    while last < 4000000:
        total += last
        first = second + last
        second = last + first
        last = first + second

    return total


print fibonacci()
