from sys import argv

# read argument form command line
script, input_file= argv

# define function to print whole file
def print_all(f):
    print f.read()

# define a funciton to rewind file
def rewind(f):
    f.seek(0)

# define funciton to print particualr line
def print_a_line(line_count, f):
    print line_count, f.readline()

# open file on the input_file
current_file = open(input_file)

print "First let's print the whole file:\n"

# print all file content
print_all(current_file)

print "Now let's rewind, kind of like tape."

# rewind current file
rewind(current_file)

print "Let's print three lines:"

current_line = 1
# print line 1
print_a_line(current_line, current_file)

current_line = current_line + 1
# print loine 2
print_a_line(current_line, current_file)

current_line = current_line + 1
# print line 3
print_a_line(current_line, current_file)
