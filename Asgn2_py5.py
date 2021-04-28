# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:30:41 2019

@author: janar
"""
import re
s= "aa my ieo abc"
s=str(input())
z=re.findall("[aeiou]{2,}",s)
print(z)