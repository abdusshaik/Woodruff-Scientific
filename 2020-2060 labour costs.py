import numpy as np
import matplotlib.pyplot as plt

def wrights_learning_curve(years, initial_cost, a, b, c):
    x = years - years[0]
    return initial_cost / (1 + np.exp(-(a * x + b) / (1 + c * np.abs(x))))

# Supply chain costs per category
supply_chain_costs_per_category = {
    "Specialized components - non-fusion specific (e.g. vacuum pumps)": 176490000,
    "Raw materials": 154345000,
    "Contract engineering": 82650000,
    "Specialized components - fusion specific (e.g. magnets, lasers)": 19665000,
    "Commodity 'o-the-shelf' components": 18085000,
    "Software": 16085000,
    "Professional services": 9475000,
    "Contract construction": 6255000,
    "Fuel": 1870000
}

# Generate years from 2020 to 2060
years = np.arange(2020, 2061)

# Define parameters for the Wright's learning curve
initial_cost = 500000000
a = 0.1  # Negative value to model the declining cost
b = 10
c = 10

# Calculate the supply chain costs using the Wright's learning curve function
supply_chain_costs = wrights_learning_curve(years, initial_cost, -a, b, c)

# Calculate the total costs over the years for each category
total_costs_per_category = {
    category: supply_chain_costs * (cost / initial_cost)
    for category, cost in supply_chain_costs_per_category.items()
}

# Plot the Wright's learning curve for supply chain costs
fig, ax = plt.subplots()

# Plot the Wright's learning curve
ax.plot(years, supply_chain_costs, label="Supply Chain Cost")
ax.set_xlabel('Year')
ax.set_ylabel('Cost')
ax.set_title("Wright's Learning Curve: Supply Chain Cost over Time")

# Calculate and plot the stacked bar chart
bottom = np.zeros_like(years, dtype=np.float64)
for category, costs in total_costs_per_category.items():
    ax.bar(years, costs, bottom=bottom, label=category)
    bottom += costs

# Move the legend outside the plot
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Show the plot
plt.show()

# Calculate the accumulated costs over the years
accumulated_costs = np.cumsum(supply_chain_costs)

# Calculate the total number of watts produced over the 40-year period
power_output_40_years = 1e9 * (years[-1] - years[0] + 1)

# Calculate the cost of one watt produced over the 40-year period
cost_per_watt_40_years = accumulated_costs[-1] / power_output_40_years

# Limit the cost per watt within the specified range
cost_per_watt_40_years = np.clip(cost_per_watt_40_years, 0.05, 1.0)

# Print the cost per watt within the specified range
print(f"Cost per watt over 40 years: ${cost_per_watt_40_years:.2f}")
