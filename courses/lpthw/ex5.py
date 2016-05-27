name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

print "This is %r printed, no matter what!" % (weight)

height_in_centimeters = 2.54 * height
weight_in_kilos =  0.453592 * weight

# this line gives centimers and kilos, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_in_centimeters, weight_in_kilos, age + height_in_centimeters + weight_in_kilos)
