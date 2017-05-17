#!/usr/bin/python
import sys


def count_words(data):
    words = data.split(" ")
    num_words = len(words)
    return num_words

def count_lines(data):
    lines = data.split("\n")
    for l in lines:
        if not l:
            lines.remove(l)
    return len(lines)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_count.py <file>")
        exit(1)
    filename = sys.argv[1]
    f = open(filename, "r")
    data = f.read()
    f.close()
    num_words = count_words(data)
    num_lines = count_lines(data)

    print("The number of words:", num_words)
    print("The number of lines:", num_lines)

#f = open("birds.txt", "r")

#data = f.read()
#f.close()
#print(data)

#words = data.split(" ")
#print("The words in the text are:")
#print(words)
#num_words = len(words)
#print("Number of words is ", num_words)

#lines = data.split("\n")
#print("The lines in the text are:")
#print(lines)
#print("Wrong: The number of lines is", len(lines))
#for l in lines:
#    if not l:
#        lines.remove(l)
#print("The number of lines is ", len(lines))
