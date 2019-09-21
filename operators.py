#This is addition------
x= 5
y=3
z=x+y
print(z) 
#Subtraction---
cats=7-3
print(cats)
 
 #Division---- always returns a floating number
age=27/3
print(age)

#Floor divisions removes the remainders
eggs=27//2
print(eggs)

#Remainders------
sugar_cane=17%3
print(sugar_cane)

#Multiplication----
seats=5*4
print(seats)

#power-------------
cows=2**9
print(cows)

#Other operators-----------------------------------------------------------------------------------------
m=23
k=44

#greater than symbol-----
print(k>m) #this case its true k is bigger than m

#less than symbol------
print(m<k) #this case is also true m is less than k

#equal to-----------
print(m==k) #this case its false since 23 is not equal to 44

#greater or equal to-------
print(m>=k) #this case its also false 23 is not equal or greater than 44

#less or equal to ------------
print(m<=k) #this means m is less or qual to k ("this case the statement is still True because 44 can not be equal to 23")

#not equal to-----------
print(m!=k) #this case its true because m is not similar to k or equal


#Boolean signs---------------------------------------------------------------------------------------------------------------------------------
 
 a= True
 b=False

 print (a)# this is True
 print (b) #this is false

 print(a and b) # this gives result as False

 print(a or b) # this is True

 print(not a)  #this is false since everything that is a is True and evertyhing that i not a is false


 #Membership operators----------------------------------------------------------------------------------------------------------------------

a = "SIMBA"

print('S' in a) # this is True because S is in a

print('s' in a) # this is false because s is not in a

print('x' in a) #this is false because x doesnot exist in a


# Identity operators----------------------------------------------------------------------------------------------------------------------------

l1 = [1, 2, 3]
l2 = [1, 2, 3]

print(l1 is l2) # False because lists are mutable