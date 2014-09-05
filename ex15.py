# from sys library / module import argv functionality
from sys import argv

# define variable script and filename from argv
script, filename = argv

# opne file specified by filename and give it to txt
txt = open(filename)

# print filename
print "Here's your file %r:" % filename
# print content of file
print txt.read()

# print statement
print "Type the filename again:"
# read filename from user input
file_again = raw_input("> ")

# open file specified by file_again and give it to txt_again
txt_again = open(file_again)

# print content of file txt_again
print txt_again.read()
