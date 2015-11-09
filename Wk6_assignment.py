# Coursera.org /Learn to Program and Analyze Data with Python Specialization
# Course 3 - Using Python to Access Web Data
# Week 6
# Assignment: Extracting Data from JSON
'''
The program will read the provided JSON data from that URL using urllib and then parse and extract the comment
counts from the JSON data, compute the sum of the numbers in the file and enter the sum below.
'''
import json
import urllib

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_169861.json'
url_instance = urllib.urlopen(url)
data_string = url_instance.read()

try: json_dict = json.loads(str(data_string))
except: json_dict = None

json_str = json.dumps(json_dict, indent=4)
#print json_str

json_list =json_dict["comments"]
total = 0

for num in range(len(json_list)):
    total += json_list[num]["count"]


print "Total comments count ", total