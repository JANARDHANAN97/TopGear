# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 23:09:19 2019

@author: janar
"""

"""Write a program to receive 5 command line arguments 
   and print each argument separately. 
Example : 
  >> python test.py arg1 arg2 arg3 arg4 arg5 
  a) From the above statement your program should receive arguments
     and print them each of them.  
  b) Find the biggest of three numbers, where three numbers
     are passed as command line arguments. """

import sys
arg = sys.argv
for i in arg:
    print(i)
    
n1=0
for i in range(1,len(sys.argv)):
    n=int(sys.argv[i])
    if(n1<n):
        n1=n
print("biggest of command line arguments",n1)
    
