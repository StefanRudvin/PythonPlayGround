import bs4 as bs
import urllib.request
import requests
import re
import os

class comic():
    """docstring for comic."""
    def __init__(self, url, currentNumber=1):
        super(comic, self).__init__()
        self.url = url
        self.currentNumber = currentNumber

    def getxml(self):
        try:
            source = urllib.request.urlopen(self.url).read()
            soup = bs.BeautifulSoup(source,'lxml')
            self.soup = soup
            return soup
        except Exception as e:
            print("Could not open Url")
            print(e)

    def imgurl(self):
        try:
            imgs = self.soup.findAll("div", {"id":"comic"})[0]
            image = imgs.find("img")
            imageSrc = image['src']
            imgurl = "http://" + imageSrc.replace("//", "")
            self.imgurl = imgurl
        except Exception as e:
            print("Something went wrong with the parsing.")
            print(e)

    def downloadimg(self):
        imgname = self.imgurl.strip("http://imgs.xkcd.com/comics/")
        imgname = imgname.strip(".jpg")

        filename = str(self.currentNumber) + "_" + imgname + ".jpg"

        img = urllib.request.urlopen(self.imgurl).read()

        path = './xkcd/'
        if not os.path.exists(path):
            os.mkdir(path)

        with open(os.path.join(path, str(filename)), 'wb') as temp_file:
            temp_file.write(img)

# get latest image number
def getMaxImage():
    url = "https://xkcd.com/"
    Comic = comic(url)
    page = Comic.getxml()
    page = page.findAll("ul", { "class" : "comicNav" })[0]
    href = page.findAll("a")[1]
    print(href)

def main():
    print("-- Welcome to the xkcd image downloader --")
    print("Files are created in ./xkcd in the root of this program.")
    getMaxImage()
    x = input("Enter range of images to download(e.g. 30-40) or single number: ")

    if "-" in x:
        startNum = int(x.split("-")[0])
        endNum = int(x.split("-")[1])
    else:
        startNum = int(x)
        endNum = int(startNum)

    baseurl = "https://xkcd.com/"

    for i in range(startNum,endNum+1):

        url = baseurl + str(i)
        Comic = comic(url, i)
        Comic.getxml()
        Comic.imgurl()
        Comic.downloadimg()

        print("Image number",i , "from url", url, "downloaded.")


    print("Script done.",(endNum+1) - startNum,"images downloaded.")


if __name__ == '__main__':
    main()
