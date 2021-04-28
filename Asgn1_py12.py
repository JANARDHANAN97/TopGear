# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:35:57 2019

@author: janar
"""
"""Read 10 numbers from user and find the average of all. 
a) Use comparison operator to check how many numbers are less than average and print them 
b) Check how many numbers are more than average. 
c) How many are equal to average."""

l1=[]
for i in range(2):
    a=int(input())
    l1.append(a)
print(l1)
avg=sum(l1)//len(l1)
print("Average of no's:",avg)
a=0
b=0
c=0
for i in l1:
    if(i<avg):
        a +=1
        print(i, "is less than avg")
    elif(i>avg):
        b+=1
        print(i, "is greater than avg")
    else:
        c+=1
        print(i, "is equal to avg")
        
print(c,"no's are equal to avg")
print(a,"no's are less than avg")
print(b,"no's are greater than avg")