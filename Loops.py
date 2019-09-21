#While loops----------------------------------------------------------------------------------------------------------------------
count = 0
while (count < 5):
	count = count + 1
	print('Hello am from planet Jupiter')

    #Applying else statement----------------------------------------------------------------------------------------------------------
count = 0
while (count > 2):
	count = count + 1
	print('Hello am from planet Jupiter')
else:
	print('What about you')
#Interating list------------------------------------------------------------------------------------------------------------------------
print('Full list of words')
m = ['she goes', 'to the', 'mary go round']
for i in m:
	print(i)

    #Tuple----------------------------------------------------------------------------------------------------------------------------
print('Other words fit in  here')
k = ['she wakes up early', 'says her prayers', 'then rashes to school']
for i in k:
        print(i)
        

        #Pass Statement-----------------------------------------------------------------------------------------------------------------
for letter in 'ComputingAcademy':
	pass
print( 'Last Letter : ', letter)
# Break Statement------------------------------------------------------------------------------------------------------------
for letter in 'ComputingAcademy':
	if letter == 'p' or letter == 'a':
		break
print ('Current Letter : ', letter)

	#Nested Loops------------------------------------------------------------------------------------------------------------------------------

for i in range(1, 5):
	for j in range(i):
		print(i, '\n')
	print()

print('\n')

#Continue Statement
for letter in 'Marygoround':
	if letter == 'y' or letter == 'u':
		continue
	print ('Current Letter : ', letter)
	var = 10