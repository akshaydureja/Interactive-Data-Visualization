#!/usr/bin/env python
# coding: utf-8

# In[48]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[35]:


ds=pd.read_csv("/Users/akshaydureja/Downloads/coursera_data.csv")


# In[36]:


ds.head()


# In[37]:


ds.shape


# In[38]:


sns.heatmap(ds.isnull())


# In[39]:


ds.drop(["Unnamed: 0"],axis=1,inplace=True)


# In[46]:


ds


# In[41]:


ds['course_students_enrolled']= ds['course_students_enrolled'].str.replace('k', '*1000')
ds['course_students_enrolled']= ds['course_students_enrolled'].str.replace('m', '*1000000')


# In[44]:


ds['course_students_enrolled'] = ds['course_students_enrolled'].map(lambda x: eval(x))


# In[45]:


ds


# In[52]:


plt.figure(figsize=(12,10))
plt.hist(ds['course_Certificate_type'])
plt.show()


# In[81]:


import plotly as py
from plotly.offline import iplot
import plotly.tools as tls

import cufflinks as cf

import plotly.graph_objs as go


py.offline.init_notebook_mode(connected=True)
cf.go_offline()


# In[88]:


cf.set_config_file(theme='polar')
ds['course_Certificate_type'].iplot(kind='hist',title='Course Certificate Type',
                                   xTitle='Course Type', yTitle='Counts')


# In[87]:


cf.set_config_file(theme='ggplot')

ds['course_rating'].iplot(kind='hist',title='Course Rating ',bargap=0.2,
                                   xTitle='Rating', yTitle='Counts')


# In[90]:


cf.set_config_file(theme='pearl')
ds['course_difficulty'].iplot(kind='hist',title='Course Difficulty',
                             xTitle='Course Type',yTitle='Count')


# In[91]:


course_org = ds.groupby('course_organization').count().reset_index()

trace = go.Pie(labels = course_org['course_organization'], values =course_org['course_students_enrolled'] )
data = [trace]
fig = go.Figure(data = data)
iplot(fig)


# In[ ]:




