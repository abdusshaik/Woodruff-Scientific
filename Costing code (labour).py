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
    "Senior Technician": 0.3,
    "Junior Scientist/Engineer": 0,
    "Junior Engineer": 0,
    "Junior Technician": 0,
    "Laborers": 0
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

# Example usage
year = 2023
total_workers = 1000  # Adjust this value according to your scenario

# Calculate the total costs of workers
total_costs = calculate_total_costs(year, total_workers)

# Print the total costs
print(f"Total costs of workers in {year}: ${total_costs:.2f}")
