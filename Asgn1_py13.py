# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:47:27 2019

@author: janar
"""
""""a)  Read 4 numbers from user using Input statement. 
   b) extend the above program to find the biggest of 5 numbers."""
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
if(a>b and a>c and a>d):
    print(a,"is biggest of all numbers")
elif(b>c and b>d and b>a):
    print(b,"is biggest of all numbers")
elif(c>a and c>b and c>d):
    print(c,"is biggest of all numbers")
else:
    if(e>d):
        print(e,"is biggest of all numbers")
    else:
        print(d,"is biggest of all numbers")