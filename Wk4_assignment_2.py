# Coursera.org /Learn to Program and Analyze Data with Python Specialization
# Course 3 - Using Python to Access Web Data
# Week 4
# Assignment: Scraping HTML Data with BeautifulSoup/ Following Links in Python
"""
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags,
scan  for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number
of times and report the last name you find.
"""
import urllib
from BeautifulSoup import *

count = 7
position = 18
name_list = []
url_list = []
url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Vicky.html "

while count != 0:

    html = urllib.urlopen(url)
    html_data = html.read()
    soup = BeautifulSoup(html_data)
    tags = soup('a')


    url_list = [tag.get('href', None) for tag in tags]
    name_list = [tag.contents[0] for tag in tags]

    url = url_list[position-1]
    name = name_list[position-1]

    name_list = []
    url_list = []

    count -= 1

print name