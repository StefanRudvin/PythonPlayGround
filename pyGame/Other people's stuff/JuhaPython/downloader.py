##Python koodaus
import urllib.request
import os.path
import time

##Get the urls from a file
f = open("urllist.txt")
urlfile = f.readlines()
f.close()

##We download the files straight from the websites with Python urllib
for line in urlfile:
    filedir = line.split(';')[0]
    filename = line.split(';')[1]
    url = line.split(';')[2]
    print("Downloading: " + url)
    with urllib.request.urlopen(url) as response:
        html = response.read()
        ##Change binary into readable text
        text = html.decode("ISO-8859-1")

    ##Save to file and create its directory if it doesn't exist
    if (os.path.exists(filedir) == 0):
        os.mkdir(filedir)
    f = open(filedir + "\\" + filename, 'w', encoding = "ISO-8859-1")
    f.write(text)
    f.close()
    time.sleep(0.2)
