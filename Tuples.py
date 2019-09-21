# I can say a tuple is a collection of elements 
pirez = ()
print(pirez)  # Output: ()

# Tuple having integers---------------------------------------------------------------------------------
pirez = (1, 2, 3)
print(pirez)  # Output: (1, 2, 3) 

# tuple with mixed datatypes--------------------------------------------------
pirez = (1, "Mambo", 3.4)
print(pirez)  # Output: (1, "Mambo", 3.4)  

# nested tuple
pirez = ("mouse", [8, 4, 6], (1, 2, 3))

# Output: ("mouse", [8, 4, 6], (1, 2, 3)) 
print(pirez)

#Accessing a tuple
sambo=('m','p','o','t','i','s','a','m','b','o')
print(sambo[3])

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4

my_tuple = (4, 2, 3, [6, 5])
my_tuple[3][0] = 9    # Output: (4, 2, 3, [9, 5]) changing items of an element
print(my_tuple)


# Tuples can be reassigned---------------------------------------------------------------
my_tuple = ('p','r','o','g','r','a','m','i','z')

# Output: ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple)

del my_tuple

print(my_tuple.count('p'))  # Output: 1

print(my_tuple.index('g'))  # Output: 3

# Boolean tuple output
print('a' in my_tuple) #Output: True
print('x' in my_tuple) #output: False

