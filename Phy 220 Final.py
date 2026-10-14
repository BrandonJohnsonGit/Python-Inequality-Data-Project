#Physics 220 Final Project

#Brandon Johnson

#Country and GDP Data



# We will start by importing our libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# We will now set up our dataframe

dataframe = pd.read_csv('data_files/countries.csv')

# We have read in our dataframe

# We will now make a scatterplot of GDP vs Population

# To do this we will use our dataframe that we read above


plt.figure(figsize=(9,5))
plt.scatter(dataframe.Population, dataframe.UN_GDP)  # setting up axis
plt.xlabel('Population')
plt.ylabel('GDP')            # labeling axis
plt.xlim((0, dataframe.Population.max() * 1.1))   # making axis limits
plt.ylim((0, dataframe.UN_GDP.max() * 1.1))   # limits slightly more than the maximum
plt.show()   # showing scatterplot

# Now we will make a histogram that will show GDP Per Capita

dataframe['per_capita'] = dataframe['GDP_per_capita']
dataframe.per_capita.hist(range=(0,200000),bins=125)   # setting up histogram
plt.xlabel('GDP Per Capita')
plt.ylabel('Amount of Countries')   # making/naming axis 

# Both of our graphs have been displayed

# Now we will work with the Gini Coefficient


# We will have a function that finds the gini coefficient

def ginico(x):   # The input (x) will be, in this case, our gdp per capita data.
    x = np.sort(x) # sorted from least to greatest
    countries = np.arange(start=1, stop=213) # amount of countries in data, goes from 1 - 212. These values will be in an array.
    return ((np.sum((2 * countries - countries.max() - 1) * x)) / (countries.max() * np.sum(x))) # calculating gini using formula, where x is the gdp per capita, countries.max() is the total number of countries, and countries is an array from 1 - 212.
    # the np.sum with countries will run through the calculation for each value 1 - 212 and then sum them. This is why countries had to be an array.

ginico(dataframe.GDP_per_capita)  # using function on gdp per capita from dataset

# Now we have found the gini coefficient, or 0.636024519935164.

# We will now graph cumulative share of world GDP vs cumulative share of population

# This is continued on the next document






