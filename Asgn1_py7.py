# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:00:59 2019

@author: janar
"""
"""Create a list with at least 10 elements in it 
       print all elements 
       perform slicing 
       perform repetition with * operator 
       Perform concatenation wiht other list. """
       
l1=["abc","123","def","456"]
for i in l1:
    print(i)
print(l1[:5])
print(l1[-5:-2])
print(l1[::-1])
print(l1[0:-1])
print("Repition : ", l1*100)
l2=["h",1.23,"fire"]
print("concatenation: ",l1+l2)