## Binary search algorithm implementation

numbers = [0,1,3,6,8,9,13,25,34,64,73,83,94,101,102,103,104,120,131]

#numbers = [0,1,2,3,4,5,6,7]

def binarysearch(array, value, currentpoint):
    i = int(len(array)/2)
    print("Current number:", array[i])
    if array[i] == value:
        print("Value",value,"found at position", currentpoint)
        return
    elif array[i] < value:
        currentpoint = currentpoint + int(len(array)/4)
        binarysearch(array[i:],value, currentpoint)
    elif array[i] > value:
        currentpoint = currentpoint - int(len(array)/4)
        binarysearch(array[:i],value, currentpoint)
    else:
        print("Number not found!")

def start():
    print("Welcome to binary search algorithm")
    print("Array:", numbers, "Length:", len(numbers))
    print("Look for number: ")
    value = int(input())

    print("Looking for:", value)
    currentpoint = int(len(numbers)/2)

    binarysearch(numbers,value, currentpoint)

while True:
    start()
    print("")
    print("Go again?")
    userinput = input()
    if userinput == "no" or userinput == "n":
        break
