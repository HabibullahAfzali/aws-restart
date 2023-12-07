
#---------- Categorizing Values -----------

#Task_1, Creating a mixed-type list

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

#We use for loop to access each value of our mixedlist values:

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
