#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


df = pd.read_excel('Analysis 1.xlsx')
df


# In[6]:





# In[43]:


df_columns=df[['simulant_id','Full Name','age','Full Name of 2030','Age of 2030']]


# In[44]:


df_columns


# In[ ]:





# In[45]:


df_Columns1=df_columns.filter(items=['simulant_id','Full Name','age','Full Name of 2030','Age of 2030']).dropna()


# In[46]:


df_Columns1


# In[47]:


df_Columns1['Comparison'] = df_Columns1['age'] == (df_Columns1['Age of 2030'] - 10)
df2=df_Columns1[df_Columns1['Comparison']]


# In[48]:


df2


# In[49]:


df2.to_excel('result.xlsx', index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




