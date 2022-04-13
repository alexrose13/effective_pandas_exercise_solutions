#!/usr/bin/env python
# coding: utf-8

# # Chapter 5 Series Deep Dive

# In[1]:


import pandas as pd
import warnings


# In[2]:


url = 'https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip'

with warnings.catch_warnings(): #a quick bit of code to surpress warnings that pop up due to ambiguous data types in this dataset.
    warnings.simplefilter("ignore")
    df = pd.read_csv(url)

city_mpg = df.city08


# In[3]:


city_mpg


# ## Exercise 1

# > Explore the documentation for five attributes of a series from Jupyter

# This produces a rather lengthy bit of output. As such, I've truncated it here.

# In[4]:


dir(city_mpg)[:20]


# I chose somewhat arbitrarily to look at:
#  * [`to_dict`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html)
#  * [`is_monotonic`](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic.html)
#  * [`resample`](https://pandas.pydata.org/docs/reference/api/pandas.Series.resample.html)

# ## Exercise 2

# > How many attributes are found on the .str attribute? Look at the documentation for three of them.

# In[5]:


s_str = pd.Series(['a','b','c'])

n_attributes = len(dir(s_str.str))

print('There are {} attributes foiund on the .str attribute'.format(n_attributes))


# I chose somewhat arbitrarily to review the following:
#  * [`str.lower()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html)
#  * [`str.lstrip()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lstrip.html)
#  * [`str.find()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.find.html)

# ## Exercise 3

# > How many attributes are found on the .dt attribute? Look at the documentation for three of them.

# In[6]:


s_ts = pd.to_datetime(pd.Series(['2022-01-01','2022-01-02','2022-01-03']))

n_attributes = len(dir(s_ts.dt))

print('There are {} attributes foiund on the .dt attribute'.format(n_attributes))


# Once more, I chose somewhat arbitrarily to review the following:
#  * [`dt.date`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.date.html)
#  * [`dt.days_in_month`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.days_in_month.html)
#  * [`dt.tz`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz.html)
