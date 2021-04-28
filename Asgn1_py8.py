# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:07:08 2019

@author: janar
"""
"""Repeat program 7 with Tuple( Take example from Tutorial ) """

t1=(1,'a',1+6j,"str")
for i in t1:
    print(i)
print(t1[1:])
print(t1[:])
print(t1[::-1])
print(t1*3)
t2=("name","job")
print("concatenation : ",t1+t2)