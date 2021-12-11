#!/usr/bin/env python
# coding: utf-8

# In[8]:


x=int(input('enter the value of x:'))
n=int(input('enter the value of n:'))
class Power():
    def power(self,x,n):
        self.x=x
        self.n=n
        return x**n
pow1=Power()
pow1.power(x,n)


# In[ ]:




