#1.Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives

import numpy as np

# Create arrays of 10 zeros, 10 ones, and 10 fives
zeros = np.zeros(10)
ones = np.ones(10)
fives = np.full(10, 5)

# Concatenate them into a single array
result = np.concatenate([zeros, ones, fives])

print(result)

#OUTPUT
'''[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 5. 5. 5. 5.
 5. 5. 5. 5. 5. 5.]'''



