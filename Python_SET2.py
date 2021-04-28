#!/usr/bin/env python
# coding: utf-8

# Using the built-in functions on Numbers perform following operations
# a) Round of the given floating point number. Example:  n=0.543 then round it next decimal number, i.e n=1.0 Use round() function
# b) Find out the square root of a given number. (Use sqrt(x) function)
# c) Generate random number between 0, and 1 ( use  random() function)
# d) Generate random number between 10 and  500. (Use uniform() function)
# e) Explore all Math and Random module functions  on a given number/ List.
# 

# In[29]:


import random
from math import *
n = 0.543
print("Rounding of to next digit", round(n))
print("Sqrt of n",sqrt(n))
print("Random no b/w 0 and 1", random.random())
print("Random no b/w 10 and 500",random.randint(10,500))

Read the value x and y from the user and apply all trigonometric functions on these numbers.
Note: Refer the tutorial Trigonometric operation table.
# In[30]:


x,y = map(eval,input("Enter two values with spaces : ").split())
print(sin(x), cos(x), tan(x))
print(sin(y), cos(y), tan(y))


# 23	Math – math.pi application	Find the area of Circle given that radius of a circle. (Use pi value from Math module as mathematical constant)

# In[31]:


r= int(input("Enter radius of circle"))
print("Area of Circle : ",pi*(r**2))


# 24	Strings	Special Characters: Write program to explore all Escape characters specified in Tutorial (Under String chapter)

# In[32]:


print("Using backslash \"Here\" ")
print("Printing \n new line")
print("tab escape character \t tab")
print("back \b backspace will be deleted")
print("\x48\x65\x6c")
print("\110\145\154")


# 25	Strings	Write a program to print the different data types (Numbers, strings characters) using the Format symbols (Refer to different format symbols specified in Tutorial)

# In[33]:


print("Integer %d %d" %(54, 5))
print("float %f and with two decimal %.2f "%(54.5656,5.6789))
print("My name is %s"%"jana")
print("printing hex value %x"%54)


# 26	Strings	Receive the encoded string from your friend & decode it to check the original message. PS: You will receive Encoded string and the Algorithm used for encoding.

# In[34]:


s1 = "HI this is encoded statement python"
s1 = s1.encode("ascii")
print(s1)

# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode()

# print result
print('The encoded version is:', string_utf)

string_utf.decode()


# Write a program to check given string is Palindrome or not.That is reverse the given string and check whether it is same as original string, if so then it is palindrome.
# Example: String = "malayalam"  reverse string = "malayalam" hence given string is palindrome. Use built functions to check given string is palindrome or not.
# 

# In[38]:


s1 = "malayalam"
s1 == str.lower(s1[::-1])
if s1:
    print("palindrome")
else:
    print("Not Palindrome")


# 28	Strings	Write a program to check how many ovals present in the given string. That is, count the number of " a e i o u" in the given string and print the numbers against each oval. Example:- "This is Python" Number of total ovals = 3, i = 2, o =1

# In[39]:


vowels = list("aeiou")
s2 = "This is Python"
for i in vowels:
    print(i, s2.count(i))

29	Strings	Apply all built in functions on Strings in your program. Note: There are 40 string functions. Use Tutorial for the help. Note: Each program should have 5 string built in functions(so write 8 programs to cover all string functions)
# In[3]:


def  fun1(string):
    print("Original string : ",string)
    print("String in upper case: ",string.upper())
    print("string in lower case: ",string.lower())
    print("string with first letter capitalize", string.capitalize())
    print("String with first character of each word to upper case:", string.title())
    print("swapcase  of original string(lower to upper and viceversa): ", string.swapcase())


# In[4]:


fun1("Sample string")


# In[1]:


def fun2(string, s):
    print("Original string : ",string)
    print("Using find() to find the first occcurence index of char in string ",string.find(s))
    print("Using index() to find the first occurence index of specified char from the string ",string.index(s))
    print("Using rfind() to find the last occcurence index of char in string ",string.rfind(s))
    print("Using rindex() to find the last occurence index of specified char from the string ",string.rindex(s))
    print("retunrs number of times a specified value occurs in string : ", string.count(s))
   


# In[5]:


fun2("sample string", "s")


# In[31]:


def fun3(string):
    print("Orginal String", string)
    print("does string contains only alpha and numeric? : ", string.isalnum())
    print("does this string is only alpha : ", string.isalpha())
    print("does this string is only numeric : ", string.isnumeric())
    print("does this string is only digit : ", string.isdigit())
    print("does this string is only decimal : ", string.isdecimal())
#isdigit vs isdecimal vs isnumeric : https://stackoverflow.com/questions/22789392/str-isdecimal-and-str-isdigit-difference-example


# In[27]:


fun3('-1.13')#'.' and '-' are not considered as alpha, numeric, digits or decimal


# In[32]:


def fun4(string):
    print("does all the characters in the string are lower? ", string.islower())
    print("does all the characters in the string are upper? ", string.isupper())
    print("does all the characters in the string are spaces? ", string.isspace())
    print("does the string is title ? ", string.istitle())
    print("does the string is identifier ? ", string.isidentifier())


# In[36]:


fun4("143 H")


# In[19]:


def fun5(s, new_value, old_value, count):
    print("checking if the string starts with specified char ",s.startswith(new_value))
    print("checking if the string ends with specified char ", s.endswith(new_value))
    print("replacing old value with new specified character for given times", s.replace(new_value, old_value,2))
    print("places the string in center with total length", s.center(count))
    print("string is encoded in this format", s.encode(encoding="ascii", errors="ignore"))


# In[20]:


fun5("string to be experimented with five functions", "#", 's', 2)


# In[10]:


def fun6(string):
    print("converts string into lower case:",string.casefold())
    print("sets the tab size with specified number of size", string.expandtabs(3))
    print("My name is {0} and I am working in {company}".format("Jana",company="Wipro"))
    print("Join iterables using a string and make as one string","#%".join({"name": "John", "country": "Norway"}))
    print("string will be in left and remaining total specified lnwgth will be filled by spaces(default) or specified char : \n ",
          string.ljust(30,"$"))


# In[11]:


fun6("text string to check fun6")


# In[17]:


def fun7(string):
    print("left stripremoves leading char from string(space is default) :", string.lstrip())
    print("similarly rsplit : ",string.rstrip())
    x = str.maketrans("sab","bas","0")
    print("make trans makes table with string-replace string each char used with table", x)
    print("using translate : ", string.translate(x))
    print("rjust string will be in right of total char", string.rjust(30,"$"))
    


# In[19]:


fun7("   function 7   ")


# In[29]:


def fun8(string, txt):
    print("format_map {x} {y}".format_map(dict(x=30, y =40)))
    print("zfill fills zero at beginning until specified length", string.zfill(20))
    print("title - first char in every word is upper case", string.title())
    print("partition method splits the string into three before match, first match, after match", string.partition(txt))
    print("partition method splits the string into three before match, last match, after match", string.rpartition(txt))
    


# In[30]:


fun8("string to use"," fun8")

30.Write a program to Sort given N numbers (Use only loop structures and Conditions to sort the elements. Use Bubble sort / Selection sort technique to sort the elements of List) Note: Don't use built in functions to sort.
# In[32]:


l1 = [4, 3, 2, 6, 1]

for i in range(len(l1)):
    for j in range(i,len(l1)-1):
            if l1[i]>l1[j+1]:
                x = l1[i]
                l1[i] = l1[j+1]
                l1[j+1] = x
l1


# 31. Write a program to search an element in the list. i.e. Perform the binary search on the sorted list having integers as elements. If the search is successful print "Success" else print "un successful search".

# In[33]:


l1 = [4, 3, 2, 6, 1]

x = 5
for i in range(len(l1)):
    if x==l1[i]:
        print("Success")
        break
    if i==len(l1)-1:
        print("Unsuccessful")


# 32 . Write a program to perform following operations on List. Create three lists as List1, List2 and List3 having 5 city names each list.
# a. Find the length city of each list element and print city and length
# b. Find the maximum and minimum string length element of each list
# c. Compare each list and determine which city is biggest & smallest with length.
# d. Delete first and last element of each list and print list contents.
# 

# In[34]:


l1 = ['Delhi','Jaipur','Chennai','Bangalore','Pune']
l2 = ['Hyderabad','Goa','Ranchi','Patna','Cochin']
l3=['Vizag','Vishakapatnam','Bhubneshwar','Kolkata','Gangtok']

x = [list(map(lambda x: [x, len(x)],i)) for i in (l1,l2,l3)]

print("Length city of each list",x)

x = [sorted(i, key = lambda x:x[1]) for i in x]

ls = []
[ls.append([i[0],i[-1]]) for i in x]
for i in ls:
    print(i)
    
print("Min string length",min(ls, key = lambda x:x[1]))
print("Max length ",max(ls, key = lambda x:x[1]))
[print("deleting first and last element of each list",i[1:-1]) for i in (l1,l2,l3)]    


# 33 . Create a list with 7 elements and perform following operations. Let the list be initialized with List1 any 5 city names;
# a) Append a new city name to the List
# b) Insert a city name at 4th index position
# c) Sort the list and print all elements
# d) Sort the elements of the list in descending order.
# e) delete last three elements using pop operation
# 

# In[35]:


l1 = ['Delhi','Jaipur','Chennai','Bangalore','Pune','Hyderabad','Goa']

l1.append("Mumbai")
print("Adding new city ",l1)

l1[4] = "chn"
print("Inserting in 4th index",l1)

l1.sort()
print("sort the elements",l1)

l1.sort(reverse=True)
print("sort the elements desc",l1)

for i in range(3):
    l1.pop()
    
print("deleting last three elements",l1)


# 34	Strings	Create 3 Lists (list1, list2, list3) with integer and perform following operations
# a) Create Maxlist by taking 2 maximum elements from each list.
# b) Find average value from all the elements of Maxlist.
# c) Create a MinlIst by taking 2 minimum elements from each list 
# d) Find the average value from all the elements of Minlist
# 

# In[36]:


import random
il1 = [random.randint(1,10) for i in range(5)]
il2 = [random.randint(10,20) for i in range(5)]
il3 = [random.randint(20,30) for i in range(5)]

max_list = []
min_list = []

for i in (il1,il2,il3):
    max_list.extend(sorted(i)[-2:]) 
    min_list.extend(sorted(i)[:2])

print("Max list by taking 2 max elements",max_list)
print("Min list by taking 2 min elements",min_list)
print("Average elements",sum(min_list)/len(min_list))


# 35 . Create Tuple as specified below;
# a) Create a Tuple tup1 with days in a week & print the tuple elements
# b) Create a Tuple tup2  with months in a year and concatenate it with tup1
# c) Create 3 tuples( tup1,tup2,tup3) with numbers and determine which is greater.
# d) Try to delete an individual element in tup1 and try deleting complete Tuple -tup1 notice the error type you get.
# e) Insert new element in to tuple by typecasting it to List
# 

# In[67]:


week_days= ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
months = ('Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov')

print(week_days + months)

tup1 = (1, 4, 7)
tup2 = (3, 4, 1)
tup3 = (0, 6, 5)
print("Max of three numbers",max(list(tup1+tup2+tup3)))

try:
    del tup1[0]
except Exception as e:
    print("Exception while deleting a element in tuple",e)
    
try:
    del tup1
    print("tuple1 deleted successfully")
except Exception as e:
    print("Exception while deleting tuple",e)
    
tup2 = list(tup2)
tup2.insert(2,5)
print(tuple(tup2))
    


# 36	Strings	Create two tuples tup1 & tup2 and apply all built in functions on tuples. ( Refer Tutorial for the Built in functions list)

# In[68]:


tup1 = (1,2,3,4,5,2,4,3)
tup2 = (6,7,8,9,10,10,0,8,9)

print("Index ",tup1.index(4))
print("Count ",tup2.count(10))
print("Concatenation ",tup1+tup2)


# 37. Create 3 dictionaries (dict1, dict2, dict3) with 3 elements each. Perform following operations
# a) Compare dictionaries to determine the biggest.
# b) Add new elements in to the dictionaries dict1, dict2
# c) print the length of dict1, dict2, dict3.
# d) Convert dict1, dict2, and dict3 dictionaries as string and concatenate all strings together.
# 

# In[70]:


dict1 = {1:"a", 2:"b", 3:"a"}
dict2 = {4:"d", 5:"e", 6:"f"}
dict3 = {7:"g", 8:"h", 9:"i"}

#Adding new elements
dict1[10]="J"
dict2[11]="A"

for i in (dict1, dict2, dict3):
    print("length ",len(i))
    
#Converting dict1, dict2, and dict3 dictionaries as string and concatenate all strings together.
dict4 = {**dict1, **dict2, **dict3}
print(dict4)

print(str(dict1)+str(dict2))


# Create 2 dictionaries as follows;
# dict1 ={'Name':'Ramakrishna','Age':25}
# dict2={'EmpId':1234,'Salary':5000}
# Perform following operations   
# a) Create single dictionary by merging dict1 and dict2
# b) Update the salary to 10%
# c) Update the age to 26
# d) Insert the new element with key "grade" and assign value as "B1"
# e) Extract and print all values and keys separately.
# f) delete the element with key 'Age' and print dictionary elements.
# 

# In[71]:


dict1 ={'Name':'Ramakrishna','Age':25}
dict2={'EmpId':1234,'Salary':5000}

dict3 = {**dict1, **dict2}
print("Merging two dict",dict3)

dict3["Salary"] = dict3["Salary"] + (dict3["Salary"]*0.1)
print("Update salary by 10%",dict3)

dict3.update(Age=26)
print("updating dict3",dict3)

dict3["grade"] = "B1"
print("Inserting grade",dict3)

del dict3["Age"]
print("deleting age",dict3)

print(dict3.keys(),"\n",dict3.values())

39	Dictionary  and Date & Time	Using Time and Calendar module, Print current date and time. Print current month calendar.
# In[72]:


import calendar, datetime


# In[73]:


#current date and time
current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(current_time)


# In[74]:


print(calendar.month(2021,3, 1, 1))

Using time module perform following operations.
a) Print current time for every 5 seconds up to 1 minute time interval.
b) Write a program to find out how much CPU time is taken for the execution of above(32.a)  program.

# In[75]:


from time import sleep, time
x=1
loop = True
while loop:
    if x:
        z1 = time()
        x = 0
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    sleep(5)
    z2 = time()
    y = round(z2-z1)
    if y>=60:
        loop = False

Write a program to perform following operations on List. Create three lists as List1, List2 and List3 having 5 city names each list.
a. Find the length city of each list element and print city and length

# In[76]:


t1 = time()
l1 = ['Delhi','Jaipur','Chennai','Bangalore','Pune']
l2 = ['Hyderabad','Goa','Ranchi','Patna','Cochin']
l3=['Vizag','Vishakapatnam','Bhubneshwar','Kolkata','Gangtok']
x = [list(map(lambda x: [x, len(x)],i)) for i in (l1,l2,l3)]
t2 = time()
print("Time taken to complete this programs is ", t2-t1)


# In[77]:


def code():
    try:
        return 1
    finally:
        return -1
code()

