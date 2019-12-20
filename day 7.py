#!/usr/bin/env python
# coding: utf-8

# In[2]:


# input:lst1=[4,3,6,8]
# output:lst2=[16,9,36,64]
lst1=[4,3,6,5]
lst2=[]
for i in lst1:
    lst2.append(i*i)
for i in lst2:
    print(i,end=" ")


# In[3]:


# list comprehension
lst3=[i*i for i in lst1]
lst3


# In[6]:


# square of even elements in another list
lst1=[4,3,6,8]
lst2=[]
for i in lst1:
    if i%2==0:
        lst2.append(i*i)
for i in lst2:
    print(i,end=" ")


# In[7]:


lst3=[i*i for i in lst1 if i%2==0]
lst3


# In[13]:


# function
# def function name(list of arguments):
#----------
#----------
# return
def add(x,y):
  print(x+y)
add(2,3)
#print(add(2,3))


# In[10]:


help("keywords")


# In[18]:


# create a given function and check whether the given num is palindrome or not.
def palin(num):
    if(num[::-1]==num):
     print("palin")
    else:
     print(no)
num=input("enter num")
palin(num)


# In[23]:


# another method
def palin(num):
    rev=0
    temp=num
    while num!=0:
      rev=(rev*10)+(num%10)
      num=num//10
    if temp==rev:
        return True
    else:
        return False
palin(121)


# In[29]:


# factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(factorial(5))


# In[27]:


# factorsum
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
def factsum(n):
    sum=0
    temp=n        
    while n!=0:
        r=n%10
        sum+=factorial(r) # nested func
        n//=10
    if temp==sum:
        return "YES"
    else:
        return "NO"
print(factsum(145))


# In[33]:


# types of arguments
# 1.required positional arguments
# 2.Default arguments
# 3.keyword arguments
# 4.variable-length arguments
def add(x,y,z=9):
    return x+y+z
add(10,20)


# In[34]:


def add(x,z):
    print(x)
    print(z)
    return x+z
add(z=10,x=20)


# In[37]:


def add(x,y):
    return x+y
def add(x,y,z): # fun overloading is not there in python
    return x+y+z
print(add(2,3))
print(add(3,4,5))


# In[41]:


def add(*x):
    sum=0
    for i in x:
        sum+=i
    return sum

print(add(2,3))
print(add(3,4,5))


# In[42]:


help("math")


# In[43]:


import math
math.exp(2)


# In[45]:


from math import factorial
factorial(4)


# 1. random
# 2. statistics
# 3. os
# 4. turtle->graphics
# 5. sqllite3->database
# 6. tkinter->GUI
# 7. smtplib->sending mails using python code
# 

# In[47]:


# file handling
# operations->open,write,save,close,read
# mode->read(r),write(w),append(a)
f=open("data.txt","w")
f.write("hello world")
f.close()


# In[50]:


f=open("data.txt","a")
f.write("hey")
f.close()


# In[55]:


f=open("data.txt","r")
data=f.read()
print(data)
f.close()


# In[56]:


# counting num of characters in given file
print("num of characters",len(data))
print("num of words",len(data.split()))


# In[57]:


# count the num of vowels in a given file
vowels="aeiouAEIOU"
count=0
for i in data:
    if i in vowels:
        count+=1
print(count)        


# In[ ]:


# 1.create a folder
# 2.goto that folder and create random number of files
# 3.each and every file should be unique
# 4. add content to the file,content should be unique from each and every file
# 5.filesize should be 512kb


# In[59]:


import os
help("os")


# In[60]:


a=[1,2,3,4,5,6,7,8,9]
print(a[::2])


# In[61]:


for num in range(2,5,1):
    print(num)


# In[ ]:


a={}

