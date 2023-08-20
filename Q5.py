import numpy as np

# Create a 10x10 array with random values between 1 and 10
array = np.random.randint(1, 11, size=(10, 10))

# Find the minimum and maximum values in the array
min_value = np.min(array)
max_value = np.max(array)

print("Minimum Value:", min_value)
print("Maximum Value:", max_value)
