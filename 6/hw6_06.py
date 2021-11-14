#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Node(object):    #the (object) is for clarity. tells you it can accept object. will work the 
                        #without specifying that
    def __init__(self, data):
        self.data = data
        self.prev = None

# Class to create a Linked List
class ReversedLinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail

    # Print the linked list
    def print_list(self):
        if self.tail == None:   #check if eempty
            raise ValueError("List is empty")

        current = self.tail   #if not empty, make tail = current node
        while current:   #traverse the list. if theres a node, 
            print(current.data, end="  ")     #if so, print the data of the node, 
            current = current.prev     #then make the current node equal to the prev node
        print("\n")
            
    def insert(self, data):  #insert on left
        new_node = Node(data)
        old_tail = self.tail
        self.tail = new_node
        self.tail.prev = old_tail     

    # Delete a node in a linked list
    def delete(self, data):
        if not self.tail:
            return
        temp = self.tail
        # Check if tail node is to be deleted
        if self.tail.data == data:
            self.tail = temp.prev  
            print("Deleted node is " + str(self.tail.data))
            return
        while temp.prev:
            if temp.prev.data == data:
                print("Node deleted is " + str(temp.prev.data))
                temp.prev = temp.prev.prev
                return
            temp = temp.prev
        print("Node not found")
        return
    
    def search(self, data):
        current = self.tail
        #test = False
        while (current.prev):            
            if current.data == data:
                return True 
            current = current.prev
        return False                     


# In[12]:


first_node = Node(11)
RLL = ReversedLinkedList(first_node)
RLL.insert(3)
RLL.insert(6)
RLL.insert(5)

print("The Reversed Linked List is (after insertion):")
RLL.print_list()

RLL.delete(6)

print("The Reversed Linked List is (after deleting 6):")
RLL.print_list()

print("Does 5 exist in the Reversed Linked List")
print(RLL.search(5))

print("Does 17 exist in the Reversed Linked List")
print(RLL.search(17))


# In[ ]:




