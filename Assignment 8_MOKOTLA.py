# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 08:06:11 2024

@author: Lenovo
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Read the contents of the CSV file into a dataframe
file_path = 'C:/CCSC 7900/FAOSTAT/FAOSTAT_data.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Step 2: Extract lettuce "Area harvested" and "Yield" to a new dataframe
lettuce_data = df[(df['Item'] == 'Lettuce and chicory') & 
                  (df['Element'].isin(['Area harvested', 'Yield']))]

# Pivoting the dataframe to have 'Year' as index and 'Area harvested' and 'Yield' as columns
lettuce_pivot = lettuce_data.pivot_table(index='Year', 
                                         columns='Element', 
                                         values='Value', 
                                         aggfunc='first').reset_index()

# Step 3: Convert the filtered data to a NumPy array with columns "Year", "Area harvested", and "Yield"
lettuce_numpy = lettuce_pivot[['Year', 'Area harvested', 'Yield']].to_numpy()

# Step 4: Identify the years with the maximum and minimum yield
max_yield_year = lettuce_pivot.loc[lettuce_pivot['Yield'].idxmax(), 'Year']
min_yield_year = lettuce_pivot.loc[lettuce_pivot['Yield'].idxmin(), 'Year']
print(f'Maximum yield occurred in {max_yield_year}')
print(f'Minimum yield occurred in {min_yield_year}')

# Step 5: Calculate the annual deviations (anomalies) for "Yield" only
mean_yield = lettuce_pivot['Yield'].mean()
lettuce_pivot['Yield Anomaly'] = lettuce_pivot['Yield'] - mean_yield

# Save the yield anomalies to a new CSV file
lettuce_pivot[['Year', 'Yield Anomaly']].to_csv('lettuce_yield_anomalies.csv', index=False)
print('Yield anomalies saved to lettuce_yield_anomalies.csv')

# Step 6: Plot a time series of the area harvested
plt.figure(figsize=(10, 6))
plt.plot(lettuce_pivot['Year'], lettuce_pivot['Area harvested'], marker='o')
plt.title('Lettuce Area Harvested Over Time')
plt.xlabel('Year')
plt.ylabel('Area harvested (ha)')
plt.grid(True)
plt.show()

# Step 7: Plot a time series of yield anomalies
plt.figure(figsize=(10, 6))
plt.plot(lettuce_pivot['Year'], lettuce_pivot['Yield Anomaly'], marker='o', color='red')
plt.title('Lettuce Yield Anomalies Over Time')
plt.xlabel('Year')
plt.ylabel('Yield Anomaly')
plt.grid(True)
plt.show()
