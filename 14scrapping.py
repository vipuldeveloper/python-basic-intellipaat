#used: pip install beautifulsoup4, pip install lxml requests
#parser: lxml’s HTML parser, html5lib

#AGENDA
    # Web scrapping
    # Beutifulsoup
    # Scrapy
    # Parsers
    # Parsing HTML
    # Extracting Links

#run: lite-server

import imp
from bs4 import BeautifulSoup
import requests
import csv

soup = BeautifulSoup(requests.get("http://localhost:3000/scrapfile.html").text, 'lxml')
#print(soup.prettify())

csvfile = open("data.csv", "w")
csvwritter = csv.writer(csvfile)
csvwritter.writerow(['title', 'link'])

headings = soup.find_all("div", class_="post")
# print(headings.h2.a.text)
# print(headings.h2.a['href'])

for heading in headings:
    atitle = heading.h2.a.text
    ahref = heading.h2.a['href']
    row = [atitle, ahref]
    csvwritter.writerow(row)
    
csvfile.close()