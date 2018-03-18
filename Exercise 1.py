#function to take duration and process it
def plumbMoney(duration):
    hours = duration / 100  # takes the hours from the duration
    mins = (duration % 100) / 10  # takes the mins from the duration and divides by ten so they can be multiplied
    if mins >= 3:  # checks to see if an extra half an hour is needed
        charged = (hours * 40) + ((mins + 1) * 20)  # adds extra half hour and totals charged money
    else:
        charged = (hours * 40) + (mins * 20)  # totals charged
    return charged


#main program
duration = input("enter time")
plumbMoney(duration)