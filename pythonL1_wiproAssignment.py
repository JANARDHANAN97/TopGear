#!/usr/bin/env python
# coding: utf-8

# 1.	Given a list, url = [www.annauniv.edu, www.google.com, www.ndtv.com, www.website.org, www.bis.org.in, www.rbi.org.in]; Sort the list based on the top level domain (edu, com, org, in) using custom sorting

# In[2]:


url = ["www.annauniv.edu", "www.google.com", "www.ndtv.com", "www.website.org", "www.bis.org.in", "www.rbi.org.in"]
def srt(x):
    s = x.split(".")
    return (x,s[-1])

ls = ["edu", "com", "org", "in"]
print(sorted(list(map(srt, url)), key=lambda x: ls.index(x[1])))


# 2.	Given a list of strings, return the count of the number of strings where the string length is 2 or more and the first and last chars of the string are the same.  
# 
# i.	['axa', 'xyz', 'gg', 'x', 'yyy']
# ii.	['x', 'cd', 'cnc', 'kk']
# iii.	['bab', 'ce', 'cba', 'syanora']
# 

# In[5]:


ls1 = [['axa', 'xyz', 'gg', 'x', 'yyy'], ['x', 'cd', 'cnc', 'kk'],  ['bab', 'ce', 'cba', 'syanora']]
x = [len(list(filter(lambda x: len(x)>=2 and x[0]==x[-1], i))) for i in ls1]
for i in range(len(x)):
    print("count of string in {}st list {}".format(i+1,x[i]))


# 3.	Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin with 'x' first.  e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']. 
# Hint: this can be done by making 2 lists and sorting each of them before combining them.
# i.	['bbb', 'ccc', 'axx', 'xzz', 'xaa']
# ii.	['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
# 

# In[6]:


ls2 = [['bbb', 'ccc', 'axx', 'xzz', 'xaa'], ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']]

l1 = [list(filter(lambda x: x.startswith("x"),i)) for i in ls2]
l2 = [sorted(list(filter(lambda x: x[0]!='x', i))) for i in ls2]
print(l1)
print(l2)
print(list(map(lambda x,y: x+y, l1, l2)))


# 4.	Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple. 
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
#       Hint: use a custom key= function to extract the last element form each tuple.
# i.	 [(1, 3), (3, 2), (2, 1)]
# ii.	[(1, 7), (1, 3), (3, 4, 5), (2, 2)]
# 

# In[7]:


x = [(1, 7), (1, 3), (3, 4, 5), (2, 2)] 
print(sorted(x, key=lambda x:x[1]))


# 5.	Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element, so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.
# i.	 [1, 2, 2, 3], [2, 2, 3, 3, 3]
# 

# In[10]:


ls = [1, 2, 2, 3]
print(list(set(ls)))
ls = [2, 2, 3, 3, 3]
print(list(set((ls))))


# 6.	Write a function to print the information in the dictionary(bookstore) in the given format
# 
# bookstore={"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],"CHILDREN":["Harry Potter”, J K. Rowling","2005","29.99"],"WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}
# 
# 
# BOOKSTORE
# 
# 'Learning XML', 'Erik T. Ray', '2003', '39.95' 
# 'Everyday Italian', 'Giada De Laurent is', '2005', '30.00']
#  'Harry Potter', 'J K. Rowling', '2005', '29.99']
# 

# In[11]:


bookstore={"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],
                           "CHILDREN":["Harry Potter”, J K. Rowling","2005","29.99"],
                           "WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}
for i in list(map(lambda x: bookstore["New Arrivals"][x], sorted(bookstore["New Arrivals"], reverse=True))):
    print(i)


# 7.	Given a string, str1=""”Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."""
# a.	Build a dictionary, with "words as key" --> Frequency of occurrence as value
# E.g. Python 7, is3
# b.	Print the top 5 words with their frequency of occurrence

# In[12]:


str1="""Python is a widely used high-level programming language for general-purpose programming,
created by Guido van Rossum and first released in 1991. An interpreted language,
Python has a design philosophy which emphasizes code readability
(notably using whitespace indentation to delimit code blocks rather than curly braces or keywords),
and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages 
such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and
large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms,
including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard 
library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems.
CPython, the reference implementation of Python, is open source software and has a community-based development model,
as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."""


# In[14]:


s1 = str1.replace(".","").replace("(","").replace(")","").replace(",","").replace("-","").lower().split()
ls = [(i, s1.count(i))for i in set(s1)]
ls_sorted = sorted(ls, key= lambda x: x[1], reverse = True)
print(ls_sorted[:5])


# a.	Build a dictionary where the key is a word and the value is the list of words that are likely to follow.
# i.	E.g. Python  [is, has, features, interpreters, code, Software]. In this example the words listed are likely to follow “Python”
# b.	Given a word predict the word that’s likely to follow.
# 

# In[16]:


import re
s1 = re.sub(r"[-,.()]"," ",str1)
s1 = s1.replace("\n","").lower()
l1 = s1.split()
l1.index("python",10,len(l1))
d1 = {}

for j in set(l1):
    x = []
    i = 0    
    while True:
        try:
            x.append(l1.index(j,i,len(l1)))
            #print(l1.index("python",i,len(l1)))
            i = 1+l1.index(j,i,len(l1))
            #print(i)
        except ValueError:
            #print(x)
            d1.update({j:x})
            break
d2 = d1.copy()
print(dict(sorted(list(map(lambda x: (x[0],set([l1[i+1] for i in x[1] if (i+1)!=len(l1)])), d2.items())))))


# Below is the output of # show ip interface brief command on a router
# 
# Interface		IP-Address	OK? 	Method Status	Protocol
# FastEthernet0/0	192.168.1.242	YES 	manual up	up 
# FastEthernet1/0        unassigned	YES 	unset		down 
# Serial2/0              	192.168.1.250	YES 	manual up	up 
# Serial3/0              	192.168.1.233	YES 	manual up	up 
# FastEthernet4/0        unassigned	YES 	unset  		down	
# FastEthernet5/0        unassigned	YES        unset 		down
# 
# a.	Use regular expressions to extract and display Interface and method status for all the interfaces.
# i.	E.g.  FastEthernet0/0, manual up
# 

# In[20]:


st1 = """FastEthernet0/0 192.168.1.242 YES  manual up up 
FastEthernet1/0        unassigned YES  unset down 
Serial2/0              	192.168.1.250 YES  manual up up 
Serial3/0              	192.168.1.233 YES  manual up up 
FastEthernet4/0        unassigned YES  unset  down
FastEthernet5/0        unassigned YES unset down
"""
for line in st1.splitlines():
    match = re.match( r'(\w+\d\/\d)\s+[.0-9a-z]+\s+\w+\s+(\w+\s?\w+?)\s+\w+', line, re.M|re.I)
    
    if match:
        print( match.group(1),match.group(2))


# 10.	Given a number line from -infinity to +infinity. You start at 0 and can go either to the left or to the right. The condition is that in i’th move, you take i steps. In the first move take 1 step, second move 2 steps and so on. 
# Hint: 3 can be reached in 2 steps (0, 1) (1, 3). 2 can be reached in 3 steps (0, 1) (1,-1) (-1, 2)
# a) Find the optimal number of steps to reach position 1000000000 and -1000000000
# 

# In[23]:


def sm(x): 
    sum = int((x * (x + 1)) / 2) 
    return sum

 
def cnt(num): 

    n = abs(num) 
    result = 0 
    while (sm(result) < n or (sm(result) - n) & 1): 
        result += 1
    return result 

n = 3
print(cnt(n))


# In[ ]:




