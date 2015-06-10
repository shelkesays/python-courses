def copy_list(l):
    """Make a copy of a list of numbers"""
    return l[:] #[d for d in l]


l = [1, 2, 3, 4]
test = copy_list(l)
print l
l[1] = 5
print l
print test
