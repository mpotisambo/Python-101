# Dictionary is like a set of various methods that is used to perform different tasks
#Examples are------------------------------------------------------------
Python Dictionary clear() #it clears all 
Python Dictionary copy()	#Returns Shallow Copy of a Dictionary
Python Dictionary fromkeys()	#creates dictionary from given sequence
Python Dictionary get()	#Returns Value of The Key
Python Dictionary items()	#returns view of dictionary's (key, value) pair
Python Dictionary keys()	#Returns View Object of All Keys
Python Dictionary popitem()	#Returns & Removes Element From Dictionary
Python Dictionary setdefault()	#Inserts Key With a Value if Key is not Present
Python Dictionary pop()	 #removes and returns element having given key
Python Dictionary values()	#returns view of all values in dictionary
Python Dictionary update()	#Updates the Dictionary
Python any() #	Checks if any Element of an Iterable is True
Python all()	#returns true when all elements in iterable is true
Python ascii()	#Returns String Containing Printable Representation
Python bool()	#Converts a Value to Boolean
Python dict()	#Creates a Dictionary
Python enumerate()	#Returns an Enumerate Object
Python filter()	#constructs iterator from elements which are true
Python iter()	#returns iterator for an object
Python len()	#Returns Length of an Object
Python max()	#returns largest element
Python min()	#returns smallest element
Python map()	#Applies Function and Returns a List
Python sorted()	 #returns sorted list from a given iterable
Python sum()	#Add items of an Iterable
Python zip()	#Returns an Iterator of Tuples

# Some of the dictionary methods in use

d = {1: "one", 2: "two"}

d.clear() # it clears everything ----------------
print('d =', d) 


original = {1:'one', 2:'two'}
new = original.copy() #Copy from origin---------

print('Orignal: ', original)
print('New: ', new)

# vowels keys ----------------------------
keys = {'a', 'e', 'i', 'o', 'u' }

vowels = dict.fromkeys(keys)
print(vowels)

d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2 ----------------------------------------
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3 --------------------------------------------------------------
d.update(d1)
print(d)


# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('apple')
print('The popped element is:', element)
print('The dictionary is:', sales)