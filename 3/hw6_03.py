#!/usr/bin/env python
# coding: utf-8

# In[71]:


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
            head = temp.next
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

    
#PLAN:  loop n times where n = length of list. 
        # in each loop, find the max from between current spot and the end,  
                # delete from current spot and insert at the beginning (referring to this max by 
                # value, using functions defined already above)
    def sort(self):
        n = self.size()
        current = self.head
        
        for i in range(n): #Loop n times 
            x=self.find_max(current)               #find max from current node to the tail
            
            self.delete(x)                         # delete it from current spot (by value)
            self.insert_at_begin(x)                # insert max at the BEGINNING ()  
                                                   #inserting max of nodes 1 thru n at the beginning, then max of 
                                                   #nodes 2-n at beginning, .... will result in ascending order
            #current = current.next                #don't need to iterate 

            
    def find_max(self, current):     #pass the linked list and a current node. 
        tmp_max=current.data
        while (current.next):                      #look thru LL from current til the end to find temporary max
            if tmp_max < current.next.data:
                tmp_max = current.next.data        #set new max whenever current node < next node
            current = current.next                 #iterate
        return tmp_max                        #return max value 



# In[72]:


LLL = LinkedList(Node(2))
LLL.insert(21)
LLL.insert(5)
LLL.insert(3)
LLL.insert(14)
LLL.insert(9)
LLL.insert(4)

#unsorted
LLL.print_list()


# In[73]:


LLL.sort()
#sorted
LLL.print_list()


# In[69]:


print(LLL.find_max(LLL.head.next))
print(LLL.find_max(LLL.head.next.next.next.next.next))


# In[ ]:


#JUNK BELOW:


# In[ ]:





# In[75]:


for x in range(4):
    print(x)


# In[ ]:





# In[17]:


node1 = Node(14)
LL = LinkedList(node1)
LL.insert(6)
LL.insert(37)
LL.insert(50)
LL.insert(9)

LL.print_list()
print(node1.data)
print(LL.head.data)
print(LL.head.next.data)
print(LL.head.next.next.data)


# In[18]:


LL.sortTest()
print("end test")
#LL.sort()
LL.insert_at_begin(87)
LL.print_list()
LL.delete(50)
LL.print_list()


# In[ ]:


current = Node(4)
print(current.data)
print(type(current))


# In[ ]:


first_node = Node("a")
linked_list = LinkedList(first_node)   #create a linked list by making head/first node
linked_list.insert("b")
linked_list.insert("c")
print("The Linked List is:")
linked_list.print_list()

linked_list.delete("b")
print("After deleting 'b', the Linked List is:")
linked_list.print_list()
print("Current Size of the Linked List is:")
print(linked_list.size())

linked_list.insert_beg("Z")
print("After beggining add, The Linked List is:")
linked_list.print_list()

linked_list.insert_at_begin("i'm ")
print("After alt beggining add, The Linked List is:")
linked_list.print_list()


# In[ ]:


def sort(self):
    n = self.size()
    
    current_outer = self.head
    current_inner = self.head 
    # 
    for i in range(n-1): # i.e. 0, 1, 2, .., n-1 indices 
        
        tmp_max=current_outer.data                     
            
        current_inner = current_outer    
        while (current_inner.next):                      #look thru LL from current til the end to find temporary max
            if tmp_max < current_inner.data:
                tmp_max = current_inner.data             #set new max whenever current node < next node
                
            current_inner = current_inner.next
        
        self.delete(tmp_max)                             # delete it from current spot (by value)
        self.insert_at_begin(tmp_max)                    # insert max at the BEGINNING ()  
        self.print_list()                                                  #insert max of nodes 1-n at the beginning, then max of 
                                                          #nodes 2-n at beginning, .... will result in ascending order
        current_outer = current_outer.next               #iterate to next node in outer loop


# In[ ]:




    def sortTest(self):
        n = self.size()
        current = self.head
        while (current.next): # i.e. 0, 1, 2, .., n-1 indices 
if current.data > current.next.data:
    print(current.data)
current = current.next    

