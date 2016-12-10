import requests
from bs4 import BeautifulSoup
from time import sleep

response = requests.get("https://hs.fi")
txt = response.text

soup = BeautifulSoup(txt, 'html.parser')
file = open("log.txt", "w")

x = eval(input("How many times do you want this to run:  "))
count = 0

for link in soup.find_all('a'):
    print(link.get('href'))
    file.write(str(link.get('href'))+ '\n')
    sleep(0.05)
    count += 1
    x -= 1
    if x < 1:
        break

file.close()

print("End of search. Final count: " + str(count))
