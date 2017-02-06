import math

message = "gfmncwmsbgblrrpylqjyrcgrzwfylb.rfyrqufyramknsrcpqypcdmp.bmglegrglzwfylbgqglcddgagclrylbrfyr'qufw rfgqrcvrgqqmjmle.sqgleqrpgle.kyicrpylq()gqpcamkkclbcb.lmuynnjwmlrfcspj."

alphabet = "abcdefghijklmopqrstuvwxyz"


alphabetList = []

for letter in alphabet:
    alphabetList.append(letter)

print(alphabetList)

number = 0

for value in alphabetList:
    number+= 1

print(number)

def interpet(text):
    final = ""
    for letter in text:
        for x in range(0,24):
            if letter == alphabetList[x]:
                if x == 24:
                    print(alphabetList[1],end="")
                if x == 23:
                    print(alphabetList[0],end="")
                else:
                    print(alphabetList[x+2],end="")
interpet(message)

#print(interpet(message))
