
def main():
    array = input("Array: ")
    array = pancake(list(array))
    print('Sorted list:', array)

def pancake(array):
    if len(array) <= 1:
        return array
    for size in range(len(array), 1, -1):
        maxindex = max(range(size), key=array.__getitem__)
        if maxindex+1 != size:
            if maxindex != 0:
                array[:maxindex+1] = reversed(array[:maxindex+1])
            array[:size] = reversed(array[:size])



if __name__ == '__main__':
    main()
