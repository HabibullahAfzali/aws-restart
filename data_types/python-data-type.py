
#print("Puthon has three numeric types: int, float, and complex")

#myValue= 1


#(str(myValue) + " is of the data type " + str(type(myValue)))
#---- float exericse-----

myValue = 3.14

print(myValue)
print(type(myValue))
print(str(myValue)+ " is of the data type "+ str(type(myValue)))

#--------- Complex data Type------
myComplexValue = 5j

print(myComplexValue)
print(type(myComplexValue))
print(str(myComplexValue)+ " is of the data type " + str(type(myComplexValue)))

#---- Boolean data type in pyton -----------

print("Boolean Data Type In Python:")
isTrue=True

print(isTrue)
print(type(isTrue))
print(str(isTrue)+ " is of the data type " + str(type(isTrue)))

isTrue=False

print(isTrue)
print(type(isTrue))
print(str(isTrue)+ " is of the data type " + str(type(isTrue)))

#----------- string Data Type In Python ----------

print("\n the bellow are examples of String data type in python:")
myString = "This is a string."
print(myString)
print(type(myString))

print(str(myString)+ " is of the data type " + str(type(myString)))

#------- String Concatenation is Python ------------

print ("\n String Concatenation in Python:")

firstString = "Water"
secondString = "fall"
thirdString = firstString + secondString

print(thirdString)


#------------ Input Strings In Python ------------

print("\n we can use input keyword to type text from keyboard or any other input device:")

name = input("What is your name?")
print("Dear " +name+" Welcome to hte world of Python Programming!")


#------------- Formatting Output Stirngs -------------
print ("\n using .format() function we can format our string output, check out the below examples:")

color = input("\n What is your favorite color? ")
animal = input("\n what is your favorite animal?")

print("{}, you like a {} {} !".format(name,color,animal))



