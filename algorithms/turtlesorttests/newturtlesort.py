# Turtlesort assignment

'''

2
3
Yertle
Duke of Earl
Sir Lancelot
Duke of Earl
Yertle
Sir Lancelot
9
Sir Lancelot
Yertle
Richard M. Nixon
Duke of Earl
Elizabeth Windsor
Michael Eisner
Mr. Rogers
Ford perfect
Mack
Yertle
Richard M. Nixon
Sir Lancelot
Duke of Earl
Elizabeth Windsor
Michael Eisner
Mr. Rogers
Ford perfect
Mack











3
Yertle
Duke of Earl
Sir Lancelot
Duke of Earl
Yertle
Sir Lancelot
3
Yertle
Duke of Earl
Sir Lancelot
Duke of Earl
Yertle
Sir Lancelot
9
Yertle
Duke of Earl
Sir Lancelot
Elizabeth Windsor
Michael Eisner
Richard M. Nixon
Mr. Rogers
Ford perfect
Mack

Yertle
Richard M. Nixon
Sir Lancelot
Duke of Earl
Elizabeth Windsor
Michael Eisner
Mr. Rogers
Ford perfect
Mack


2
3

Yertle
Duke of Earl
Sir Lancelot

Duke of Earl
Yertle
Sir Lancelot
9

Yertle
Duke of Earl
Sir Lancelot
Elizabeth Windsor
Michael Eisner
Richard M. Nixon
Mr. Rogers
Ford perfect
Mack

Yertle
Richard M. Nixon
Sir Lancelot
Duke of Earl
Elizabeth Windsor
Michael Eisner
Mr. Rogers
Ford perfect
Mack

Richard M. Nixon
Sir Lancelot
Yertle
Duke of Earl
Elizabeth Windsor
Michael Eisner
Mr. Rogers
Ford perfect
Mack




'''

global printables
global moves
printables = []
moves = []

def main():
    global moves
    start = False
    count = False
    while True:

        if start == False:
            userInput = input()
            testCount = userInput
            testCount = int(testCount)
            #print("Number of test counts:", testCount)
            start = True
        else:
            if testCount > 0:
                arraylen = input()
                input()
                #print("Number of turtles per stack:", arraylen)
                #print("start geting arrays")
                #print("Tests left",testCount)
                sortedArray = []
                inputArray = []
                moves = []

                for i in range(int(arraylen)):
                    userInput = input()
                    inputArray.append(userInput)

                orig = inputArray

                input()

                for i in range(int(arraylen)):
                    userInput = input()
                    sortedArray.append(userInput)

                #Arrays are set. Now do the maths and add to printables.
                sort(inputArray, sortedArray)

                #Send moves for printing at end
                for i in moves:
                    printables.append(orig[i])
                printables.append("")

                testCount -= 1
            else:
                break

# Moves n index of array to the top
def move(ar, n):
    return [ar[n]] + ar[:n] + ar[n+1:]

# Get nth largest element in list
def nthlargest(ar, n):
    sortedar = sorted(ar)
    for a,b in enumerate(ar):
        for j in sortedar:
            if j == n:
                if b == n:
                    return a

# Main
def turtleSort(ar, index):
    global moves
    if index > 1:
        largest = nthlargest(ar, index)
        secondLargest = nthlargest(ar, index-1)
        if secondLargest > largest:
            #print("Moved number", ar[secondLargest], "@index", secondLargest)
            moves.append(secondLargest)
            ar = move(ar, secondLargest)
            index -= 1
            turtleSort(ar, index)
        else:
            index -= 1
            turtleSort(ar, index)
    else:

        return ar

def sort(inputString, sortedString):

    inputAr = []
    sortedAr = []

    for a,b in enumerate(inputString):
        for c,d in enumerate(sortedString):
            if b == d:
                inputAr.append(c+1)
    turtleSort(inputAr, len(inputAr))

printables.append("")
main()
for i in printables:
    print(i)
