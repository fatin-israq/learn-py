import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([1, 0, 1, 0])
print(a)

## We can directly calculate with the array
print(a + 2)
print(a * 2)
print(a / 2)
print(a + b)
print(np.cos(a)) # cosine of each element
## ... and so on