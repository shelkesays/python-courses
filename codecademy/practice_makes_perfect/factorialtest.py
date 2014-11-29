def factorial(number):
    fact = 1
    num = 1
    while num <= number:
        fact *= num
        num += 1
    return fact


print factorial(4)
