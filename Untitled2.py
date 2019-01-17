
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


Location = "datasets/DC_Properties.csv"
df = pd.read_csv(Location)

df.head()


# In[18]:


df.corr()


# In[6]:


import statsmodels.formula.api as smf


# In[20]:


result = smf.ols('ROOMS ~ PRICE + BEDRM + FIREPLACES + KITCHENS', data=df).fit()


# In[21]:


result.summary()

