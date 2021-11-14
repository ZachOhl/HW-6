#!/usr/bin/env python
# coding: utf-8

# In[36]:


class Queue:
    inner_list = []  #que is made out of a list
    top = 0          #top will point to position that next item gets inserted (back of the que) 
                        #(initiated as zero becuz front = back = 0)
    
    def enqueue(self, value):
        self.inner_list.insert(self.top, value)  #use .insert(index, item) on que's inner list. index is top (back of que)
        self.top = self.top + 1                  #increase top by 1. once first item is inserted, that item's position is 0
                                                    #and top points to pos=1

        
    def dequeue(self):
        value = self.inner_list.pop(0)  #pop the first (0th) item in list (front of the que)
        return value  #return that item

    #Note: function deletes first instance of value 
    def delete(self, value):
        length = 0            #initiate length variable
        delete_index = None   #and deletion index variable
        for x in self.inner_list:                       #Find 'index' of item to be deleted
            if (x == value) and (delete_index == None):  #second logical added so it will 
                delete_index = length                    #delete FIRST instance
            length += 1

        for i in range(length):                    #Loop though queue
            if (i != delete_index):                 #move any item except at the tracked index
                self.enqueue(self.dequeue())        #from the front to the back of the line
            else:
                self.dequeue()                      #move item at the tracked index to nowhere

        
obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.enqueue(7)

obj.delete(7)
print(obj.dequeue()) # Should return 5


# In[35]:


ob1 = Queue()
ob1.inner_list.clear()  #
ob1.enqueue(2)
ob1.enqueue(9)
ob1.enqueue(7)
ob1.enqueue(9)
ob1.enqueue(11)
print(ob1.inner_list)
ob1.delete(9)
print(ob1.inner_list)

