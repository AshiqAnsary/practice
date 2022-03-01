#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pyinstaller')


# In[5]:


print("Geuss number and win price")
import random
n=20
to_be_guessed=int(n*random.random())+1
guess=0
while guess != to_be_guessed:
    guess=int(input("new number :"))
    if guess>0:
        if guess>to_be_guessed:
            print("Number Is too large")
        elif guess<to_be_guessed:
             print("Number Is too small")
    else:
        print("Sorry, that you are giving up")
        break

else :
    print("congratilation you made it")


# In[ ]:




