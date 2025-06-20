import numpy as np;

a = np.ones((2, 3))
print(a)

b = np.full((3, 2), 2)
print(b)

# matrix multiplication -> matmul(matA, matB)
print(np.matmul(a, b))

# Find the determinant
c = np.identity(3)
determinant = np.linalg.det(c)
print(determinant)