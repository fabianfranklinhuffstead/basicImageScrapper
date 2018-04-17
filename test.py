import urllib.request
from bs4 import BeautifulSoup

page = urllib.request.urlopen('https://yahoo.com').read()
soup = BeautifulSoup(page, "html.parser")
counter = 0
for img in soup.find_all('img'):
    with open("image" + str(counter) + ".png", 'wb') as f:
        print(img['src'])
        f.write(urllib.request.urlopen(img['src']).read())
    counter += 1
