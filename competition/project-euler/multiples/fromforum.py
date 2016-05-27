# This is best answer from forum from python as per number of lines
print sum(map(lamda x: x if x%3 == 0 or x%5 == 0 else 0, range(1, 1000)))
