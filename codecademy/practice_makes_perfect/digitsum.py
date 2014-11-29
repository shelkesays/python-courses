def digit_sum(number):
    number_string = str(number)
    total = 0
    for num in number_string:
        total += int(num)

    return total


print digit_sum(1234)
