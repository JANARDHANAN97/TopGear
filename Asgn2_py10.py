# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:02:57 2019

@author: janar
"""

""" Implement a decorator that quantifies and 
  returns the execution time of any function """
  
import time

def Time(org_fun):
    t1= time.clock()
    org_fun()
    t2=time.clock()
    print(t2-t1)
    return t2-t1

@Time
def ran():
    for i in range(10):
        pass
    
@Time 
def jog():
    for i in range(10000000):
        pass