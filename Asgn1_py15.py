# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:32:11 2019

@author: janar
"""
''' a) Use membership operator ( IN ) to check the presence of an element. '''

l1=['a','d','c','b','e']
b='a' in l1
if b==True:
    print("name is present")
else:
    print("name is not present")

""" b) Perform above task without using membership operator. """
a='b'
n=0
for i in l1:
    if(a == i):
        print("name is present using for loop")
        break
    else:
        n+=1
#print(len(l1))
#print(n)
if(n==len(l1)):
    print("given name is not present in list using loop")
    
"""c) Print the elements of the list in reverse direction"""
print("Printing elements in reverse direction ",l1[::-1])