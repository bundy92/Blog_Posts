# Import dependencies. 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Set Seaborn style
sns.set(style="darkgrid")

# Parameters for the simulation
num_simulations = 1000
num_time_steps = 150

# Initial rare earth price
initial_price = 50

# Generate random factors for each simulation and time step
random_factors = np.random.normal(0, 5, size=(num_simulations, num_time_steps))

# Initialize an array to store simulated prices for each simulation
simulated_prices = np.zeros((num_simulations, num_time_steps))

# Set the initial price for each simulation
simulated_prices[:, 0] = initial_price

# Introduce disruptions due to the rare earth material crisis
crisis_year = 30

for i in range(1, num_time_steps):
    simulated_prices[:, i] = simulated_prices[:, i-1] + random_factors[:, i]

    # Introduce disruptions at the specified time step
    if i == crisis_year:
        disruption_amount = np.random.uniform(10, 20)
        simulated_prices[:, i] -= disruption_amount

    # Ensure prices stay non-negative
    simulated_prices[simulated_prices < 0] = 0

# Perform linear regression on average simulated prices
time_reshaped = np.arange(num_time_steps).reshape(-1, 1)
average_prices = np.mean(simulated_prices, axis=0).reshape(-1, 1)

regression_model = LinearRegression()
regression_model.fit(time_reshaped, average_prices)
regression_line = regression_model.predict(time_reshaped)

# Plot the Monte Carlo simulation and regression results with colors
plt.figure(figsize=(12, 8))

# Plot individual scenarios with a low alpha for transparency
for i in range(num_simulations):
    plt.plot(np.arange(num_time_steps), simulated_prices[i, :], color='lightgray', alpha=0.1)

# Highlight the crisis year with a distinct color
plt.plot(np.arange(num_time_steps), np.mean(simulated_prices, axis=0), color='blue', linewidth=2, label='Average Price')
plt.fill_between(np.arange(num_time_steps),
                 np.percentile(simulated_prices, 10, axis=0),
                 np.percentile(simulated_prices, 90, axis=0),
                 color='blue', alpha=0.2, label='10-90 Percentile Range')

# Plot the regression line
plt.plot(np.arange(num_time_steps), regression_line.flatten(), color='orange', linestyle='--', linewidth=2, label='Regression Line')

# Add labels and title
plt.title('Monte Carlo Simulation of Rare Earth Prices with Crisis and Regression Analysis (Non-negative Prices)')
plt.xlabel('Time Steps')
plt.ylabel('Simulated Rare Earth Prices')
plt.legend()

# Show the plot
plt.show()
