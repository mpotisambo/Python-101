#Strings---------------------------------------------------------------------------------------------------------------
# we can say a string is a set of word

String1 = 'Coding Addict' # simple singel string
print(String1)

#finding a character
char = "Mpotisambo Zamea"

print(char[0]) # finding the first character

print(char[-1]) #last character

print(char[3:10])# slicing a character

print(char[3:-2])#slicing from one point to another with indication of the last character

#updating a string---------------------------------------------------------------------------------------------------
char="MPOTISAMBO ZAMEA PETER"
print(char)

print(char.replace('O','U')) # replacing a character with another--

print(char.replace('A','')) #replace a character with nothing or in otherwords removing a character

print(char.translate({ord('E'): None})) #Similar with replace or remove

# Double quotes---------------------------------------------------------------------------------------------------------------
char = 'Hi\'m a "happy finally meeting you"'
print(char)