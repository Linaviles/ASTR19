#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
from tabulate import tabulate
import math

x = np.linspace(0, (math.pi * 2) , 10000)


# In[25]:


def sin(x):
    return np.sin(x)



# In[26]:


def cos(x):
    return np.cos(x)


# My (Lindsay's) **Notebook**
# 
# The function sin() returns a value from 0, 2pi where y is sin(x). Same with the function cos() where is returns a value from cos(x) where x has a range of 0, 2pi. I used the numpy function np.sin and np.cos to compute these values, and for x I created a linear space with the range 0, 2pi with 1000 entries. 

# In[27]:


cos_val = cos(x)
sin_val = sin(x)

data = [(x[i],sin_val[i], cos_val[i]) for i in range(0,1000)]
table_header = ["x","cos(x)", "sin(x)"]
print(tabulate(data, table_header))


# In[28]:


for i in range(10):
    print(f'{x[i]:.2f}, {cos_val[i]:.2f}, {sin_val[i]:.2f}')

