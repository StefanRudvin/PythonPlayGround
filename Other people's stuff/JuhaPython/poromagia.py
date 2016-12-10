##Python koodaus
import os, re

datadir = "poromagia"
katalogi = dict()
name = 0  ##Apumuuttuja, jolla tieto nimirivin loytymisesta
price = 0 ##Apumuuttuja, jolla tieto hintarivin loytymisesta

poro = open("poromagia.txt", 'w', encoding = "ISO-8859-1")

for page in os.listdir(datadir):
    f = iter(open(datadir + "/" + page, 'r', encoding = "ISO-8859-1"))
    for line in f:

        ##Find the line where the name is
        if '<a itemprop="name"' in line:
            name = 1
        ##Get name
        elif name == 1:
            name = 0
            regu = re.search('\s*(.*)', line)
            if regu != None:
                    game = regu.group(1)

        ##Find the line where the price is
        elif '<span itemprop="price"' in line:
            price = 1
        elif price == 1:
            price = 0
            regu = re.search('\s*(.*)\D{6}',line)
            if regu != None:
                katalogi[game] = regu.group(1)
                poro.write(game + "---" + regu.group(1) + "\n")

f.close()
poro.close()

##Print out number of items in catalogue
print('Items in catalogue: ' + str(len(katalogi)))
