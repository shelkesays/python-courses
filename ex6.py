# Define variabel x with string of value assigned
x = "There are %d types of people." % 10
# define variable binary with string of value assigned
binary = "binary"
# define variable do_not with string of value assigned
do_not = "don't"
# define variable y with string of value assigned
y = "Those who know %s and those who %s." % (binary, do_not)

# print value of variable x
print x
# print value of variable y
print y

# print value of x with formatted string representation
print "I said: %r." % x
# print value of y with formatted string representation
print "I also said: '%s'." % y

# define variable hialrious and assign it a value False
hilarious  = False
# define a variable joke_evaluation and assign it a value
joke_evaluation = "Isn't that joke so funny?! %r"

# print variable joke_evaluation and hilarious with formatted string
# representaiton
print joke_evaluation % hilarious

# Define variable w with string of value assigned
w = "This is the left sode of..."
# define varianble e with string of value assigned
e = "a string with a right side."

# print caoncatenations of variable w and e
print w + e
