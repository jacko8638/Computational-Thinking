from time import sleep
#subroutines
def question1():
    #A is the correct answer
    print("question?")
    sleep(2)
    print("Is it:")
    sleep(1)
    print("A: answer"
          "B: answer"
          "C: answer"
          "D: answer")
    answer = input("Your answer:")
    if len(answer) = 1 and answer.isalpha():
        lower(answer)
        if answer = "a":
            print("Congrats, your answer is correct!")
            totalCorrect = totalCorrect + 1
            return totalCorrect
        else:
            print("Oh no! Your answer was incorrect")
            totalIncorrect = totalIncorrect + 1
            return totalIncorrect
            questionNext()
    else:
        print("Sorry I didn't understand your answer, please try again")
        question1()

def questionNext():
    #same formula as first question but different question and answer

#globals
totalCorrect = 0
totalIncorrect = 0



#mainprogram
print("Welcome to the quiz.")
question1()
print("Thank you for playing")
print("You have %d correct answers" % totalCorrect)
print("You have %d incorrect answers" % totalIncorrect)