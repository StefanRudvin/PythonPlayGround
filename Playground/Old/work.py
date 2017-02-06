import pygame

print("Hello")
message = """Work hours:

  1.       2.      3.       4.       5.
8hours  7.5hours 7hours  6.5hours  6hours
"""
print(message)

def openAika(hours,breaks):
    return ((hours*60)-breaks)/60

def omaTauko(hours,breaks):
    return 0.05*((hours*60)-breaks)

def message(hours,breaks):
    print("""
    Your work day is %s hours.
    Your open aika is: %s hours.
    Your tauko aika is: %s minutes.""" % (hours,openAika(8,55),omaTauko(8,55)) )

while True:
    selection = input("Select your hours: ")

    if selection == "1":
        message(8,55)
        break
    elif selection == "2":
        message(7.5,50)
        break
    elif selection == "3":
        message(7,25)
        break
    elif selection == "4":
        message(6.5,25)
        break
    elif selection == "5":
        message(6,25)
        break
    else:
        print("Invalid selection!")







#8 hours: 15 + 10 + 30 = 55 minutes taukoa
