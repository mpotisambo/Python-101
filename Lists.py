# empty list--------------------------------------------------------------------------------------------------------------------
list1 = []
# list of integers---------------------------------------------------------------------------------------------------------------
list2 = [1, 2, 3]
# list with mixed datatypes--------------------------------------------------------------------------------------------------
list3 = [1, "Hello", 3.4]

print(list1)
print(list2)
print(list3)

# nested list
my_list = ["mouse", [8, 4, 6], ['a']]
print(my_list)

#Accessing Elements in the List------------------------------------------------------------------------------------------------------------

employees = ['mpotisambo','amani','zamea','peter']#nested list-----
print(employees[0]) #one element is accessed from the list

print(employees[0] [2]) # accessing  element 0 and specifically o in the nested list-------

#Negative indexing-------------------------------------------------------------------------------------------------------------
my_list = ['p','r','o','b','e']

print(my_list[-1]) #out put e

#Slicing in lists---------------------------------------------------------------------------------------------------------------------

my_list = ['p','r','o','g','r','a','m','i','z']

print(my_list[2:5])# elements 3rd to 5th

print(my_list[:-5])# elements beginning to 4th

print(my_list[5:])# elements 6th to end

print(my_list[:])# elements beginning to end



#Changing Elements--------------------------------------------------------------------------------------------------------------------------
numb = ['0','2','3','4']
numb[0] = '1'
print(numb)

#Adding an element in the list---------------------------------------------------------------------------------------------------
numb.append('5')# adding a single element---
print(numb)

numb.extend(['6','7','8','9'])
print(numb)# adding multiple characters--------------

print("mpoti" * 5)

#Adding an element in the list------------------------------------------------------------------------------------
numb.insert(9,'10') #adding another element after thre previous number
print(numb)

my_list = ['p','r','o','b','l','e','m']

del my_list[2]# delete one item
print(my_list)