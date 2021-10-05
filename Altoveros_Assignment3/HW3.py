# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 16:01:25 2021

@author: ialto
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn


url = "https://raw.githubusercontent.com/ebubekiraygun/World-Happiness-Data-on-Python/master/2017.csv"


dataset = pd.read_csv(url)

dataset.columns

dataset = dataset[['Happiness.Rank', 'Happiness.Score', 'Whisker.high', 'Whisker.low', 'Economy..GDP.per.Capita.', 'Family',
                   'Health..Life.Expectancy.', 'Freedom', 'Generosity', 'Trust..Government.Corruption.', 'Dystopia.Residual']]

plt.figure(figsize=(13,13))
seaborn.heatmap(dataset.corr(), annot = True)



#happiness = dataset['Happiness.Score']
#freedom = dataset['Freedom']

#plt.scatter(freedom, happiness, color = 'green')

#plt.title("Ian Altoveros - Freedom vs Happiness.Score")


#plt.legend(["Freedom"])
#plt.xlabel("Freedom")
#plt.ylabel("Happiness Score")
#plt.show()