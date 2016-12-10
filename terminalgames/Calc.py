import os

NUMBERS = [str(x) for x in range(9999+1)]

def divide(var1,var2):
    print('The result of ' + var1 + ' divided by ' + var2 + ' is: ')
    print(int(var1) / int(var2))

def multiply(var1,var2):
    print('The result of ' + var1 + ' multiplied by ' + var2 + ' is: ')
    print(int(var1) * int(var2))

def subtract(var1,var2):
    print('The result of ' + var1 + ' - ' + var2 + ' is: ')
    print(int(var1) - int(var2))

def add(var1,var2):
    print('The result of ' + var1 + ' + ' + var2 + ' is: ')
    print(int(var1) + int(var2))

def playAgain():
   # This function returns True if the player wants to play again, otherwise it returns False.
   print('Do you want to play again? (yes or no)')
   return input().lower().startswith('y')

while True:
    os.system('clear')
    print('Welcome to the calculator python script.')
    print('1 for divide, 2 for multiply, 3 for subtract, 4 for add')
    while True:
        mode = input()
        if mode not in '01234':
            print('Invalid input, try again:')
        else:
            break
    print('Enter 1st value')

    while True:
        num1 = input()
        if num1 not in NUMBERS:
            print('Invalid input, try again:')
        else:
            break

    print('Enter 2nd value')
    while True:
        num2 = input()
        if num2 not in NUMBERS:
            print('Invalid input, try again:')
        else:
            break

    if int(mode) == 1:
        divide(num1,num2)

    elif int(mode) == 2:
        multiply(num1,num2)

    elif int(mode) == 3:
        subtract(num1,num2)

    elif int(mode) == 4:
        add(num1,num2)

    if not playAgain():
        break
