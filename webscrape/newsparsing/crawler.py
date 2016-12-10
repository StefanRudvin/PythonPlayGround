import requests
from bs4 import BeautifulSoup
from time import sleep

def main():
    with open("log.txt") as f:
        for line in f:
            getLinks(line)
            #print(line + "\n")


def getLinks(html):
    #print(html)
    visitSite(html)

#Return list of links from site
def visitSite(link):
    response = requests.get(link)
    txt = response.text
    soup = BeautifulSoup(txt, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        print('')
        for address in href:
            print(address)
        #href = link.get('href')
        #links += href
    #print(links)


if __name__=='__main__':
    main()
