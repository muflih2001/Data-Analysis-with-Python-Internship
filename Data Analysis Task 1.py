#!/usr/bin/env python
# coding: utf-8

# In[20]:


#List Operations
list=[1,2,3,4,5]
print("Initial List is ",list)


# In[21]:


list.append(6)


# In[22]:


print("List after adding an element is ",list)


# In[23]:


list.remove(5)
print("Updated List after removing an element is ",list)


# In[24]:


list[3]=7


# In[25]:


print("Updated List after modifying an element is ",list)


# In[59]:


#Dictionary Operations
Dict={'ID':1,'Dept': 'Computer','Age':22,'Course':'Data Analysis'}
print("Initial Dictionary Elements is ",Dict)


# In[60]:


Dict['City'] = 'Delhi'  
print("Updated Dictionary after adding an element is ",Dict)


# In[61]:


del Dict['Course']
print("Updated Dictionary after deleting an Element is ",Dict)


# In[62]:


Dict['Age'] = 27
print("Updated Dictionary after modfying an element is ",Dict)


# In[69]:


#Set Operations
Set={1,4,7,9,11,21}
print("Initial Set Elements is ",Set)


# In[70]:


Set.add(33)
print("Updated Set after adding an Element is ",Set)


# In[71]:


Set.remove(9)
print("Updated Set after removing an Element is ",Set)


# In[ ]:


#an element in a set cannot be modified

