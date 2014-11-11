def test_function(values):
    print "Values passed are: %d\n" % values


value = 20
test_function(10)
test_function(value)
test_function(value * 2)
test_function(30 / 5)
# this is wrong in current case since test_function does not return anything
#test_function(test_function(30))

value = raw_input("Enter value: ")
test_function(int(value))
test_function(int(raw_input("Enter another value: ")))
