# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:43:19 2019

@author: janar
"""
''' i) Check whether given number is prime or not. ''' 
n=int(input())
b=int(n/2)
s1=2
for i in range(2,b+1):
    if(n%i==0):
        break
    s1+=1
if(s1>b):
    print(n," is a prime no")
else:
    print(n,"is not a prime no")
    
''' ii) Generate all the prime numbers between 1 to N where N is given number. '''

for i in range(1,n+1):
    if(i==1):
        print("1 is prime")
    else:
        c=int(i/2)
        s2=2
        for j in range(2,c+1):
            if(i%j==0):
                break
            s2+=1
            #print(s2)
        if(s2>c):
            print(i,"is a prime no")
        else:
            print(i,"is not a prime no")
    