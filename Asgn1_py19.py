# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 09:14:13 2019

@author: janar
"""    
#PRINTING EVEN VALUES FROM 1 TO 100
for i in range(101):
    if(i%2==0):
        print(i)
''' A) PART
1)break at 50'''
for j in range(101):
    if(j%2==0):
        if(j != 50):
            print(j)
        else:
            break
    else:
        pass

'''2)using continue for 10,20,30,40,50'''
for j in range(101):
    if(j%2==0):
        if(j in (10,20,30,40,50)):
            continue
        else:
            print(j)   
    else:
        pass

""" B) PART
Implemented both (1) and (2)
1)break at 90
2) use continue for 60,70,80,90  """     
i=1
while(i<101):
    if(i%2==0):
        if(i in (60,70,80,90)):
            if(i==90):
                break
            else:
                i+=1
                continue
        else:
            print(i)
    else:
        pass
    i+=1
    