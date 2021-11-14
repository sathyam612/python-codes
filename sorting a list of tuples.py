#!/usr/bin/env python
# coding: utf-8

# In[11]:


tup =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def sort_tuple(tup):
    n=len(tup)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if (tup[j][-1]>tup[j+1][-1]):
                temp=tup[j]
                tup[j]=tup[j+1]
                tup[j+1]=temp
    return(tup)
print(sort_tuple(tup))


# In[ ]:




