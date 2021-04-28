# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 18:35:23 2019

@author: janar
"""

c = 0
def f2(x):
    c+= 1
    b = x + c
    print(c)
    return b
#print(f2(2))
try:
    print(f2(1))
    print(c) 
except UnboundLocalError: 
    try:
        print(f2(1))
    except :
        print("Exception occurred")              
else:
    print("Code executed without exception")
finally:
    print("Code executed") 