import numpy as np

a = np.array([1, 2, 3])
print(a)

# 2D Array
b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)

# Get Dimension = a.ndim
print(a.ndim)
print(b.ndim)

# Get Shape = b.shape
print(b.shape)

# Get Type = a.dtpye
print(a.dtype)

# Get Size = a.itemsize
print(f"{a.itemsize} bytes")

# Get total size
print(f"{a.size * a.itemsize} bytes")

# Get a specific element [row, col]
print(b[1, 2])

# Get a specific row
print(b[0, :]) # will print the first row

# Get a specific col
print(b[:, 2]) # will print the third col

# Getting a little more fancy [startindex:endindex:stepsize]
print(b[0, 0:-1:2])