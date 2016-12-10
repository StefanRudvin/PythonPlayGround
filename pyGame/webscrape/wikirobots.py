import requests
response = requests.get("https://en.wikipedia.org/robots.txt")
txt = response.text
print(txt)
