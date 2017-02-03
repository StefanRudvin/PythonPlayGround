# Selection sort algorithm
import math

#numbers = [31,192,4104,1,6,2,15,51,162]
numbers = [5,4,3,2,1]

def selectionsort(array):
    finalArray = []
    i = 0
    n = len(array)
    while i < n:
        finalArray.append(swapminimum(array)[0])
        array.pop(0)
        i += 1
    return finalArray


def swapminimum(array):
    i = 0
    minplace = 0
    minimum = math.inf

    while i < len(array):
        x = array[i]
        if x < minimum:
            minimum = x
            minplace = i
        i += 1

    array[minplace], array[0] = array[0], array[minplace]

    return array

def start():
    print("Welcome to the sorting algorithm")
    print("Array to sort: ", numbers)

    print("Sorted array:")
    print(selectionsort(numbers))

while True:
    start()
    print("Go again?")
    userinput = input()
    if userinput == "no" or userinput == "n":
        break
