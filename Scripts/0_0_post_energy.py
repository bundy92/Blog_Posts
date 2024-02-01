# Importing the dependencies. 
import numpy as np
import matplotlib.pyplot as plt

# Simulate disruptions in the Strait of Hormuz.
# 1 year simulation of our time series.
time = np.linspace(0, 365, 365)
# Initial global oil supply in million barrels per day.
oil_supply = np.random.normal(80, 10, len(time))

# Introduce a disruption in Q1.
disruption_start = int(len(time) / 4)
oil_supply[disruption_start:] -= np.random.uniform(10, 30)

# Plot the results.
plt.plot(time, oil_supply, label='Simulated Global Oil Supply')
plt.axvline(x=disruption_start, color='r', linestyle='-', label='Disruption Event')
plt.title('Strait of Hormuz Disruption Event')
plt.xlabel('Days')
plt.ylabel('Oil Supply (Million Barrels per Day)')
plt.legend()
plt.show()