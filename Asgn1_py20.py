# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 22:39:56 2019

@author: janar
"""
""" 1) printing fibonacci series """
n=int(input())
fib1=0
fib2=1
fib3=fib1+fib2

for i in range(n):
    print(fib1)
    fib1=fib2
    fib2=fib3
    fib3=fib1+fib2
""" 2) fibonacci series with max value (n) """
#b)
fib1=0
fib2=1
fib3=fib1+fib2
for i in range(n):
    if(fib1<n):
        print(fib1)
    else:
        break
    
    fib1=fib2
    fib2=fib3
    fib3=fib1+fib2

