# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:56:54 2019

@author: janar
"""
"""
 Create a class called First and two classes called Second and
 Third which inherit from First. 
 Create class called Fourth which inherits from Second and Third.
 Create a common method called method1 in all the classes and
 provide the Method Resolution Order
"""

class First:
    def method1(self):
        print("First Method")

class Second(First):
        def method1(self):
            print("Second Method")

class Third(First):
        def method1(self):
            print("Third Method")

class Fourth(Second, Third):
        def method1(self):
            print("Fourth Method")

obj = Fourth()
print(obj.method1())
print(Fourth.mro())