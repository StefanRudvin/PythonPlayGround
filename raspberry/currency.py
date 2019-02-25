import requests

url = "http://api.fixer.io/latest?symbols=USD,GBP"

def getCurrencyString():
    return "The euro to pound currency rate is {}.".format(parseCurrency())

def parseCurrency():
    data = getRequestJSON(url)
    return round(data['rates']['GBP'], 3)


def getRequestJSON(url):
    response  = requests.get(url)
    return response.json()
