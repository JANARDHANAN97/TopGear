# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 08:56:14 2019

@author: janar
"""
''' printing 1 to 100 using for loop '''
for i in range(1,101):
    print(i)
    
''' printing in reverse using for '''
v=100
for j in range(1,101):
    print(v)
    v-=1
    
 ''' printing 1 to 100 using while loop '''   
i=1
while(i<101):
    print(i)
    i+=1
    
 ''' printing 1 to 100 using while loop '''   
i=100
while(i>0):
    print(i)
    i-=1
    
''' printing string elements seperately '''
my_string = "Hello World"
for i in range(len(my_string)):
    print(my_string[i])