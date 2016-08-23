import math, string

#message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

message="map"
alphabet = string.ascii_lowercase

alphabetList = []

for word in alphabet:
    alphabetList.append(word)

print(alphabetList,end="")

print("")
print("")

def interpet(text):
    for (n, v) in enumerate(alphabetList):
        pass
    final = ""
    for letter in text:
        for i in range(0,26):
            if alphabetList[i] in letter:
                if i > 22:
                    i -= 26
                    print(alphabetList[i+2],end="")
                    final += alphabetList[i+2]
                else:
                    print(alphabetList[i+2],end="")
                    final += alphabetList[i+2]

    return final


dat = interpet(message)

filename = "test.text"
target = open(filename,'w')
target.truncate()
target.write(dat)
target.close()
