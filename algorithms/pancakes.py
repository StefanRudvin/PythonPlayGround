# Pancake Sort Practical 3
import sys

def flip(ar):
    length = len(ar) - 1

    for i, j in enumerate(ar):
        if i <= length / 2:
            h = length - i
            ar[i], ar[h] = ar[h], ar[i]
    return ar

def getuserinput():
    userinput = raw_input().split()
    return userinput

def flipbyn(array, n):
    n -= 1
    leftover = array[:n]
    flipped = flip(array[n:])
    final = leftover + flipped
    return final

def moveLargest(arrayslice, a):
    maxNum = 0
    maxIndex = 0

    for i, j in enumerate(arrayslice):
        if int(j) >= int(maxNum):
            maxNum = j
            maxIndex = i

    maxIndex += 1

    if maxIndex > 1:
        if maxIndex == len(arrayslice):
            flipnumber = len(arrayslice) - maxIndex + 1
            arrayslice = flipbyn(arrayslice, flipnumber)
            sys.stdout.write(str(flipnumber+a))
            sys.stdout.write(" ")
        else:
            arrayslice = flipbyn(arrayslice, maxIndex)
            sys.stdout.write(str(maxIndex+a))
            sys.stdout.write(" ")
            arrayslice = flipbyn(arrayslice, 1)
            sys.stdout.write("1 ")

    return arrayslice

while True:
    array = getuserinput()

    if len(array) == 1 and array[0] == "0":
        #print("Done bitch")
        break
    for a, b in enumerate(array):
        array[a:] = moveLargest(array[a:], a)
    print("0")
    #print("Final: ", array)
print("0")


'''
5 4 3 2 1
1 2 3 4 5
4 3 2 1 5
0
Running with input
5 4 3 2 1
1 2 3 4 5
4 3 2 1 5
0

Your output:
0
1 0
1 2 4 1 0
17 50 44 41 59 66 38 35 11 12 63 14 54 21 51 4 45 18 70 13 15 20 71 64 42 67 16 46 39 52 57 49 36 10 43 23 62 58 31 30 22 76 48 40 56 72 47 53 6 9 65 19 69 29 37 34 5 24 68 73 33 55 8 25 74 28 61 75 26 60 7 27 32

'''
