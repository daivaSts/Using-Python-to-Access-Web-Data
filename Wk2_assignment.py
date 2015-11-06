# Coursera.org /Learn to Program and Analyze Data with Python Specialization
# Course 3 - Using Python to Access Web Data
# Week 2
# Assignment: Extracting Data With Regular Expressions

import re

hand = open('regex_sum_actual.txt','r')
number_list = []
result = 0

# VERSI0N 1
# for line in hand:
# 	line = line.rstrip()
# 	line_numbers = re.findall('[0-9]+',line)
# 	number_list += line_numbers

# for num in number_list:
# 	result += int(num)


#VERSION 2
print sum( [ int(i) for i in re.findall('[0-9]+', hand.read()) ] )
hand.close()