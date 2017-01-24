#Algorithms practical 1

'''

 5 carry operations.
27.4 carry operations.
28.4 carry operations.
29.8 carry operations.
30.6 carry operations.
31.6 carry operations.
32.3 carry operations.
33.2 carry operations.

 5 carry operations.
36.4 carry operations.
37.4 carry operations.
38.8 carry operations.
39.6 carry operations.
40.6 carry operations.
41.3 carry operations.
42.2 carry operations.

2 carry operations.
2 carry operations.


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
    elif carryNumbers == 1:
        print carryNumbers , "carry operation."
    else:
        print carryNumbers , "carry operations."
