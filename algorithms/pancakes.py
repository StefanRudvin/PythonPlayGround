# Sorting Practical 3
from pip._vendor.distlib.compat import raw_input
import sys


def flip(ar):
    length = len(ar) - 1

    for i, j in enumerate(ar):
        if i < length / 2:
            h = length - i
            ar[i], ar[h] = ar[h], ar[i]
    return ar


def getuserinput():
    userinput = raw_input("Array: ").split()
    return userinput


def getflipnumber():
    flipnumber = raw_input("Cutoff: ")
    flipnumber = int(flipnumber) - 1
    return flipnumber


def flipbyn(array, n):
    leftover = userinput[:flipnumber]
    flipped = flip(userinput[flipnumber:])
    final = leftover + flipped
    return final


userinput = getuserinput()

sorted = sorted(userinput, reverse=True)
print(sorted)

flipnumber = getflipnumber()

final = flipbyn(userinput, flipnumber)

[sys.stdout.write(i + " ") for i in final]


"""

Find a list of movements to make.

Compare sorted numbers to original numbers




Make a list out of them.


Print them at the end of the program





"""






