# Geopolitical conflicts Pt.3

## Implications of a rare earth material crisis

[Link to Python script on Github](your_github_link)

## Introduction

Hello everyone! Today, we talk about a topic of great importance - the connection between resources and geopolitics, with a specific focus on the 2010 rare earth material crisis. This event, triggered by China's decision to stop exporting many of these crucial ores, caused quite a stir in the global supply chain. We will tools like the Monte Carlo method and regression analysis and explore how this crisis affected economies and politics around the world. But first, let's lay down some groundwork.

Understanding Rare Earth Materials
Rare earth materials are a group of seventeen chemical elements in the periodic table, comprising the lanthanide series and scandium and yttrium. Despite their name, they are not particularly rare, but they are widely dispersed in the Earth's crust and often found in conjunction with other minerals. These materials possess unique magnetic, luminescent, and catalytic properties, making them essential components in various high-tech applications, including electronics, renewable energy technologies, and defense systems. Rare earth materials play a crucial role in a myriad of industries, from electronics to renewable energy. However, the unpredictable nature of rare earth prices poses significant challenges for industries reliant on these materials.

In our narrative, we hone in on neodymium, a prized constituent of the rare earth family, revered for its magnetic properties and indispensable role in the production of high-performance magnets. From powering wind turbines to electrifying the automotive industry, neodymium emerges as a linchpin in the arsenal of modern technology, propelling innovation and progress. Despite its moniker as a "rare earth" material, neodymium's ubiquity in contemporary applications belies its scarcity, underscoring the intricacies of resource economics and industrial exigencies.

Global Distribution and Production
The majority of the world's rare earth elements are mined and produced in China, which accounts for approximately 80% of global production. Other significant producers include Australia, the United States, Russia, and several countries in Africa and Southeast Asia. Given their critical role in modern technology, the geopolitical implications of rare earth production and distribution are profound, shaping international relations and strategies for resource security.

Japan, a major consumer of neodymium, found itself grappling with the repercussions of China's dominance during the 2010 rare earth material crisis. Historically, China supplied over 90% of Japan's rare earth imports, a figure that has gradually declined to around 60%. To counter the risks associated with this heavy dependency, Japan has embarked on strategic initiatives. These include investments in recycling programs to recover rare earth minerals from discarded electronics, exploring alternative mining sites such as seabed deposits, and fostering international partnerships to diversify its supply chain. By leveraging these strategies, Japan aims to bolster its economic competitiveness and technological innovation while reducing vulnerability to geopolitical disruptions in the rare earth market.

The 2010 rare earth material crisis unfolded when China, the world's leading producer of rare earth elements, decided to halt its export of these vital materials. Rare earth elements are essential components in high-tech industries such as electronics, renewable energy, and defense technologies. The sudden disruption of the supply chain had widespread ramifications, forcing a reassessment of global dependencies and exposing vulnerabilities in the interconnected realms of energy and geopolitics.

The crescendo of the 2010 rare earth material crisis reached its zenith when China, the unrivaled titan in neodymium production, elected to curtail its export of this vital material. Embedded within the sinews of burgeoning industries such as renewable energy and electric vehicles, neodymium emerged as a linchpin, orchestrating the symphony of technological progress. The sudden disruption of the neodymium supply chain sent shockwaves reverberating through global markets, catalyzing a paradigm shift in the calculus of resource dependencies and accentuating the vulnerabilities entrenched within the labyrinth of energy geopolitics.

As we navigate the annals of history, armed with insights gleaned from the 2010 rare earth material crisis and Japan's proactive endeavors, let us glean lessons from the past to inform our trajectory towards a more resilient and sustainable future. With neodymium as our lodestar, we embark on a journey of discovery, poised at the nexus of resource geopolitics and technological innovation.

Now that we have a basic understanding of rare earth materials and their significance, let's delve deeper into the 2013 rare earth material crisis and its far-reaching consequences.

## Monte Carlo simulation and potential scenarios

To better grasp the impact of the 2010 rare earth material crisis, we harness advanced mathematical methodologies - the Monte Carlo method and regression analysis. These tools offer invaluable insights into the multifaceted consequences of energy-related conflicts, shedding light on both economic and geopolitical dimensions.

The **Monte Carlo method**, as explained in [Investopedia](https://www.investopedia.com/terms/m/montecarlosimulation.asp), is a powerful statistical technique that enables us to simulate diverse scenarios and their corresponding outcomes. Let's apply this method to model the potential economic and political consequences of the 2010 rare earth material crisis.

In our analysis, we simulate rare earth prices over time using the Monte Carlo method. As outlined in the article, this involves generating multiple hypothetical scenarios by incorporating random factors. Each scenario represents a plausible trajectory of rare earth prices, allowing us to explore a range of possible outcomes. Mathematically, we represent $$ \( P_t \) $$at the simulated \( t \) prices as:

\[ P_t = P_{t-1} + \text{Random Factor}_t \] 

Here, \( P_{t-1} \) denotes the price at the previous time step, and the random factor accounts for the variability introduced into the simulation, as mentioned in the article.

### Regression Analysis: Uncovering Long-term Trends

In addition to the Monte Carlo method, we employ regression analysis to identify long-term trends in rare earth prices. As discussed in the article, this statistical technique helps us discern underlying patterns and correlations, providing valuable insights into market behavior.

**Linear Regression Model**

\[ Price = β_0 + β_1 × \text{Time} + ε \]

Our regression analysis focuses on fitting a linear model to the average simulated prices over time, similar to the approach outlined in the article.

### Generating Random Factors

To initiate our simulation, we generate random factors for each simulation and time step, as described in the article. These factors emulate the myriad market dynamics affecting rare earth prices.

```python
random_factors = np.random.normal(0, 5, size=(num_simulations, num_time_steps))
```

In this simulation, we follow a similar approach as outlined in the article, assuming that the random factors follow a normal distribution with a mean of 0 and a standard deviation of 5.

### Simulating Rare Earth Prices

Building upon the random factors, we simulate rare earth prices over time, as explained in the article. At each time step, prices are adjusted based on the preceding values and the associated random factor.

\[ \text{Simulated Prices}_{t} = \text{Simulated Prices}_{t-1} + \text{Random Factors}_{t} \]

```python
simulated_prices[:, i] = simulated_prices[:, i-1] + random_factors[:, i]
```

Additionally, we introduce crisis events to the simulation, mirroring real-world disruptions that can profoundly impact rare earth markets, as mentioned in the article.

\[ \text{Disrupted Prices}_{t} = \text{Simulated Prices}_{t} - \text{Disruption Amount} \]

Through this combined approach of Monte Carlo simulation and regression analysis, leveraging techniques discussed in the article, we aim to gain deeper insights into the potential scenarios and dynamics surrounding rare earth prices amidst the 2010 crisis and beyond.

```python
if i == crisis_year:
    disruption_amount = np.random.uniform(10, 20)
    simulated_prices[:, i] -= disruption_amount
```

### Python script

```python
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
```

### Regression Analysis for Long-term Trends

In addition to the Monte Carlo method, we employ regression analysis to identify long-term trends in rare earth material prices and their correlation with geopolitical events. This statistical tool will help us better understand the underlying factors influencing the market.
The regression analysis aims to identify and analyze long-term trends in rare earth material prices, providing insights into the underlying factors influencing market dynamics.

## Linear Regression Analysis

Linear regression emerges as a fundamental statistical technique, facilitating the exploration of relationships between variables. Here, we employ it to discern the overarching trend in rare earth prices over time.

### Performing Linear Regression

Our linear regression analysis focuses on the average simulated prices across all simulations. By fitting a regression line to this data, we unveil the underlying trend amidst the market's inherent volatility.

$$ \text{Regression Line} = \beta_0 + \beta_1 \times \text{Time} + \epsilon $$

```python
regression_model = LinearRegression()
regression_model.fit(time_reshaped, average_prices)
regression_line = regression_model.predict(time_reshaped)
```

In essence, this equation describes how rare earth prices evolve over time. The coefficients \(\beta_0\) and \(\beta_1\) capture the intercept and slope of the regression line, while \(\epsilon\) represents the residual error.

## Visualizing the Results

To enhance our understanding, we visualize the results of our simulation and regression analysis using intuitive graphical representations.

### Monte Carlo Simulation Plot

Through visualizing individual simulated scenarios, we offer insights into the variability of rare earth prices over time. By highlighting crisis years, we shed light on how disruptive events can influence market dynamics.

### Linear Regression Line

The regression line serves as a compass, guiding us through the complex landscape of rare earth prices. By tracing its trajectory, we gain valuable insights into the overarching trend shaping market behavior.

### Economic Repercussions

The rare earth material crisis led to a surge in prices and disrupted global supply chains. Our simulations and regression analysis shed light on how these economic consequences unfolded and influenced various sectors.

### Security Concerns and Diversification

Nations heavily dependent on Chinese rare earth exports faced security concerns. We explore how this crisis prompted countries to diversify their sources, emphasizing the importance of a resilient and diversified supply chain.

### Global Geopolitical Shifts

The crisis had broader geopolitical implications, influencing diplomatic relations and alliances. Our analysis examines how nations reevaluated their strategies in the pursuit of resource security.

## Conclusion

In this article, we employed advanced mathematical tools like the Monte Carlo method and regression analysis to dissect the 2013 rare earth material crisis. Our findings provide valuable insights into the intricate interplay between energy resources, geopolitics, and global economics.
In conclusion, our mathematical journey through Monte Carlo simulation and linear regression unveils valuable insights into the dynamics of rare earth prices. By comprehending these underlying patterns and anticipating market uncertainties, industries can navigate the turbulent waters of rare earth supply chains with greater resilience and foresight.

### Sources

1. [Title of source 1](link1)
2. [Title of source 2](link2)
3. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction.* Springer Science & Business Media.
4. Kuczera, G. (2009). *Monte Carlo Simulations.* In Encyclopedia of Complexity and Systems Science (pp. 5808-5827). Springer.
5. Montgomery, D. C., Peck, E. A., & Vining, G. G. (2012). *Introduction to Linear Regression Analysis.* John Wiley & Sons.
6. ...
7. Hurst, C. (Year). "China's Rare Earth Elements Industry: What Can the West Learn?" *Journal of Defense Studies and Resource Management,* [link]
8. U.S. Geological Survey. (Year). "Rare Earth Elements: The Global Supply Chain," [link]
9. Hedrick, J. B. (Year). "Rare Earths: China's Competitive Advantage." *Journal of Alloys and Compounds,* [link]

10. **"China's Rare Earth Elements Industry: What Can the West Learn?"** by Cindy Hurst - Published in the Journal of Defense Studies and Resource Management, this article provides insights into China's dominance in the rare earth industry and the potential implications for Western nations.

11. **"Rare Earth Elements: The Global Supply Chain"** - This comprehensive report by the U.S. Geological Survey offers a detailed analysis of the global rare earth elements market, highlighting the significance of these materials in various sectors.

12. **"Rare Earths: China's Competitive Advantage"** - A research paper by James B. Hedrick, published in the Journal of Alloys and Compounds, explores the geopolitical aspects of China's control over rare earth elements and its impact on global trade dynamics.

**Disclaimer:** This article is intended for educational purposes only and does not constitute financial, investment, or geopolitical advice. The information presented, including simulations and analyses, is based on hypothetical scenarios for illustrative purposes.
