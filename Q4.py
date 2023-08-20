import numpy as np

# Create the array
arr = np.array([1, 2, 0, 0, 4, 0])

# Find the indices of non-zero elements
non_zero_indices = np.nonzero(arr)

print(non_zero_indices)
