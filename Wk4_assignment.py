# Coursera.org /Learn to Program and Analyze Data with Python Specialization
# Course 3 - Using Python to Access Web Data
# Week 4
# Assignment: Scraping HTML Data with BeautifulSoup
"""
The program will use urllib to read the HTML from the provided data file, parse the data, extracting numbers and
compute the sum of the numbers in the file.
"""
import urllib
from BeautifulSoup import *

url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_169860.html"
html = urllib.urlopen(url)
print type(html)
html_data = html.read()
print type(html_data)

soup = BeautifulSoup(html_data)
print type(soup)
tags = soup('span')
print type(tags) #list of 'BeautifulSoup.Tag' instances

print type(tags[1])


print sum([int(tag.contents[0]) for tag in tags])

