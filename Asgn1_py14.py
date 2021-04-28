# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:08:30 2019

@author: janar
"""
"""a) Print all names on to screen 
     b) Read the index from the  user and print the corresponding name from both list. 
     c) Print the names from 4th position to 9th position 
     d) Print all names from 3rd position till end of the list 
     e) Repeat list elements by specified number of times ( N- times, where N is entered by user) 
     f)  Concatenate two lists and print the output. 
     g) Print element of list A and B side by side.( i.e.  List-A First element ,  List-B First element """
     
emp_id=['e1','e2','e3','e4','e5','e6','e7','e8',"e9","e10"]
emp_name=["bala","jana","karthi","dharma","surya","simbu"
          "vijay","elaiya","suganthi","bharathi"]
print(emp_id,emp_name)
ind=int(input())
print(emp_id[ind],emp_name[ind])
print(emp_id[4:10],emp_name[4:10])
print(emp_id[3:],emp_name[3:])
n=int(input())
print(emp_id*n,emp_name*n)
print(emp_id+emp_name)
for (i1,i2) in zip(emp_id,emp_name):
    print(i1,i2)
