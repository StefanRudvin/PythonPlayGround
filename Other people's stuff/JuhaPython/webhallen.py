##Python koodaus
import os, re

datadir = "data"
katalogi = dict()
##toivelista = list()

Info range <table class="productlist"> ja </table>
##Kaikki muu discardiksi
web = open("webhallen.txt", 'w', encoding = "ISO-8859-1")

for page in os.listdir(datadir):
   discard = 1
   price = 0

   f = iter(open(datadir + "\\" + page, 'r', encoding = "ISO-8859-1"))
   for line in f:
    ##1. Find beginning of product list
    ##2. Find name of an item
    ##3. Find price of an item
    ##4. Find end of product list

        ##1##
        if '<table class="productlist">' in line:
           discard = 0
        if discard == 0:

           ##2##
           ##Regular Expession to pick the name of the game
           regu = re.search('\<a href=\"\/fi-fi\/leikki_ja_gadgets\/[\d\D[^"]*"\>(.*)\<\/a>.*',line)
           if regu != None:
              name = regu.group(1)

           ##3##
           if '<td class=\"price\">' in line:
              price = 1
           elif price == 1:
                 price = 2
           elif price == 2:
                 price = 0
                 ##Regular Expession to pick the price of the game
                 regu = re.search('(\S*)&',line)
                 if regu != None:
                    katalogi[name] = regu.group(1)
                    web.write(name + "---" + regu.group(1))
                    web.write("\n")

           ##4##
           if '</table>' in line:
              discard = 1
   f.close()

##Print Collected Catalogue Size
print('Items in catalogue: ' + str(len(katalogi)))
web.close()

"""
##Open wishlist
f = open("wishlist.txt", 'r')

for line in f:
    toivelista.append(line.strip())

f.close()

##Print out number of items in wishlist
print('Items in wishlist: ' +str(len(toivelista)))

##Write the names and prices to a file
f = open("webhallen.txt", 'w')
f.write('Items in wishlist: ' +str(len(toivelista)))
for name in toivelista:
    f.write("\n")
    if name in katalogi:
        f.write(name + " " + str(katalogi[name]))
    else:
        f.write(name + " ---")
"""
