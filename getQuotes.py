# -*- coding: utf-8 -*-

# This is a simple python script that requests the name of a book/author 
# and prints out the top 30 relevant quotes as found on Goodreads (www.goodreads.com)

# This script uses BeautifulSoup-4 to perform the final html parsing to retrieve the quotes and
# a python wrapper for the Goodreads API to retrieve the relevant bookID from the given string raw_input

# Link to the python wrapper: https://github.com/sefakilic/goodreads 



from goodreads import client
import re
import urllib
from bs4 import BeautifulSoup


CONSUMER_KEY = "p2pwj3WQa62EwELBTz"
CONSUMER_SECRET ="d8bEXGOBhuGN0KybFpxJmOKdVU0FIPKJmhqZXsgU"

gc = client.GoodreadsClient(CONSUMER_KEY,CONSUMER_SECRET)

gc.authenticate()

bookName = raw_input("Enter the name of your favorite book(Enter Author's name to retrive top quotes from the author): ")

print "Hold on while we retrieve the top quotes..."


bookIdList = gc.search_books(bookName)

baseUrl = 'https://www.goodreads.com/work/quotes/'
editedBookName = bookName.replace(' ','-')
s = bookIdList[0]+'-'+editedBookName
finalUrl = baseUrl + s;
# print finalUrl

print "..............."
print 
print 

html = urllib.urlopen(finalUrl).read()
soup = BeautifulSoup(html,"lxml")

# print soup
quotesPart = soup.findAll("div",class_="quoteText")

for item in quotesPart:
    tex = str(item)

    matchQ = re.findall('“(.*)”',tex)
    print matchQ[0]
    print 
    print