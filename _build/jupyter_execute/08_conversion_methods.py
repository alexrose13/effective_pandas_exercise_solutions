#!/usr/bin/env python
# coding: utf-8

# # Chapter 8 Conversion Methods

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


url = 'https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip'

df = pd.read_csv(url, usecols = ['city08', 'fuelType1'])
city_mpg1 = df.city08
fuel_type1 = df.fuelType1


# ## Exercise 1

# > Convert a numeric column to a smaller data type

# In[3]:


city_mpg1.dtype


# In[4]:


city_mpg2 = city_mpg1.astype('int16')


# In[5]:


city_mpg2.dtype


# ## Exercise 2

# > Calculate the memory savings by converting to a smaller numeric types.

# In[6]:


mem_delta_cty_mpg = city_mpg2.memory_usage(deep=True) - city_mpg1.memory_usage(deep=True)

print('By converting the data type of the `city_mpg1` series we have successfully altered the amount of memory required to store this infomration by {} bytes.'.format(mem_delta_cty_mpg))


# ## Exercise 3

# > Convert a string column into a categorical type

# In[7]:


fuel_type1.dtype


# In[8]:


fuel_type2 = fuel_type1.astype('category')


# In[9]:


fuel_type2.dtype


# ## Exercise 4

# > Calculate the memory savings by converting to a categorical type.

# In[10]:


mem_delta_cty_mpg = fuel_type2.memory_usage(deep=True) - fuel_type1.memory_usage(deep=True)

print('By converting the data type of the `fuel_type1` series we have successfully altered the amount of memory required to store this infomration by {} bytes.'.format(mem_delta_cty_mpg))

