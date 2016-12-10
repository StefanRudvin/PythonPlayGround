import requests
from lxml import html
page = requests.get("http://www.example.com").text
doc = html.fromstring(page)
link = doc.cssselect("a")[0]
print(link.text_content())
# More information...
print(link.attrib['href'])
# http://www.iana.org/domains/example
