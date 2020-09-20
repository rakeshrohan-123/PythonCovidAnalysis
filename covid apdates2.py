#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import requests
def getStats(country):
  api_url = 'https://api.smartable.ai/coronavirus/stats/'+country
  api_params = {
    'Cache-Control': 'no-cache',
    'Subscription-Key': 'a6499014767b428eb59db92affbaf181',
  }
  r = requests.get(url=api_url, params=api_params) 
  return r.text

data = getStats('IN')


# In[12]:


import simplejson as json
jsonData = json.loads(data)
jsonData.keys() 


# In[13]:


country = jsonData['location']['countryOrRegion']
country


# In[14]:


jsonData['updatedDateTime']


# In[15]:


jsonData['stats']['breakdowns']
latestData = jsonData['stats']['breakdowns'][0]
latestData['newDeaths'] 


# In[16]:


history = pd.DataFrame(jsonData['stats']['history'])
history['date']=pd.to_datetime(history['date'])
history


# In[17]:


history.plot(figsize=(10,5), x='date', title=country)


# In[18]:


history['ddeaths']=history['deaths'].pct_change()*100
partialhistory = history[40:70]
partialhistory.plot(x='date',y='ddeaths',figsize=(10,5))


# In[ ]:




