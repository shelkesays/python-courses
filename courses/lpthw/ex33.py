def whileTest(maxvalue, incrementor):
    i = 0
    numbers = []
    while i < maxvalue:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + incrementor
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers


def forTest(maxvalue):
    numbers = []
    for num in range(0, maxvalue):
        print "At the top i is %d" % num
        numbers.append(num)

        # i = i + incrementor
        print "Numbers now: ", numbers
        # print "At the bottom i is %d" % i

    return numbers


# numbers = whileTest(int(raw_input("Enter loop counter: ")), int(raw_input("Enter Incrementor: ")))
numbers = forTest(int(raw_input("Enter loop counter: ")))
print "The numbers: "

for num in numbers:
    print num
