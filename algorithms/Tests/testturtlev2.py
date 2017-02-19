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
    if index > 1:
        largest = nthlargest(ar, index)
        secondLargest = nthlargest(ar, index-1)
        #print(index, "largest:", largest,"2ndlargest: ", secondLargest)
        if secondLargest > largest:
            print("Moved number", ar[secondLargest], "@index", secondLargest)
            moves.append(secondLargest)
            ar = move(ar, secondLargest)
            index -= 1
            turtleSort(ar, index)
        else:
            index -= 1
            turtleSort(ar, index)
    else:
        print(ar)
        return ar

def sort():
    global moves
    moves = []

    #inputArray = [5,3,4,2,1]
    #print(inputArray)
    #inputArray = turtleSort(inputArray, len(inputArray))
    #print(inputArray)

    # Now: make the strings equal numbers

    #inputString = ['cat', 'dog', 'bear', 'camel']
    #sortedString = [ 'camel','dog', 'bear', 'cat']

    inputString = ['b', 'c', 'a']
    sortedString = ['a','b', 'c']

    inputAr = []
    sortedAr = []

    for a,b in enumerate(inputString):
        for c,d in enumerate(sortedString):
            if b == d:
                inputAr.append(c+1)

    #inputAr = [2,3,1]
    #sortedAr = [1,2,3]
    print("input",inputAr)
    inputAr = turtleSort(inputAr, len(inputAr))
    print("Moves:",moves)
    for i in moves:
        print(inputString[i])
    print(inputAr)

sort()
