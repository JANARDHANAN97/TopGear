# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 21:56:03 2019

@author: janar
"""

'''
a. digit at the beginning of the string and a digit at the end of the string 
b. A string that contains only whitespace characters or word characters 
c. A string containing no whitespace characters '''

import re
dir(re)
s1 = "Ticket number is 1xyz203"
s2 = "    "
s3 = " name"
x = re.findall("[0-9]+[\w]+[0-9]",s1)
y= re.findall("[\s] | [\w]",s2)
z= re.findall("[^\s]",s3)
print(x)
print(y)
print(z)