import numpy as np
import matplotlib.pyplot as plt

def wrights_learning_curve(years, initial_workers, a, b, c):
    x = years - years[0]
    return initial_workers / (1 + np.exp(-(a * x + b) / (1 + c * np.abs(x))))

# Generate years from 2024 to 2050
years = np.arange(2024, 2051)

# Define parameters for the Wright's learning curve
initial_workers = 1000
a = 0.1  # Positive value to model the increasing number of workers
b = 20
c = 8

# Calculate the number of workers using the Wright's learning curve function
workers = wrights_learning_curve(years, initial_workers, a, b, c)

# Plot the Wright's learning curve
plt.plot(years, workers, label="Number of Workers")
plt.xlabel('Year')
plt.ylabel('Number of Workers')
plt.title("Wright's Learning Curve: Number of Workers over Time")
plt.grid(True)
plt.legend()
plt.show()
