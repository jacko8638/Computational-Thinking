from time import sleep
#subroutines

def question1():
    global totalpoints
    #A is the correct answer
    #this prints the question and answers
    sleep(1)
    print("what is the best IT related tv show")
    sleep(2)
    print("Is it:")
    sleep(1)
    print("A: IT Crowd")
    sleep(1)
    print("B: Silicon Valley")
    sleep(1)
    print("C: Mr Robot")
    sleep(1)
    print("D: </scorpion>")
    sleep(1)
    #this asks the user to input their answer
    answer = input("Your answer:")
    #first if statement questions if answer is valid
    if len(answer) == 1 and answer.isalpha():
        #converts answer to always be lower case so it can be understood by if statement
        answer.lower()
        if answer == "a":
            print("Congrats, your answer is correct!")
            #updates points
            totalpoints = totalpoints + 1
        elif answer == "b":
            #corrects user who thinks silicon valley is better than IT Crowd
            print("Thats definatly wrong, for that answer your getting two negative points")
            #updates points
            totalpoints = totalpoints - 2
        else:
            print("Oh no! Your answer was incorrect")
            #updates points
            totalpoints = totalpoints - 1
    #calls next question
    else:
        #gets user to re-enter answer if it wasnt a valid answer
        print("Sorry I didn't understand your answer, please try again")
        question1()

#other questions are defined here

#globals
totalpoints = 0



#mainprogram
print("Welcome to the quiz.")
question1()
print("Thank you for playing")
#displays how many answers they got right and wrong
print("Your score is %d" % totalpoints