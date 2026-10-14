# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 10:11:15 2024

@author: brand
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt      #importing everything
from scipy.optimize import curve_fit



dataframe = pd.read_csv('data_files/countries.csv')  # setting up data again

x = (0, 1.0)   # variables for x and y to make the straight line on lorenz curve
y = (0, 1.0)   # the straight line will represent the line of equality, or a gini of zero

gdp = dataframe.UN_GDP  # using our gdp data

pop = dataframe.Population  # using population data 

lorenz = 1*(gdp.cumsum() / gdp.sum()) # cumulative sum / sum using gdp data
# here gdp.cumsum will make a list of 212 values for the 212 countries.the list will be all of the gdps slowly added up. they will then each be divided by the gdp.sum.
# lorenz is now a list of values ranging from 0 - 1
# These values in lorenz represent the total cumulative percentage of the world gdp

lorenz_pop = 1*(pop.cumsum() / pop.sum()) # Here we basically do the same thing as above but with population data instead of gdp

#plt.scatter(lorenz, np.arange(start=1, stop=213)/(212), marker='o', color='red') # scatterplot where our lorenz from above is x coordinate, and our np.arrange makes the y    
# The np arrange is used in the same way we had our gini set up. It makes a list from 1-212 for all of the countries.
# It is then divided by the total amount of countries, 212.
# This makes a similar list of values from 0 - 1, representing the cumulative share of population

def lorenz_eq(z, m, n):    # Formula for curve fit
    return m*z**n          

x_range = np.linspace(0, 1)  # The range goes from 0 to 1, or 0 to 100 percent

popt, pcov = curve_fit(lorenz_eq, lorenz, lorenz_pop,) # setting up covariance of perameters and optimal perameters. lorenz and lorenz_pop again in x and y.


lorenz_model = lorenz_eq(x_range, popt[0], popt[1])  # setting up model with optimal perameters

plt.plot(x_range, lorenz_model, '-r', label='Rank vs 200 words')   # plotting curve fit line
plt.xlabel("Cumulative share of population")    # x-axis label
plt.ylabel("Cumulative share of world GDP")  # y-axis label
plt.title("Lorenz Curve to Visualize Inequality") #plot label
plt.scatter(lorenz, lorenz_pop, marker = 'o', color = 'red')  # plotting scatter information
plt.plot(x, y, color='k') # making the perfect equality line. in a hypothetical scenario where this line would represent the gini, everyone in the world would have the same income


# We have now made our graph for cumulative share of world GDP vs cumulative share of population.

# We will make our choropleth on the jupyter notebook file










