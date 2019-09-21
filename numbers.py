# we have integer, decimals, floats and others
# an integer can be a whole number such as 2
import fractions
from decimal import Decimal as D

x=2
print (x)   # whole number

x =5.3
print(  int (x)) #prints out only 5

x=7.8
print(float (x)) # print out its floating decimal

x = 1.1
y = 2.2
z = x + y

print(z) # it gives a decimal answer
print(int(z)) #gives whole number as answer

print(fractions.Fraction(1.5))
print(D('1.1') + D('2.2'))

#Using Math method
import math


print(math.pi) # Output: 3.141592653589793


print(math.cos(math.pi)) # Output: -1.0


print(math.exp(10)) # Output: 22026.465794806718


print(math.log10(1000)) # Output: 3.0


print(math.sinh(1)) # Output: 1.1752011936438014


print(math.factorial(6)) # Output: 720