# Geopolitics of Energy: Unraveling the Dynamics of Energy-Driven Conflicts

## 1. Introduction

Welcome everyone! Let's continue exploration into the relationship between energy resources and geopolitics. In this blog post, another critical scenario, the geopolitical dynamics surrounding the Nord Stream 2 pipeline is our playground. Through a new simulation, we illustrate potential scenarios and their impacts on European gas prices and political relationships. In this script we build on the very simple solution shown in the previous article. Again these scenarios are extendable if needed. Also not thorough in investigating the actual geopolitical events that might have occurred.

## 2. Pipeline Politics: Nord Stream 2

The Nord Stream 2 pipeline, connecting Russia to Europe, has become a well known point of geopolitical tensions in the recent years. This undersea pipeline has been a source of controversy, raising concerns related to energy security, regional influence, and political alliances. Notably, in the aftermath of the Russo-Ukrainian conflict in early 2022 the Nord Stream pipelines were sabotaged, adding a new layer of complexity to the geopolitical landscape. Even though Nord Stream 1 was out of commission and Nord Stream 2 never became operable in the time of the events.

## 3. The Nord Stream 2 Simulation

Let's model the potential economic and political consequences if the pipeline faces disruptions. This scenario is of particular interest as it involves key geopolitical players, including the Russian Federation, the European Union, and the United States. The destructive sabotage after the start of the Russo-Ukrainian conflict is significant twist as well. The simulated European gas prices, represented in EUR per MMBtu (British thermal unit), are subjected to disruptions of the Nord Stream 2 pipeline, taking into account the destructive events in 2022. You may introduce other variables if you are to build on this concept. In reality there are a myriad of factors to consider. Such as American or Middle-Eastern LNG (liquid natural gas) supply availability or the increase of local production in case of disruption.

## 4. Python Simulation

In this simulation, again a Python script will model economic and political consequences over a five-year period. Similarly to our previous article we utilize NumPy as a standard fast mathematical library and Matplotlib to visualize our results. Don't forget to install them locally or into your virtual environment. First we make a ten year time series vector using NumPy. Then adding gas prices to each date following normal distribution. Here, as before the normal distribution only implies our price to fluctuate around the mean. Not necessarily as it happens in reality. Now introduce two disruptions. One, if the first pipeline goes out of commission. The second, if after finishing the construction the second pipeline will not be turned on at all. Now let's apply these disruptions as we did in the previous article. Deducting uniformly distributed values after the events happened. Another addition to shift the price to a new base level after the disruptions.

```python
# Import dependencies.
import numpy as np
import matplotlib.pyplot as plt

# Simulate economic and political consequences of Nord Stream 2.
# 5-year simulation.
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

```

## 5. Analysis of the results

The simulation illustrates the potential economic and political consequences around Nord Stream 2. As shown in the graph, the European gas prices experience fluctuations based on the introduction of disruptions of the pipeline, with a notable impact from both destructive events. However, as in the real world in a long enough time window the momentarily fluctuations are barely visible. Prices tend to return their market values after such events. We can clearly see both situation could harm commodities and option markets that rely on predictably. Important to mention, as visible on the chart the normal distribution is not perfect to capture price movements. Those tend to follow trends of the markets and react on singular events as well. Possible future task is to check it against historical time series data or apply better tools, like the Monte Carlo method.

## 6.Potential geopolitical implications

Post-Conflict Economic Recovery
 The events in 2022 significantly impacted European gas prices, highlighting the vulnerability of energy infrastructure to geopolitical conflicts. Post-conflict economic recovery efforts might include rebuilding energy infrastructure and re-establishing stable supply chains.
Security Concerns and Diversification
 The destruction of the Nord Stream pipelines raises security concerns and emphasizes the need for diversification of energy sources. European nations may need to intensify efforts to secure alternative energy routes to reduce dependence on specific pipelines.
Global Energy Landscape
 The geopolitical landscape undergoes shifts as a consequence of new global wars. Countries should reevaluate their energy strategies, potentially leading to altered alliances and diplomatic relations in the quest for energy security.

## Conclusion

In this article we observed the potential economic and political consequences of a pipeline disturbance may cause. The script provided a visual representation of how these events can influence European gas prices and discussed the effect of geopolitical relationships.
We continue to learn more of energy-driven conflicts, future scenarios, that are shaping the world of energy. Stay with us for our upcoming posts where we continue to build on these concepts!
Disclaimer: This article is intended for educational purposes only and does not constitute financial, investment, or political advice. The information presented, including the Python simulation, is based on hypothetical scenarios for illustrative purposes. Any actions taken or decisions made based on the content of this article are at the sole discretion of the reader. The author is not responsible for any consequences resulting from the use or misuse of the information.
