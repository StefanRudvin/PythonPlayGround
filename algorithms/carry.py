# Algorithms practical 1
# User inputs numbers, this program counts how many carry operations an addition produces.
from pip._vendor.distlib.compat import raw_input

while True:

    userInput = raw_input()

    numbers = userInput.split()
    digit1 = numbers[0]
    digit2 = numbers[1]

    if digit1 == "0" and digit2 == "0":
        break

    carryNumbers = 0

    n1 = len(digit1) - 1
    n2 = len(digit2) - 1
    carryOver = False

    while n1 > -1 and n2 > -1:

        carry = int(digit1[n1]) + int(digit2[n2])

        if carryOver is True:
            carry += 1
            carryOver = False

        if carry >= 10:
            carryNumbers += 1
            carryOver = True

        n1 -= 1
        n2 -= 1

    if carryNumbers == 0:
        print
        'No carry operation.'
    elif carryNumbers == 1:
        print(carryNumbers, "carry operation.")
    else:
        print(carryNumbers, "carry operations.")
