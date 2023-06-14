import numpy as np
import matplotlib.pyplot as plt

def s_curve(x):
    return 1 / (1 + np.exp(-k*(x - x0)))

# Generate x values from -10 to 10
x = np.linspace(-5, 5, 100)
k = 1.7
x0 = -1 

# Calculate y values using the S-curve function
y = s_curve(x)

# Define the gradient for the linear line
gradient = 0.3 # Change this value to adjust the gradient of the line

# Calculate the y values for the linear line
linear_line = gradient * x +0.8

# Plot the S-curve and the linear line
plt.plot(x, y, label='S-Curve')
plt.plot(x, linear_line, label='Linear Line', linestyle='--')
plt.xlabel('Year')  # Update the x-axis label
plt.ylabel('Total Installed Effective Power')  # Update the y-axis label
plt.title('S-Curve')
plt.grid(True)
plt.legend()

# Custom tick values and labels for the x-axis
x_ticks = [ -7.5, 0, 7.5]
x_tick_labels = [ '2030', '2050', '2070']
plt.xticks(x_ticks, x_tick_labels)

# Custom tick values and labels for the y-axis
y_ticks = [0, 0.5, 1]
y_tick_labels = ['100 MW', '10 GW', '1 TW']
plt.yticks(y_ticks, y_tick_labels)

plt.show()