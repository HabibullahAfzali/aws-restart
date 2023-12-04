#------------ Introducing the list data type in python! ----------
print("\n In this Exercise We try some of list or collection in Python check out the below examples:")
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print("\n Each item in a list/collection in python has their own numeric  postion called index, the first Index starts from 0")

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#------------ Changing the values in a list -------

myFruitList[2] = "orange"
print(myFruitList)

#------------ Defining a tuple --------------
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#Accessing a tuple by position---------

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])


#Introducing the dictionary data Type---------

print("\n Defining a dictionary!")

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#------- Accessing a dictionary by name -----------

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

