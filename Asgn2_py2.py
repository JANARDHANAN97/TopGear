# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:35:39 2019

@author: janar
"""
#a=int(input())
#try:
   # while(True):
   #    print("1")
try:
    a=int(input())
    x=9/a
    print(x)
    while(True):
        print("1")
    print(l)
except ArithmeticError:
    print("\n Enter a no other than 0")
    try:
        a=int(input())
        x=9/a
        print(x)
    except ArithmeticError:
        print("\n You have Entered 0")
except KeyboardInterrupt:
    print("\n Handled KeyboardInterrupt Exception")
except NameError:
    print("\n Variable is not initialized")
finally:
    print("\n session closed")
    