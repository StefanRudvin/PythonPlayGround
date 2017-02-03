# Algorithms practical 2

# Stefan Rudvin

import sys
result = {}

while True:

    userInput = raw_input()

    inputString = userInput.split()

    if len(inputString) < 1: 
        break

    if not len(inputString) < 2:
        key = inputString[0]
        value = inputString[1]

        if key not in result:
            result[key] = [value]
        else:
            result[key].append(value)

for key in sorted(result):
    sys.stdout.write(key)
    for value in result[key]:
        sys.stdout.write(" ")
        sys.stdout.write(value)
    print ""
