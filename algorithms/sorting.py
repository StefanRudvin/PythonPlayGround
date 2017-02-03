## Sorting algorithm python implementation

numbers = [31,192,4104,1,6,2,15,51,162]
#numbers = [5,4,3,2,1]

def sort(array):

    passes = len(array)
    i = 0
    while i < passes:
        print("Pass number: ",i)
        i += 1
        sortpass(array)

    print("Passes done!")

def sortpass(array):
    i = 0
    while i < len(array)-1:
        j = i + 1
        #print("Comparing",array[i],"to",array[j])
        if int(array[i]) > int(array[j]):
            array[i], array[j] = array[j], array[i]
        i = j

def start():
    print("Welcome to the sorting algorithm")
    print("Array to sort: ", numbers)
    sort(numbers)
    print("Sorted array:")
    print(numbers)

while True:
    start()
    print("Go again?")
    userinput = input()
    if userinput == "no" or userinput == "n":
        break
