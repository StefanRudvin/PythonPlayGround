inputArray = [4,5,3,1,2]
sortedArray = [1,2,3,4,5]
print("input array",inputArray)
print("sorted array",sortedArray)

counter = 0
maxCounter = 0
lastindex = 0

for a,b in enumerate(sortedArray):
    for c,d in enumerate(inputArray):
        if b == d:
            if a == c:
                counter += 1
                if counter > maxCounter:
                    maxCounter = counter
                    lastindex = c
            else:
                counter = 0
count = False

for a,b in enumerate(sortedArray):
    for c,d in enumerate(inputArray):
        print(a,c)
        if count is False:
            if b == d:
                for y in reversed(range(c)):
                    print("to set:",y+1)
                    inputArray[y+1] = inputArray[y]
                inputArray[0] = b


print("input array",inputArray)

#print("Max num of repeated occurences:", maxCounter, "Ending at index:", lastindex)
#rangetostay = (lastindex-maxCounter+1, lastindex)
#print("Range to stay:", rangetostay)
