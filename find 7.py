import math

# this subroutine checks the length of the list to check it isn't empty and to find all the numbers
#divisable by 7 and adding them to a list
def findDivSeven(inputList):
    if len(inputList) == 0:
        print ("The inputted list is empty")
    else:
        outputList = []
        for i in inputList:
            if i % 7 == 0:
                outputList.append(i)
        if len(outputList) == 0:
            print ("There are no numbers divisible by 7")
        else:
           return outputList

#this is the list of numbers
intList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,123,45678,890]

#this is the main program
print(findDivSeven(intList))
