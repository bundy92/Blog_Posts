# Geopolitics of Energy: Unraveling the Dynamics of Energy-Driven Conflicts

## Introduction

Welcome! In this series we plan to explore some of current global geopolitical events with some added scientific background. Let's start our first article with quite an important topic the black gold! As we know crude oil trade in the prime example of a complex relationship between energy resources and geopolitics. Many significant global events these days revolve around these resources. Particularly crude oil and natural gas. In this post, we focus on the critical Strait of Hormuz and its implications of energy-related conflicts.

## 1. Energy as a catalyst for geopolitical conflicts

The topic of energy and geopolitics is an arena where access, control, and distribution of energy resources often become the theatre for international tensions. One of the most critical geopolitical hotspots is the Strait of Hormuz, a strategic waterway connecting the Persian Gulf to the Gulf of Oman and the Arabian Sea. - I can recommend it as a holiday destination if you happen to like deserts!
 This shipping lane is amongst the most important ones of the world. Since the 1970's, when international oil trade from the Middle-East started to gain significance. This area is in constant pressure from conflicting local and global powers. Such as the USA and the Islamic Republic of Iran. However, following the reignited war between Israel and the Hamas terrorist group in the Gaza Strip, the pressure on shipping lanes shifted to the Red Sea area.

## 2. The Strait of Hormuz event

In our short Python simulation, we describe potential scenarios and their impacts on global oil supply and prices.
 Here we aim to model the potential impacts on global oil supply and prices if the strait experiences disruptions due to regional tensions. If we turn on the TV we may see, that happens quite often. Not a big suprise considering the general tension in the Gulf region. This scenario is particularly relevant as the strait is a vital passage for oil transportation, with a significant portion of the world's oil trade passing through its narrow waters from said Gulf states. Note that this is not an exhaustive simulation. You may consider one variables and factors. Such as the OPEC council decisions, US embargoes, global Black Swan events, etc.

## 3. Python Simulation

To simulate this scenario, we employ a simple Python script that models disruptions in the Strait of Hormuz over a one-year period. The simulated global oil supply, represented in million standard barrels per day, is subjected to disruptions introduced at a specified point in time.
We employ NumPy as a standard fast mathematical library and Matplotlib to visualize our results. Don't forget to install them locally or into your virtual environment.  
First we make numpy vector to represent our year of simulation. Next populate a random vector for our daily oil supply for that year. Using normal distribution. Here the normal distribution only implies that the daily supply fluctuated around a mean value. In reality that could change drastically. Then start to disrupt our supply in the first quarter of the year. There are many options to tailor this for your liking. 250 for business days or change the disruption for random days. For instance you may introduce a stabilized or even constantly declining price window as well.
After the disruption event we daily subtract a uniformly distributed value from the initial supply for the corresponding dates.

```python
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
```

## 4. Analysis of the results

The chart illustrates the potential consequences of a disruption in the oil supply of the Gulf area. As depicted in the graph, the global oil supply experiences a significant drop following the introduction of the disruption in the first quarter. This decline reflects the real-world impact such geopolitical events can have on the energy landscape. Examples like a naval blockade or natural disaster.

## 5. Potential geopolitical implications

**Global Economic Impact:**
 Disruptions in the Strait of Hormuz can lead to a reduction in the global oil supply, resulting in increased oil prices. This may  have cascading effects on economies around the world, harming heavily import reliant nations.
**Regional Tensions:**
 We already highlighted the vulnerability of global energy supply chains to regional geopolitical tensions. Strained relations in the Middle East or any disruptions in the strait can quickly reverberate across the international stage. As happened before when the Iranian navy detained a western oil tanker.
**Energy Security Concerns:**
 Countries heavily dependent on oil imports may face challenges in ensuring energy security during such disruptions. Diversification of energy sources and supply routes becomes critical for mitigating risks for these nations.

## Conclusion

In this simple Strait of Hormuz scenario, we witnessed the potential consequences of a geopolitical crisis on the global oil supply. The script and visual representation shows how disruptions in this single critical chokepoint can lead to significant impacts on the energy landscape, international relations, and global economies. Every single point of this scenario can be extended and expanded. Further and more thorough analysis with comparisons using historical data and advanced methods like machine learning tools might help build more professional model for us.
Later we continue to study the dynamics of energy-driven conflicts and events, future additional scenarios, allowing us to gain a broader view of the such events and forces as they shape the world.
Our next topic of analysis is the Nord Stream pipeline. Feel free to recommend and comment for further subject!
Disclaimer: This article is intended for educational purposes only and does not constitute financial, investment, or political advice. The information presented, including the Python simulation, is based on hypothetical scenarios for illustrative purposes. Any actions taken or decisions made based on the content of this article are at the sole discretion of the reader. The author is not responsible for any consequences resulting from the use or misuse of the information.
