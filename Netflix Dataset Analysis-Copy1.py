#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
data = pd.read_csv(r"C:\Users\KIIT\Downloads\8. Netflix Dataset.csv")


# In[5]:


data


# In[7]:


data.head()


# In[5]:


data.tail()


# In[6]:


data.shape


# In[7]:


data.size


# In[8]:


data.columns


# In[9]:


data.dtypes


# In[10]:


data.info()


# In[8]:


data.head()


# In[12]:


data.shape


# In[14]:


data[data.duplicated()]


# In[16]:


data.drop_duplicates(inplace = True)


# In[17]:


data[data.duplicated()]


# In[18]:


data.shape


# In[19]:


data.head()


# In[20]:


data.isnull()


# In[21]:


data.isnull().sum()


# In[22]:


import seaborn as sns


# In[23]:


sns.heatmap(data.isnull())


# In[24]:


data.head()


# In[9]:


data[data["Title"].isin(['House of Cards'])]


# In[10]:


data[data['Title'].str.contains('House of cards')]


# In[11]:


data.dtypes


# In[13]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[14]:


data.head()


# In[16]:


data.dtypes


# In[18]:


data['Date_N'].dt.year.value_counts()


# In[19]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')


# In[22]:


data.groupby('Category').Category.count()

