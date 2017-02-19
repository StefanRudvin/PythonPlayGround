# x = "123"
#
# try:
#     int(x)
#     print("it worked")
# except:
#     print("haha")
#
# y = "123"
#
# try:
#     str(y)
#     print("Didnt work")
# except:
#     print("hsdlads")


string = ['b','c','a']

count = False

for a,b in enumerate(string):
    if count == False:
        if b == "a":
            for y in reversed(range(a)):
                string[y + 1] = string[y]
            string[0] = b
            count == True
print(string)
