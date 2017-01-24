#Algorithms practical 1

while True:

    carrynumbers = 0

    userInput = raw_input()

    numbers = userInput.split()
    digit1 = numbers[0]
    digit2 = numbers[1]

    #print "First digit: " , digit1, "Second digit: ", digit2

    if digit1 == "0" and digit2 == "0":
        break

    carryNumbers = 0

    for n in range(len(digit1)):
        carry = int(digit1[n]) + int(digit2[n])
        #print carry
        if carry >= 10:
            carryNumbers += 1
        n += 1

    print "This has", carryNumbers , "Carries"
