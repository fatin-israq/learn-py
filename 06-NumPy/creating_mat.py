# [[1, 1, 1, 1, 1],
#  [1, 0, 0, 0, 1],
#  [1, 0, 9, 0, 1],
#  [1, 0, 0, 0, 1],
#  [1, 1, 1, 1, 1]]

# We will be trying to create the matrix with the methods we've learned so far

import numpy as np

matrix = np.ones((5, 5), dtype=np.int8)
matrix[1:4, 1:4] = 0
matrix[2, 2] = 9

print(matrix)