## Binary search algorithm implementation

numbers = [0,1,3,6,8,9,13,25,34,64,73,83,94,101,102,103,104,120,131]

def binarysearch(array, value):
    i = int(len(array)/2)
    print("Current number:", array[i])
    if array[i] == value:
        print("Value found!")
        return
    elif array[i] < value:
        binarysearch(array[i:],value)
    elif array[i] > value:
        binarysearch(array[:i],value)
    else:
        print("Number not found!")

def start():
    value = 34
    print("Welcome to the sorting algorithm")
    print("Array: ", numbers)
    print("Look for number: ")
    value = int(input())

    print("Looking for:", value)
    binarysearch(numbers,value)

while True:
    start()
    print("Go again?")
    userinput = input()
    if userinput == "no" or userinput == "n":
        break
