import numpy as np

# Create a random vector of size 30 with values between 1 and 30
random_vector = np.random.randint(1, 31, size=30)

# Calculate the mean value
mean_value = np.mean(random_vector)

print("Random Vector (between 1 and 30):")
print(random_vector)
print("\nMean Value:", mean_value)
