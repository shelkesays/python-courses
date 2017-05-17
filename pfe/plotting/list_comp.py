#! /usr/bin/python
import numpy as np

x = [5, 10, 15, 20, 25]

# declare y as empty list
y = []

for counter in x:
    y.append(counter / 5)

print("\nOld fashioned way: x = {} y = {} \n".format(x, y))

z = [n/5 for n in x]
print("List Comprehension: x = {} z = {}".format(x, z))

a = np.array(x)
b = a / 5

print("With Numpy: a = {} b = {} \n".format(a, b))
