# define a function names cheese_and_crackers with two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# call function with values directly
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# call function with variables as arguments / parameters
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# call function with math inside arguments
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# call function with variable and math in argument
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
