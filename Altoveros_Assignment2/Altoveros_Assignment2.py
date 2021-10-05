# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 17:37:27 2021

@author: ialto
"""

import pandas as pd
import os, glob
import csv


path = "D:\School\CS\CS478\HW"

all_files = glob.glob(os.path.join(path, "companylist-*.csv"))
df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
df_merged   = pd.concat(df_from_each_file, ignore_index=True)

sorted_df = df_merged.sort_values(by=["Symbol"], ascending = True)
sorted_df.to_csv( "merged.csv")


sorted_df_marketCap = sorted_df.sort_values(by=["MarketCap"], ascending = False)


sorted_df_marketCap.to_csv("sortedMarketCap.csv")


df = pd.read_csv("sortedMarketCap.csv", skiprows = 0, nrows = 15)

df.to_csv("marketcap.csv")


stockSymbol = input('Enter the stock symbol to find: \n')
missing = True

csv_file = csv.reader(open('merged.csv', "r"), delimiter = ",")

for row in csv_file:
    if stockSymbol == row[1]:
        print(row)
        missing = False
        
if missing:
    print("Not Found")



