def multiple(number1, number2, upto):
    total = 0
    counter = 1
    while counter < upto:
        if counter % number1 == 0 or counter % number2 == 0:
            total += counter
        counter += 1

    return total


print multiple(3, 5, 1000)
