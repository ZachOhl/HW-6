#!/usr/bin/env python
# coding: utf-8

# In[120]:


class Node(object):    #the (object) is for clarity. tells you it can accept object. will work the 
                        #without specifying that
    def __init__(self, data):
        self.data = data
        self.next = None


# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Print the linked list
    def print_list(self):
        if self.head == None:   #check if eempty
            raise ValueError("List is empty")

        current = self.head   #if not empty, make head = current node
        while current:   #traverse the list. if theres a node, 
            print(current.data, end="  ")     #if so, print the data of the node, 
            current = current.next     #then make the current node equal to the next node
        print("\n")

    # Find length of Linked List
    def size(self):
        if self.head == None:
            return 0

        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        return size

    # Insert a node in a linked list (AT THE END of the list)
    def insert(self, data): 
        node = Node(data)
        current = self.head   #current is the node. contains data and containts next
        if not current:  #check if empty
            self.head = node
        else:
            while (current.next):       #navigate to last node
                current = current.next  #by checking if current is empty, if not keep looping. 
                            #current.next is a node - it is also a pointer to a node(?)
            current.next = node   #when reach the end, assign data youre inserting to the current
            
#IN CLASS EXERCISE:         
    # Insert a node at BEGINNinG a linked list. check if correct
    #
    def insert_beg(self, data):  #Inserting new 'data' into LL 'self'
        newnode = Node(data)        #define node data type using inserted data
        newnode.next = self.head    #set pointer of newly defined node as pointing to current LL (self)'s head
        self.head = newnode         #set head of LL (self) equal to newly created node w/ 'data' in it
        
#ALT VERSION:
    def insert_at_begin(self, data):
        new_node = Node(data)
        old_head = self.head
        self.head = new_node
        self.head.next = old_head     #self.head.next -> this is ok i guess



    # Delete a node in a linked list
    def delete(self, data):
        if not self.head:
            return

        temp = self.head

        # Check if head node is to be deleted
        if self.head.data == data:
            self.head = temp.next
            #print("Deleted node is " + str(self.head.data))
            return

        while temp.next:
            if temp.next.data == data:
                #print("Node deleted is " + str(temp.next.data))
                temp.next = temp.next.next
                return
            temp = temp.next
        print("Node not found")
        return

    
#plan: 
#1. sort list using exercise 3 function
#2. iterate thru list, find when current = current.next
    #a. delete one of them when this happens
    #b. start over after deletion
#3 repeat #2 until no duplicates
#^nope - doesn't work because delete function doesnt work

#plan 2:
#separte function that #checks if duplicates exist
#if above returns true
#store node 1 value
    #look thru rest of list for duplicates. delete if so
#store node 2 value
    #same as above
#repeat steps n (list size) times
#check for duplicates - repeat if so



    def remove_dups(self):
        if self.is_dups() == False:    #if no duplicates, exit func
            return
        else:                         #if yes duplicates, find one, delete it then call function again
            x = self.find_dup()
            self.delete(x)
            self.remove_dups()  


    def is_dups(self):
        nodes_list = self.linked_to_regular_list()    #convert linked to regular list to check for duplicates
        if (len(set(nodes_list)) == len(nodes_list)):  #check if length of list equals lenght of list as a set
            return False                             #if so -> no duplicates
        else: 
            return True                              #if no -> yes duplicates

        
    def find_dup(self):     
        nodes_list = self.linked_to_regular_list()  #convert to regular list
            
        first_dup = None                         #use regular list to search for first duplicate
        index = 0
        unique_list = []
        while (first_dup == None):               # loop while first duplicate hasn't been found
            if nodes_list[index] not in unique_list:   #check if item is in new unique list already. if not then append it
                unique_list.append(nodes_list[index])
            else:                                          #if it is, thats the duplicate
                first_dup = nodes_list[index]
            index += 1
        return first_dup                         #return the first duplicate value
        
        
    def linked_to_regular_list(self):
        nodes_list = []
        current = self.head
        while (current):                      #look thru LL from and add data one at a time
            nodes_list.append(current.data)   #linked list becomes regular list
            current = current.next
        return nodes_list                     #return regular list
                            


# In[121]:


LLL = LinkedList(Node(11))  
LLL.insert(3)
LLL.insert(6)
LLL.insert(3)
LLL.insert(11)
LLL.insert(6)
LLL.insert(5)
LLL.insert(7)
LLL.insert(5)

print("the linked list is:")
LLL.print_list()

LLL.remove_dups()    

print("after removing duplicates, the linked list is:")
LLL.print_list()


# In[ ]:




