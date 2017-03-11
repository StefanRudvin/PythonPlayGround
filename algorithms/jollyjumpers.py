#Algorithms practical 6

def main():
    printAr = []
    while True:
        userinput = raw_input()
        if userinput == "0":
            break
        inputAr = userinput.split()
        inputAr = map(int, inputAr)
        printAr.append(jolly(inputAr))
    print "\n".join(printAr)

def jolly(numbers):
    difs = []
    for i, j in enumerate(numbers):
        if not i == 0:
            difs.append(abs(j - numbers[i-1]))
    for i in range(len(numbers)-1):
        if not i == 0:
            if i not in difs:
                return "Not Jolly"
    return "Jolly"

main()
