# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 08:40:20 2019

@author: janar
"""
''' function for biggest and smallest of n numbers'''
l1=[1,3,2,4,8,56,76]


min1=l1[0]
max1=0

for i in l1:
    if(i>max1):
        max1=i
    if(i<min1):
        min1=i
print(max1)
print(min1)