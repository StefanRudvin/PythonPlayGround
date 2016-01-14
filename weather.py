import os
import random
import urllib.request
import re
import os.path

def greeting():
    os.system('clear')
    print('       --------------------------       ')
    print('------ Welcome to the weather app ------')
    print('       --------------------------       ')
    print('Enter 1 for puuro app, 2 for weather app: ')
    return ""

def puuro():
    #Puuro & Method checks if you can use methods within methods
    print('       --------------------------       ')
    print('------       This is puuro       -------')
    print('       --------------------------       ')
    print('What is your name?')
    print(question(input()))

def question(name):
    os.system('clear')
    print('Does puuro print method with ' + name + '?')
    print('Yes it does.')
    return ""

# hhttp://ilmatieteenlaitos.fi/saa/espoo
def makeurl(location):
    global url
    url = "http://ilmatieteenlaitos.fi/saa/" + location
    print(url)
    return url

def gettext(url):
    global text
    with urllib.request.urlopen(url) as response:
        html = response.read()
        ##Change binary into readable text
        text = html.decode("ISO-8859-1")
    f = open("weather.txt", 'w', encoding = "ISO-8859-1")
    f.write(text)
    f.close()

def getweather():
    name = 0
    f = open("weather.txt")
    stuff = f.readlines()
    f.close()
    lines = 0
    for line in stuff:
        if 'weather' in line:
            name = 1
            lines += 1
        elif name == 1:
            name = 0
            print('Joo')
    print(lines)

def playAgain():
   # This function returns True if the player wants to play again, otherwise it returns False.
   print(' ')
   print('Try again? (yes or no)')
   return input().lower().startswith('y')

### Methods end ####

print(greeting())

tries = 0

a = input()

if a == '1':
    os.system('clear')
    print(puuro())
elif a == '2':
    #Ask user for location
    print('This is the weather app')
    while True:
        os.system('clear')
        if tries == 0:
            print('Enter your location: ')
        else:
            print('Enter your new location: ')
        location = input()
        os.system('clear')
        makeurl(location)
        gettext(url)
        getweather()
        #print('The weather in ' + 'location' + ' is ' + 'final')
        tries = 1
        if not playAgain():
            break
else:
    print('Invalid input. ')
