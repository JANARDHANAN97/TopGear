# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:49:11 2019

@author: janar
"""
"""Write a program to read string and print each character separately. 
    a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings. 
    b) Repeat the string 100 times using repeat operator * 
    c) Read strig 2 and  concatenate with other string using + operator. """
s1=str(input())
for i in range(len(s1)):
    print(s1[i])
print(s1[1:5])#slicing
print("Repeating the string 100 times", s1*100)
s2=input()
print("concatenating s1 and s2 :", s1+s2)