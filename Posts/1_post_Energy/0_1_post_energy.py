# Import dependencies.
import numpy as np
import matplotlib.pyplot as plt

# Simulate economic and political consequences of Nord Stream 2.
# 10-year simulation.
time = np.linspace(0, 5, 150)

# Initial European gas prices in EUR per MMBtu.
european_gas_prices = np.random.normal(5, 1, len(time))

# Introduce disruptions for both pipelines considering 2022 events.
first_pipeline_out_of_commission_year = 3
second_pipeline_never_turned_on_year = 2

# Introduce disruptions in gas prices due to geopolitical events in 2022.
european_gas_prices[first_pipeline_out_of_commission_year:] -= np.random.uniform(2, 4)

# The second pipeline was never turned on.
european_gas_prices[second_pipeline_never_turned_on_year:] -= np.random.uniform(1, 3)

# Simulate settling to new normals after disruptions.
new_normal_after_disruptions = 2
european_gas_prices[first_pipeline_out_of_commission_year:] = np.random.normal(new_normal_after_disruptions, 1, len(european_gas_prices) - first_pipeline_out_of_commission_year)
european_gas_prices[second_pipeline_never_turned_on_year:] = np.random.normal(new_normal_after_disruptions, 1, len(european_gas_prices) - second_pipeline_never_turned_on_year)

# Plot the simulation results.
plt.plot(time, european_gas_prices, label='Simulated European Gas Prices')
plt.axvline(x=first_pipeline_out_of_commission_year, color='r', linestyle='-', label='First Pipeline Out of Commission (2022)')
plt.axvline(x=second_pipeline_never_turned_on_year, color='g', linestyle='-', label='Second Pipeline Never Turned On')
plt.title('Nord Stream 2 Geopolitical Event')
plt.xlabel('Years')
plt.ylabel('European Gas Prices (EUR per MMBtu)')
plt.legend()
plt.show()
