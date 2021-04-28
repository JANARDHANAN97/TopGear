# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 19:37:41 2019

@author: janar
"""
def fibonacci(n):
    fib1=1
    fib2=2
    fib3=fib1+fib2
    print(1)
    for i in range(n):
        fib1=fib2
        fib2=fib3
        fib3=fib1+fib2
        yield fib1

a=fibonacci(5)
print(next(a))
print(next(a))
