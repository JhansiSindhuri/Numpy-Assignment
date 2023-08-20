import numpy as np

# Create a 1D array with values ranging from 0 to 8
array_1d = np.arange(9)

# Reshape the 1D array into a 3x3 matrix
matrix_3x3 = array_1d.reshape(3, 3)

print(matrix_3x3)
