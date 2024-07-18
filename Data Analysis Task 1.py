#List Operations
list=[1,2,3,4,5]
print("Initial List is ",list)

list.append(6)

print("List after adding an element is ",list)

list.remove(5)
print("Updated List after removing an element is ",list)

list[3]=7

print("Updated List after modifying an element is ",list)

#Dictionary Operations
Dict={'ID':1,'Dept': 'Computer','Age':22,'Course':'Data Analysis'}
print("Initial Dictionary Elements is ",Dict)

Dict['City'] = 'Delhi'  
print("Updated Dictionary after adding an element is ",Dict)

del Dict['Course']
print("Updated Dictionary after deleting an Element is ",Dict)

Dict['Age'] = 27
print("Updated Dictionary after modfying an element is ",Dict)

#Set Operations
Set={1,4,7,9,11,21}
print("Initial Set Elements is ",Set)

Set.add(33)
print("Updated Set after adding an Element is ",Set)

Set.remove(9)
print("Updated Set after removing an Element is ",Set)

#an element in a set cannot be modified
