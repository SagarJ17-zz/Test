import requests as rs
from bs4 import BeautifulSoup as bs
import re
import numpy
import matplotlib
import pandas
import zipp
import hashin
import tensorflow
site = ''
req = rs.get(site)
soup = bs(req.text, 'html.parser')
urls = re.findall('(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})', str(soup))
print(urls)
"""link=input("Enter which url you want http or https:")

if link == "http":
    for i in soup.find_all('a',attrs={'href': re.compile("^http://")}):
        print(i.get('href'))

if link == "https":
    for i in soup.findAll('a',attrs={'href': re.compile("^https://")}):
        print(i)

        extract = ["Name:","License:"]
        for details in extract:
            if details in scan:
                #print(scan)
                list_one = scan.split(":")
                if list_one[1].find("UNKNOWN") != 1:
                    print(list_one[1])"""
