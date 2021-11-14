#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Node(object):    #the (object) is for clarity. tells you it can accept object. will work the 
                        #without specifying that
    def __init__(self, data):
        self.small = None
        self.big = None
        self.toobig = None
        self.data = data
        

    # Insert a node in a tri tree (At the first available spot that it fits criteria)
    def insert(self, data): 
        
        if self.data:

            if (data < self.data):
                if (self.small == None):
                    self.small = Node(data) 
                else:
                    self.small.insert(data)
            elif (data > self.data) and (data < self.data + 10):
                if (self.big == None):
                    self.big = Node(data) 
                else:
                    self.big.insert(data)
            elif (data >= self.data + 10):
                if (self.toobig == None):
                    self.toobig = Node(data) 
                else:
                    self.toobig.insert(data)
        else:
            self.data = data   #if no data in top node, insert there
                    
                    
    def traversal_print(self):
        if self.small:
            self.small.traversal_print()
        print(self.data)
        if self.big:
            self.big.traversal_print()
        if self.toobig:
            self.toobig.traversal_print()  
            
    def traversal_append(self, list):
        if self.small:
            self.small.traversal_append(list)
        list.append(self.data)
        if self.big:
            self.big.traversal_append(list)
        if self.toobig:
            self.toobig.traversal_append(list)
        return list
            
    def delete(self, data):
        temp_list = []
        temp_list = self.traversal_append(temp_list)
        
        temp_list.remove(data)
        
        self.small = None
        self.big = None
        self.toobig = None
        self.data = None
        
        for x in temp_list:
            self.insert(x)

                


# In[8]:


root = Node(20) 
root.insert(40)
root.insert(45)
root.insert(32)

print("Tree contents after insertion using the traversal:")
root.traversal_print()

root.delete(45)

print("Tree contents after deleting 45 using the traversal:")
root.traversal_print()


# In[ ]:




