#!/usr/bin/env python
# coding: utf-8

# # Chapter 4 Categorical Data

# In[1]:


import pandas as pd


# ## Exercise 1

# > Using Jupyter,  create a series with the temperature values for the last seven days. Filter out the values below the Mean

# The [US National Weather Service](https://www.weather.gov) has some basic charts and data that are readily available. I'll use the page dedicated to [Salt Lake City](https://www.weather.gov/slc/Cliplot), the capital of my state and grab some data.

# In[2]:


#creating a series with temperature values from the last seven days
slc_temps_hi = pd.Series(
    [34, 40, 46, 55, 56, 55, 47],
    name = 'slc_temps_hi'
)


# In[3]:


#creating a boolean array to use as a filtration mask
mask = slc_temps_hi > slc_temps_hi.mean()

#we'll display the bool array for good measure
mask


# In[4]:


#now we'll use the mask as a filter to display only values from `slc_temps_hi` that are above the average value of the series
slc_temps_hi[mask]


# ## Exercise 2

# > Using Jupyter, create a series with your favorite colors. Use the categorical type.

# I've always been purple, black, red, and pink. I'll build a series to reflect that. Note that there are (at least) two very simple ways to to do this. I'll include both methods below.

# In[5]:


#method 1
fav_colors = pd.Series(
    ['purple', 'black', 'red', 'pink'],
    name = 'favorite_colors',
    dtype='category'
)

fav_colors


# In[6]:


#method 2
fav_colors2 = pd.Series(
    ['purple', 'black', 'red', 'pink'],
    name = 'favorite_colors'
).astype('category')

fav_colors2


# In[ ]:




