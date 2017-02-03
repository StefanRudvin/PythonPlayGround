# Algorithms practical 2
# This program is a 'merger' that merges files, in this case inputs. Can be used for e.g. emails, phone numbers etc.
'''
stefan stefan.rudvin@hotmail.com
john aberdeen@email
sam aberdeen@test

stefan aberdeen
john london
sam china

stefan 040123123
john 077123123
sam 12331231231

Combines into:
Stefan ['stefan.rudvin@hotmail.com', 'aberdeen', '040123123']
etc.


'''

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
