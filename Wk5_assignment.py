# Coursera.org /Learn to Program and Analyze Data with Python Specialization
# Course 3 - Using Python to Access Web Data
# Week 5
# Assignment: Parsing/ Extracting Data from XML
'''
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data,
compute the sum of the numbers in the file and enter the sum,
'''
import urllib
import xml.etree.ElementTree as ET

comment_url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_169857.xml'
comment_data = urllib.urlopen(comment_url)
data = comment_data.read()

tree = ET.fromstring(data)
comment_list = tree.findall('.//comment')

suma = 0
for item in comment_list:
    content = item.find("count").text
    suma += int(content)
    
    name = item.find("name").text
   
print suma    