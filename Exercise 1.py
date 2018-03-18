#function to take duration and process it
def plumbMoney(duration):
    hours = duration / 100 # takes the hours from the duration
    mins = (duration % 100) / 10 # takes the mins from the duration and divides by ten so they can be multiplied
    if mins >= 3:
        charged = (hours * 40) + ((mins + 1) * 20)
    else:
        charged = (hours * 40) + (mins * 20)
    return charged


#main program
duration = input("enter time")
plumbMoney(duration)