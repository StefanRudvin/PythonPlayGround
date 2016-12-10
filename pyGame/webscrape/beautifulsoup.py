import requests
from bs4 import BeautifulSoup


response = requests.get("https://hs.fi/")
txt = response.text

soup = BeautifulSoup(txt, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))

#print(soup.prettify())

#print(soup.title)

#print(soup.title.name)

#print(soup.title.string)

#print(soup.title.parent.name)

#print(soup.p)

#print(soup.p['class'])

#print(soup.a)

#print(soup.find_all('a'))

#print(soup.find(id="link3"))
