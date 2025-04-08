#!/usr/bin/env python
# coding: utf-8

# In[2]:


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

print("I am in fibo.py file")

print("My __name__ is:", __name__)


# In[ ]:




