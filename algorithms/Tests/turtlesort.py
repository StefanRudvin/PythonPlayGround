
global printables
printables = []

def main():
    start = False
    count = False
    while True:

        if start == False:
            userInput = input()
            if count == False:
                testCount = userInput
                testCount = int(testCount)
                print("Number of test counts:", testCount)
                count = True
            else:
                start = True
                arraylen = userInput
                print("Number of turtles per stack:", arraylen)
                print("start geting arrays")
        else:
            if testCount > 0:
                print("Tests left",testCount)
                sortedArray = []
                inputArray = []

                for i in range(int(arraylen)):
                    userInput = input()
                    inputArray.append(userInput)

                input()

                for i in range(int(arraylen)):
                    userInput = input()
                    sortedArray.append(userInput)

                #Arrays are set. Now do the maths and add to printables.
                sort()
                testCount -= 1
            else:
                break

main()
