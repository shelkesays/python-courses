from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# Get status to continue or close program
raw_input("?")

print "Opening the file..."
# open filename
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# truncate file
target.truncate()

print "Now I'm going to ask you for three lines."

# read 3 lines form user
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to file."

# Write result to file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
# Close file
target.close()
