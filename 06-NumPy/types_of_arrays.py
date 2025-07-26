import numpy as np

# All 0s matrix
arr_zero = np.zeros(5) # It will create a 5 sized array where every value is 0
mat_zero = np.zeros((2, 3)) # It will create a 2x3 matrix where every value is 0

print(arr_zero)
print(mat_zero)
print()

# All 1s matrix
arr_one = np.ones(5)
mat_one = np.ones((2, 3))

print(arr_one)
print(mat_one)
print()

# Any other number
mat_other = np.full ((2, 3), 99) # First parameter is the shape, second one is the value
print(mat_other)
print()

# The identity matrix
mat_identity = np.identity(5)
print(mat_identity)
print()

