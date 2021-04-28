# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 22:32:51 2019

@author: janar
"""
"""Write a program to find the number is Prime or not. """
a=int(input())
b=int(a/2)
print(b)
s=2
for i in range(2,b+1):
    if((a%i)==0):
        break
    s+=1
    print(s)
  
if(s>b):
    print(a,"is prime number")
else:
    print(a,"is non-prime number")
    