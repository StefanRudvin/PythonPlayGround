def distance(house1, house2):
    return abs(house1 - house2)

def calc(houses):
    finalSum = float("inf")
    for i in range(min(houses), max(houses)):
        currentSum = 0
        for house in houses:
            currentSum += distance(i, house)
        if currentSum < finalSum:
            finalSum = currentSum

    return finalSum

def main():
    start = False
    finalSums = []
    while True:
        if start == False:
            testCount = int(raw_input())
            start = True
        else:
            if testCount > 0:
                houses = []
                houses = raw_input()

                houses = houses.split()

                houses = map(int, houses)

                relativeNum = houses[0]

                houses.pop(0)

                finalSums.append(calc(houses))

                testCount -= 1
            else:
                break

    #print "Final sum:"
    for i in finalSums:
        print i

main()
