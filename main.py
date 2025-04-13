#Importing necesary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3D
#Create dictionaries to store the data of countries

countries = {
    "Austria": {"r":0.195,"N":14700},
    "Italy": {"r":0.099,"N":216600},
    "Netherlands": {"r":0.114,"N":42580},
    "Switzerland": {"r":0.163,"N":28400},
    "Turkey": {"r":0.144,"N":133700}
}

#Initialize the days of analysis
days = 31

#Initial amount of people infected
initial_infected = 10
#Storing the results in "results"
result = {}

#Iterate through the dictionary
for country,values in countries.items():
    r = values ["r"]
    N = values ["N"]
    y = [initial_infected]

    #for each day with the 31 days
    for day in range(days):
        prev = y[-1]
        next_value = prev + r * prev * (1-prev/N)
        y.append(next_value)

    result [country] = y

plt.figure(figsize=(10,6))
for country, y_values in result.items():
    plt.plot(range(len(y_values)), y_values, label=country)

plt.xlabel("Days")
plt.ylabel("Number of Infected Cases")
plt.title("Covid-19 Infection Spread (Logistic Growth Model)")
plt.legend()
plt.grid(True)
plt.show()

#Creating 3D graph model to analyze infected cases.
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for idx, (country, y_values) in enumerate(result.items()):
    x = list(range(len(y_values)))
    y = [idx] * len(y_values)
    z = y_values
    ax.plot(x, y, z, label=country)

ax.set_xlabel('Day')
ax.set_ylabel('Country Index')
ax.set_zlabel('Number of Infected Cases')
ax.legend()
plt.show()