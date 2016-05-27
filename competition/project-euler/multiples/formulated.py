def divisible(number, target):
    p = target / number
    return number * (p * (p + 1)) / 2


print divisible(3, 999) + divisible(5, 999) - divisible(15, 999)
