#!/usr/bin/env python
# coding: utf-8

# not 12>45

# # membership opearators
# 

# In[2]:


str="ambh kjd"


# In[7]:


print('h kjd' in str)
print('w' not in str)


# In[11]:


# identity operators-->is,is not
x=10
y=20
x is y


# In[12]:


print(id(x),id(y))


# In[13]:


x=10
y=20
print("x<y") if x<y else print("x>y")


# In[18]:


# accept a num as input and give whether given no is positve or negative or zero
num=int(input("enter number"))
if num>0:
    print("positive")
elif num<0:
    print("neagative")
else:
    print("zero")


# In[2]:


# divisible by 2 and 3
num=int(input("enter number"))
if num%2==0 and num%3==0 and num%4!=0:
    print(num)
else:
    print("not divisible")


# In[4]:


print("enter 3 subject marks")
sub1,sub2,sub3=map(int,input().split())
if (sub1>30 and sub2>30 and sub3>30):
    tot=sub1+sub2+sub3
    avg=tot/3
    if(avg>75):
     print("A")
    elif avg>65 and avg<75:
        print("B")
    elif avg>50 and avg<65:
        print("C")
    elif avg>30 and avg<50:
        print("D")
else:
    print("fail")


# In[7]:


# while loop
i=1
n=int(input())
while i<=n:
    print(i,end=" ")
    i+=1


# In[4]:


# sum of natural numbers
i=1
sum=0
no=int(input("enter num"))
while i<=no:
    if i%2==0:
     sum+=i
    i+=1
print("sum" ,sum)


# In[6]:


# accept the number and print sum of digits
num=int(input("enter number"))
sum=0
while num!=0:
    sum=sum+num%10
    num=num//10
print(sum)


# In[10]:


# reverse
num=int(input("enter number"))
while num!=0:
    print(num%10,end=" ")
    num=num//10


# In[11]:


str="application1889"
# sum of digits in given string-->1+8+8+9=26
i=0
sum=0
for i in str:
    if i.isdigit():
        sum+=int(i)
print(sum)


# In[13]:


# print n natural num using for loop
num=int(input("enter num"))
i=0
for i in range(1,11,1):
    print(i)


# In[1]:


str=input("enter string")
width=4
print(str)


# # collection type:
# 1. list
# 2. tuple
# 3. collection

# In[20]:


# list-->indexed,ordered,mutable,allows duplicate values.
lst=[334,56,334,"asdf",None,True]
# adding elements
lst.append(45) # with append we can only add one value
print(lst)
lst.insert(2,450)
lst[2]=53
lst.extend([3,2,1])
print(lst)


# In[24]:


# removing elements
del lst[-1]
print(lst)
# lst.pop()
r=lst.pop(1)
print(lst)
lst.remove(334) 
print(lst)


# In[29]:


lst1=[8,2,45,12]
lst1.reverse()
lst1


# In[37]:


lst1.sort(reverse=True)
lst1


# In[38]:


lst2=lst1
lst2
lst1.append(400)
lst1


# In[40]:


lst3=lst2.copy()
lst3


# In[44]:


# accept 3 sub marks of the student and should store values in a list and then return total marks of the student
n=int(input("enter no. of sub marks"))
marks=[]
for i in range(n):
    marks.append(int(input()))
print("sum",sum(marks))


# In[49]:


lst=[45,98,76,49,24]
for i in range[lst]:
    if lst[i]>lst[i+1]:
      large=last[i]
print(large)


# In[51]:


# tuple--> indexed,ordered,allows dup values,immutable
t1=(54,45,67,89)
lst=list(t1)
lst[1]=20
t1=tuple(lst)
t1


# In[57]:


# dict={key1:value1,key2:value2,....}
# rukes for keys:
# 1.keys should be unique
# 2.keys should be immutable(number,strings,tuple)
s1={"name":"shivani","rollno":21,"course":"cse","name":"annu"}
# adding new entry
s1["add"]="hyd"
s1["name"] # key value will be updated if you have same name for key
s1


# In[58]:


del s1["course"]
s1


# In[59]:


s1["add"]="kuk" # updating your dictionary
s1


# In[ ]:




