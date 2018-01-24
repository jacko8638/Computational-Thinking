import math
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

intList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(findDivSeven(intList))
