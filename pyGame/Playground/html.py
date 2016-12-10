# write-html.py
import urllib
import urllib.request

def writehead(title):
    global head
    head = """<html>
    <head>
        <title>""" + title + """ </title>
    </head>"""

def writeBody():
    global body
    body = """<body><p>Hello World!</p>dasdadasdjajaja</body>"""
def writeFooter():
    global footer
    footer = """</html>"""

f = open('helloworld.html','w')
writehead("myTitle")
writeBody()
writeFooter()

f.write(head)
f.write(body)
f.write(footer)
f.close()

url = "http://inventwithpython.com/pygame/chapters/"

with urllib.request.urlopen(url) as murl:
    s = murl.read()
    htmlpage = s.split()

next = 0

'''
for word in htmlpage:
    if next == 1:
        print(word)
        next = 0
    if "Yliopistot" in str(word):
        next += 1
'''

wordfreq = []

for word in htmlpage:
    wordfreq.append(htmlpage.count(word))

print("Pairs\n" + str(zip(htmlpage, wordfreq)))
