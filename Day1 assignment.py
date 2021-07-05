#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # numerical 
import pandas as pd # data reading
import seaborn as sns # statistical analysis

import matplotlib as mpl #charts
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', "inline # to avoid 'plt.show' when ploting the graph.")


# In[4]:


## sample examples

x=np.arange(0,10)
y=np.arange(11, 21)


# In[7]:


plt.plot(x,y, 'go--', linewidth=1, markersize=5)
plt.title('Line Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')


# In[11]:


x=np.arange(0, 4* np.pi,0.1)
y=np.sin(x)
plt.title("sine waveform")

#plot the points using matplotlib
plt.plot(x,y, color='r')
plt.show()


# In[14]:


x=np.arange(0,10)
y=x*x
x


# In[15]:


y


# In[17]:


plt.plot(x,y)


# In[21]:


x= [1,2,3,4,5,6,7] # days of week 
y= [160,150,140,145,175,165,185] # sales 


plt.plot(x,y, 'go-', linewidth=1, markersize=5)
plt.title('Line Plot')
plt.xlabel('days of week')
plt.ylabel('sales')
plt.plot(x,y)
plt.show()


# In[ ]:




