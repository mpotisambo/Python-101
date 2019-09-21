#A function is like  a method or a class it consists of variables and other elements--------------------------------
name= "Mpotisambo"
def welcome(): #function name is greet in this case

 if (name == "Mpotisambo"):
    print("Hello " +  name  + "  Welcome back") # this case true statement it prints Hello mpotisambo welcome back

 else: 
        print("Hello who are you") # incase the variable name is not "Mpotisambo"


welcome() #this is how you call a function

#Using the return statement in functions-------------------------------------------------------------------------------------
 
def jibu():
 wikedz= 5
 timoth=3

 answer= wikedz + timoth
 print(answer)

 return answer


jibu()
