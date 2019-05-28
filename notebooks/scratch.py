#!/usr/bin/env python
# coding: utf-8

# In[7]:


li = [1, 2, 3, 5, 8, 10, 55, -19989]
print(set(filter(lambda x: x%2 == 1, li)))


# In[6]:


li = set([1, 1, 1, 2, 3, 5, 8, 10, 55, -19989])
print(li)

