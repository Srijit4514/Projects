
import numpy as np
import matplotlib.pyplot as plt 

# Number of random points
num_points = 10000000

# Generate random points
x = np.random.uniform(-1, 1, num_points)
y = np.random.uniform(-1, 1, num_points)

# Calculate the number of points inside the circle
inside_circle = x**2 + y**2 <= 1

# Estimate Pi
pi_estimate = 4 * np.sum(inside_circle) / num_points

# Display results
print(f"Estimated value of Pi: {pi_estimate} ")

import random

sample_size = 10000
indices = np.random.choice(num_points, sample_size, replace=False)

sample_x = x[indices]
sample_y = y[indices]
sample_inside_circle = inside_circle[indices]

# Plot the points
plt.figure(figsize=(6, 6))
plt.scatter(sample_x[sample_inside_circle], sample_y[sample_inside_circle], color='blue', marker='.', label='Inside Circle')
plt.scatter(sample_x[~sample_inside_circle], sample_y[~sample_inside_circle], color='red', marker='.', label='Inside Circle')
plt.gca().set_aspect('equal', adjustable = 'box')
plt.legend()
plt.title('Monte Carlo Simulation for Estimating Pi')
plt.axis(False)
plt.show()