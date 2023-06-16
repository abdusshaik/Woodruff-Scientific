import numpy as np
import matplotlib.pyplot as plt

def wrights_learning_curve(years, initial_workers, a, b, c):
    x = years - years[0]
    return initial_workers / (1 + np.exp(-(a * x + b) / (1 + c * np.abs(x))))

# Worker costs per category per hour
costs_per_hour = {
    "Scientist": 163.60,
    "Senior Technician": 57.74,
    "Junior Scientist/Engineer": 140.74,
    "Junior Engineer": 123.42,
    "Junior Technician": 52.93,
    "Laborers": 18.04
}

# Workforce distribution during construction
construction_distribution = {
    "Scientist": 0,
    "Senior Technician": 0.2,
    "Junior Scientist/Engineer": 0.1,
    "Junior Engineer": 0.2,
    "Junior Technician": 0.2,
    "Laborers": 0.3
}

# Number of working hours in a year
working_hours_per_year = 2080  # Assuming 40 hours per week, 52 weeks per year

# Function to calculate total costs for a year and number of workers
def calculate_total_costs(year, total_workers):
    construction_workers = {
        category: total_workers * percentage
        for category, percentage in construction_distribution.items()
    }

    total_costs = 0
    for category, percentage in construction_distribution.items():
        category_workers = construction_workers[category]
        cost_per_hour = costs_per_hour[category]
        category_costs = category_workers * cost_per_hour * working_hours_per_year
        total_costs += category_costs

    return total_costs

# Generate years from 2020 to 2060
years = np.arange(2020, 2061)

# Define parameters for the Wright's learning curve
initial_workers = 6000  # Assume 6 years to build each reactor
a = 0.1  # Positive value to model the increasing number of workers
b = 10
c = 10

# Calculate the number of workers using the Wright's learning curve function
workers = wrights_learning_curve(years, initial_workers, a, b, c)

# Calculate the total costs for each year based on the number of workers
total_costs_per_year = [
    calculate_total_costs(year, workers[i])
    for i, year in enumerate(years)
]

# Calculate the accumulated costs over the years
accumulated_costs = np.cumsum(total_costs_per_year)

# Calculate the total cost
total_cost = accumulated_costs[-1]

# Calculate the total number of watts produced over the 40-year period
power_output_40_years = 10e9 * 1000  # 10 GW per reactor, 1000 reactors

# Calculate the cost of one watt produced over the 40-year period
cost_per_watt_40_years = accumulated_costs[-1] / power_output_40_years

# Plot the Wright's learning curve and stacked bar chart
fig, ax = plt.subplots()

# Plot the Wright's learning curve
ax.plot(years, workers, label="Number of Workers")
ax.set_xlabel('Year')
ax.set_ylabel('Number of Workers')
ax.set_title("Wright's Learning Curve: Number of Workers over Time")

# Calculate and plot the stacked bar chart
categories = list(construction_distribution.keys())
bottom = np.zeros_like(years, dtype=np.float64)
for category in categories:
    workers_category = workers * construction_distribution[category]
    ax.bar(years, workers_category, bottom=bottom, label=category)
    bottom += workers_category

# Add legend
ax.legend()

# Show the plot
plt.show()

# Print the total cost and the cost of one watt produced over the 40-year period
print(f"Total labor cost for 1000 reactors over 40 years: ${total_cost:.2f}")
print(f"Cost of one watt produced over 40 years: ${cost_per_watt_40_years:.10f}")
