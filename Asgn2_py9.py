# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:39:04 2019

@author: janar
"""

"""Write an iterator class that iterators over a sequence
 of values in the reverse direction""" 

class Reverse:
    def __init__(self,s):
        self.n=-1
        self.s=s
    def __iter__(self):
        self.s=self.s
        return self
    def __next__(self):
        s1=s[self.n]
        self.n+=-1
        return s1

c=Reverse("12345")
obj=iter(c)
print(next(obj))
print(next(obj))
print(next(obj))
     
