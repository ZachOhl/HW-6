#!/usr/bin/env python
# coding: utf-8

# In[30]:


def delete_keys(list , dictionary):  
    for x in list:
        dictionary.pop(x)
    return dictionary
        
        
dict = {"firstname": "Mohamed", "lastname": "Farag", "birthyear": 1990, "nationality": "Eqyptian"}

print(delete_keys(["lastname", "birthyear"], dict))

