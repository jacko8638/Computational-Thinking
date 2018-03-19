#function to take duration and process it
def plumbMoney(duration):
    hours = int(duration) / 100  # takes the hours from the duration
    mins = (int(duration) % 100) / 10  # takes the mins from the duration and divides by ten so they can be multiplied
    if mins >= 3:  # checks to see if an extra half an hour is needed
        charged = (int(hours) * 40) + ((int(mins) + 1) * 20)  # adds extra half hour and totals charged money
    else:
        charged = (int(hours) * 40) + (int(mins) * 20)  # totals charged
    return charged


#main program
duration = input("enter time")
print(plumbMoney(duration))