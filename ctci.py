import math

def powersOf2(n):
    if (n < 1):
        return 0
    elif (n == 1):
        print(1)
        return 1
    else:
        prev = powersOf2(math.floor(n/2))
        curr = prev * 2
        print(curr)
        return curr

powersOf2(50)
