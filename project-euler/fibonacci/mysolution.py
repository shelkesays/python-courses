def fibonacci():
    first = second = 1
    series = [first]
    total = 0
    while second < 4000000:
        series.append(second)
        if second % 2 == 0:
            total += second
        last = first + second
        first = second
        second = last

    return total, series


print fibonacci()
