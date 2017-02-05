##   Binary search algorithm implementation

numbers = [0, 1, 3, 6, 8, 9, 13, 25, 34, 64, 73, 83, 94, 101, 102, 103, 104, 120, 131]

# numbers = [0,1,2,3,4,5,6,7]

def binarysearch(numbers, value: object, currentpoint: object) -> object:
    i = int(len(numbers) / 2)
    print("Current number:", numbers[i])
    if numbers[i] == value:
        print("Value", value, "found at position", currentpoint)
        return
    elif value > numbers[i]:
        currentpoint += int(len(numbers) / 4)
        binarysearch(numbers[i:], value, currentpoint)
    elif value < numbers[i]:
        currentpoint -= int(len(numbers) / 4)
        binarysearch(numbers[:i], value, currentpoint)
    else:
        print("Number not found!")


def start():
    print("Welcome to binary search algorithm")
    print("Array:", numbers, "Length:", len(numbers))
    print("Look for number: ")
    value = int(input())

    print("Looking for:", value)
    currentpoint = int(len(numbers) / 2)

    binarysearch(numbers, value, currentpoint)


while True:
    start()
    print("")
    print("Go again?")
    userinput = input()
    if userinput == "no" or userinput == "n":
        break
