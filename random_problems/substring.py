# Check if a string ends with the given target string
def substring(string, endstring):
    if string.find(endstring):
        return string[-len(endstring):]

print substring("Rahul Shelke", "Shelke")
