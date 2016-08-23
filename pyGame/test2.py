import math, string

filename = "test2.txt"
target = open(filename)
message = target.read()
target.close()

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
    print(text)
    for letter in text:
        if alphabetList[i] in letter:
            final += alphabetList[i]
    return final

dat = interpet(message)

filename = "test2output.txt"
target = open(filename,'w')
target.truncate()
target.write(dat)
target.close()
