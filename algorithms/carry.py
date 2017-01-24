#Algorithms practical 1

'''

6 operations
299743898 716456069

156188102
193749048
      150
010011001


'''

while True:

    carrynumbers = 0

    userInput = raw_input()

    numbers = userInput.split()
    digit1 = numbers[0]
    digit2 = numbers[1]

    if digit1 == "0" and digit2 == "0":
        break

    carryNumbers = 0

    n1 = len(digit1)-1
    n2 = len(digit2)-1
    carryOver = False

    while n1 > -1 and n2 > -1:

        carry = int(digit1[n1]) + int(digit2[n2])

        if carryOver == True:
            carry += 1
            carryOver = False

        if carry >= 10:
            carryNumbers += 1
            carryOver= True

        n1 -= 1
        n2 -= 1

    if carryNumbers == 0:
        print "No carry operation."
    else:
        print carryNumbers , "carry operations."
