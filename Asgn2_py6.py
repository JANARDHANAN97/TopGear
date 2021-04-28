# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:39:24 2019

@author: janar
"""

class sqroot:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sqroot(self):
        print(self.a**self.b)
    #def __init__(self,a,b)
    
class addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)

class subtraction:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sub(self):
        print(self.a-self.b)
        return self.a-self.b

class multiplication:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def mul(self):
        print(self.a*self.b)
        return self.a*self.b

class division:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def div(self):
        print(self.a/self.b)
        return self.a/self.b

        
class mathnew(sqroot,addition,subtraction,multiplication,division):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        super().__init(self.a,self.b)

obj=mathnew(2,4)
print(obj.__init__(2,4))





















