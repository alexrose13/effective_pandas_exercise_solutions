#!/usr/bin/env python
# coding: utf-8

# # Chapter 6 Operators (& Dunder Methods)

# Per usual we'll import a few packages

# In[1]:


import pandas as pd
import numpy as np


# And generate a quick numerical series. One that starts at 0 (inclusive), increments by 2, and stops at 22 (non-inclusive).

# In[2]:


s = pd.Series(np.arange(start = 0, stop = 22, step = 2))
s


# ## Exercise 1

# > Add a numeric series to itself

# In[3]:


s + s


# ## Exercise 2

# > Add 10 to a numeric series

# In[4]:


s + 10


# ## Exercise 3

# > Add a numeric series to itself using the `.add` method.

# In[5]:


s.add(s)


# ## Exercise 4

# > Read the documentation for the `.add` method.

# Follow [this link](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add.html) to read the documentation of the `.add` method.
