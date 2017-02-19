# Turtlesort assignment

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
            userInput = raw_input()
            testCount = userInput
            testCount = int(testCount)
            start = True
        else:
            if testCount > 0:
                arraylen = raw_input()
                sortedArray = []
                inputArray = []
                moves = []

                for i in range(int(arraylen)):
                    userInput = raw_input()
                    inputArray.append(userInput)

                orig = inputArray


                for i in range(int(arraylen)):
                    userInput = raw_input()
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
    for i in printables:
        print i

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


if __name__ == '__main__':
    main()
