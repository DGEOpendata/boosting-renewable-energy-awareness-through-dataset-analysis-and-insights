python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Renewable_Energy_Share_2013-2024.csv')

# Preview the dataset
print(data.head())

# Convert Year column to datetime
data['Year'] = pd.to_datetime(data['Year'], format='%Y')

# Plot the Renewable Energy Share over Years
plt.figure(figsize=(12, 6))
plt.plot(data['Year'], data['Renewable_Energy_Share'], marker='o', linestyle='-', color='green')
plt.title('Renewable Energy Share in Abu Dhabi (2013-2024)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Renewable Energy Share (%)', fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()

# Save the plot
plt.savefig('Renewable_Energy_Share_Trend.png')

# Summary statistics
summary_stats = data['Renewable_Energy_Share'].describe()
print(summary_stats)

# Save the summary statistics to a CSV file
summary_stats.to_csv('Renewable_Energy_Share_Summary.csv')
