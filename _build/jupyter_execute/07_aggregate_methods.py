#!/usr/bin/env python
# coding: utf-8

# # Chapter 7 Aggregate Methods

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


url = 'https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip'

df = pd.read_csv(url, usecols = ['city08'])
city_mpg = df.city08


# ## Exercise 1

# > Find the count of non-missing values of a series.

# In[3]:


city_mpg.count()


# ## Exercise 2

# > Find the number of entries of a series.

# In[4]:


city_mpg.size


# ## Exercise 3

# > Find the number of unique entries of a series

# In[5]:


city_mpg.nunique()


# In[6]:


city_mpg.nunique(dropna=True)


# ## Exercise 4

# > Find the mean value of a series

# In[7]:


city_mpg.mean()


# ## Exercise 5

# > Find the maximum value of a series.

# In[8]:


city_mpg.max()


# ## Exercise 6

# > Use the .agg method to find all of the above.

# In[9]:


city_mpg.agg(['count', 'size', 'nunique', 'mean', 'max'])

