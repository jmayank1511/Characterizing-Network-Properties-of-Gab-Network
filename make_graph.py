#!/usr/bin/env python
# coding: utf-8

# In[1]:


import igraph
from igraph import *


# In[2]:

import json
json1_file = open('user_follower_following.json')
json1_str = json1_file.read()
partialData = json.loads(json1_str)


# In[52]:


import pickle
# In[5]:



# In[66]:
users = set()

list1 = []
for i in partialData:
    if(len(partialData[i]["follower"])!=0):
        #print(partialData[i]["follower"])
        for j in partialData[i]["follower"]:
            list1.append((i,j[1]))
            users.add(i)
            users.add(j[1])
allUsers=list(users)
    


# In[64]:


#g = Graph(directed=True)
#g.add_vertices(allUsers)
#g.add_edges(list1)


with open("allUsersData_degree_distribution.pkl", "wb") as o:
    pickle.dump(allUsers, o)

# In[67]:

#with open("graph.pkl","wb") as o:
#    pickle.dump(g,o)
