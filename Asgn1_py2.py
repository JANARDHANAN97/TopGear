# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 22:12:05 2019

@author: janar
"""
"""Write a program to find the biggest of 3 numbers ( Use If Condition ) """
a=int(input())
b=int(input())
c=int(input())

if(a>b and a>c):
    print("The biggest of three numbers ",a,b,c, "is",a)
elif(b>a and b>c):
    print("The biggest of three numbers ",a,b,c, "is",b)
else:
    print("The biggest of three numbers ",a,b,c, "is",c)

        