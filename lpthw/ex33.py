def whileTest(maxvalue):
    i = 0
    numbers = []
    while i < maxvalue:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers

numbers = whileTest(int(raw_input("Enter loopcounter: ")))
print "The numbers: "

for num in numbers:
    print num
