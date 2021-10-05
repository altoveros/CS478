# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 13:51:46 2021

@author: ialto
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/datasets/gdp/0be54c18d900edc37123f25b4eff014731c9e459/data/gdp.csv"

dataset = pd.read_csv(url)


us = dataset[dataset['Country Name'] == 'United States']
eu = dataset[dataset['Country Name'] == 'European Union']
china = dataset[dataset['Country Name'] == 'China']

plt.plot(us.Year, us.Value, color = 'red')
plt.plot(eu.Year, eu.Value, color = 'blue')
plt.plot(china.Year, china.Value, color = 'orange')

plt.legend(["United States", "European Union", "China"])
plt.title("Ian Altoveros's GDP Plot")

plt.xlabel("Year")
plt.ylabel("GDP")
plt.show()
