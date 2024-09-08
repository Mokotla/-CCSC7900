# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 21:38:48 2024

@author: Lenovo
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir(r'C:\CCSC 7900\QBO')

def read_data(file_path):
    data = pd.read_csv(file_path, sep='\s+', header=None)
    data.replace(-999.90, np.nan, inplace=True)  # Handle missing values
    data.columns = ['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return data

def calculate_monthly_mean(data):
    monthly_means = data.iloc[:, 1:].mean()
    monthly_means_df = pd.DataFrame({'Month': data.columns[1:], 'Mean Index Value': monthly_means})
    return monthly_means_df

def calculate_monthly_std(data):
    monthly_std = data.iloc[:, 1:].std()
    monthly_std_df = pd.DataFrame({'Month': data.columns[1:], 'Standard Deviation': monthly_std})
    return monthly_std_df

def find_min_max(data):
    max_vals = data.iloc[:, 1:].idxmax()
    min_vals = data.iloc[:, 1:].idxmin()
    max_years = data.loc[max_vals, 'Year'].values
    min_years = data.loc[min_vals, 'Year'].values
    max_indices = [data.loc[max_vals[month], month] for month in data.columns[1:]]
    min_indices = [data.loc[min_vals[month], month] for month in data.columns[1:]]
    
    min_max_df = pd.DataFrame({
        'Month': data.columns[1:],
        'Max Year': max_years,
        'Max Index Value': max_indices,
        'Min Year': min_years,
        'Min Index Value': min_indices
    })
    
    return min_max_df

def calculate_annual_mean(data):
    annual_means = data.iloc[:, 1:].mean(axis=1)
    return pd.DataFrame({'Year': data['Year'], 'Annual Mean': annual_means})

def plot_time_series(data):
    plt.figure(figsize=(10, 6))
    for month in data.columns[1:]:
        plt.plot(data['Year'], data[month], label=month)
    plt.xlabel('Year')
    plt.ylabel('Index Value')
    plt.title('Time Series of Monthly Index Values')
    plt.legend(loc='upper right', fontsize='small', ncol=3)
    plt.show()

def plot_monthly_mean(monthly_means):
    months = monthly_means['Month']
    plt.plot(months, monthly_means['Mean Index Value'], marker='o')
    plt.xlabel('Month')
    plt.ylabel('Mean Index Value')
    plt.title('Monthly Mean Index Values')
    plt.show()

def plot_annual_mean(annual_means):
    plt.plot(annual_means['Year'], annual_means['Annual Mean'], marker='o')
    plt.xlabel('Year')
    plt.ylabel('Annual Mean Index Value')
    plt.title('Annual Mean Index Values')
    plt.show()

# Main function to run all tasks
def main():
    file_path = r'C:\CCSC 7900\QBO\QBO INDEX.txt'  
    
    # Step 1: Read the data
    data = read_data(file_path)
    
    # Step 2: Calculate monthly mean
    monthly_means = calculate_monthly_mean(data)
    print("Monthly Means:\n", monthly_means)
    
    # Step 3: Calculate standard deviation for each month
    monthly_std = calculate_monthly_std(data)
    print("Monthly Standard Deviations:\n", monthly_std)
    
    # Step 4: Identify the years with max and min index values for each month
    min_max_df = find_min_max(data)
    print("Years with Maximum and Minimum Index Values:\n", min_max_df)
    
    # Step 5: Calculate annual mean index values
    annual_means = calculate_annual_mean(data)
    print("Annual Means:\n", annual_means)
    
    # Step 6: Plot time series of monthly index values
    plot_time_series(data)
    
    # Step 7: Plot monthly mean index values
    plot_monthly_mean(monthly_means)
    
    # Step 8: Plot annual mean index values
    plot_annual_mean(annual_means)
    
    #closing messege
    print("enjoy the coding")

# Run the program
if __name__ == '__main__':
    main()

