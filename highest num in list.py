def findHighest(list):
    if len(list) == 0:
        return "THE LIST IS EMPTY!!!! ARE YOU HAPPY NOW?!"
    else:
        high = list[0]
        for num in list:
            if num > high:
                high = num
        return high

numList=(1,2,3,4,5,6,7,8,9,234,546,215,1456,13,5367,135,245,54678,13425)
print(findHighest(numList))