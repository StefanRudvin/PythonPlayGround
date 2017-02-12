# Pancake Sort Practical 3

'''
Uses the pancake sort algorithm and returns values on which index of the array was flipped.

Trickyness is ensued when the result must be in 'reverse' order, and indexes start from left to right for flipping.

Sample Input
 5 4 3 2 1
 1 2 3 4 5
 4 3 2 1 5
 0

 Sample Output
 5 4 3 2 1
 0
 1 2 3 4 5
 1 0
 4 3 2 1 5
 1 2 0
 0

'''


import sys

class Pancake():

    def engage(self, array):
        sorter = Sort()
        if len(array) == 1 and array[0] == "0":
            return False
        for a, b in enumerate(array):
            array[a:] = sorter.engage(array[a:], a)
        print("0")
        print("Final: ", array)
        return True


class Sort():

    def __init__(self):
        pass

    def engage(self, array, cycle):

        maxNum = 0
        maxIndex = 0

        for i, j in enumerate(array):
            if int(j) >= int(maxNum):
                maxNum = j
                maxIndex = i

        maxIndex += 1

        if maxIndex > 1:
            if maxIndex == len(array):
                flipnumber = len(array) - maxIndex + 1
                array = self.flipbyn(array, flipnumber)
                sys.stdout.write(str(flipnumber+cycle))
                sys.stdout.write(" ")
            else:
                array = self.flipbyn(array, maxIndex)
                sys.stdout.write(str(maxIndex+cycle))
                sys.stdout.write(" ")
                array = self.flipbyn(array, 1)
                sys.stdout.write("1 ")

        return array

    def flip(self, ar):
        length = len(ar) - 1

        for i, j in enumerate(ar):
            if i <= length / 2:
                h = length - i
                ar[i], ar[h] = ar[h], ar[i]
        return ar

    def flipbyn(self, array, n):
        n -= 1
        leftover = array[:n]
        flipped = self.flip(array[n:])
        final = leftover + flipped
        return final

def main():
    while True:
        array = getuserinput()

        pancake = Pancake()
        running = pancake.engage(array)
        if not running:
            break

    print("0")

def getuserinput():
    userinput = raw_input().split()
    return userinput


main()
