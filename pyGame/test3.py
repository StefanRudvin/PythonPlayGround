import math, string

filename = "test3.txt"
target = open(filename,'r')
message = target.read()
target.close()

alphabet = string.ascii_lowercase

alphabetList = []

for word in alphabet:
    alphabetList.append(word)

#print(alphabetList,end="")

print("")
print("")

#Three big letters

def interpet(text):
    bigCounter = 0
    big2Counter = 0
    theLetter = ""
    nextLevel = False
    for letter in text:
        if nextLevel:
            if letter not in alphabetList:

                big2Counter +=1
                bigCounter += 1
            else:
                nextLevel = False
            if big2Counter == 3:
                return theLetter
                break
        else:
            if bigCounter == 3 and letter in alphabetList:
                print(letter)
                theLetter = letter
                nextLevel = True
                bigCounter = 0
            if letter not in alphabetList:
                bigCounter += 1

dat = interpet(message)

filename = "test3output.txt"
target = open(filename,'w')
target.truncate()
target.write(dat)
target.close()
