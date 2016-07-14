# Check if a string ends with the given target string
def substring(string, endstring):
    if string.find(endstring):
        return string[-len(endstring):] == endstring

string = "Rahul Shelke"
endstring = "Shelke"
if substring(string, endstring):
    print("The string {} ends with {}".format(string, endstring))
else:
    print("The string {} does not end with {}".format(string, endstring))
